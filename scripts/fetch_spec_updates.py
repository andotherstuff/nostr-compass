#!/usr/bin/env python3
"""Fetch exact-window activity for every tracked Nostr-adjacent spec family."""
from __future__ import annotations
import argparse, json, os, subprocess, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
sys.path.insert(0, str(Path(__file__).parent))
from source_collector_receipt import emit_receipt, native_evidence, observed_page
ROOT=Path(__file__).parents[1]; DEFAULT_CONFIG=ROOT/"data/spec_sources.json"; OUTPUT_DIR=ROOT/"data/spec_updates"
def parse_time(value:str)->datetime: return datetime.fromisoformat(value.replace("Z","+00:00"))
def in_window(value:str|None,since:str,until:str)->bool: return bool(value) and parse_time(since)<=parse_time(value)<parse_time(until)
def family_result(family:dict[str,str],commits:list[dict[str,Any]],pulls:list[dict[str,Any]],since:str,until:str)->dict[str,Any]:
    selected_pulls=[]
    for p in pulls:
        if any(in_window(p.get(f),since,until) for f in ("created_at","updated_at","merged_at")):
            selected_pulls.append({"number":p["number"],"title":p["title"],"state":"merged" if p.get("merged_at") else p.get("state","open"),"created_at":p.get("created_at"),"updated_at":p.get("updated_at"),"merged_at":p.get("merged_at"),"url":p["html_url"]})
    selected_commits=[{"sha":c["sha"],"date":c["commit"]["author"]["date"],"title":c["commit"]["message"].splitlines()[0],"url":c["html_url"]} for c in commits if in_window(c["commit"]["author"]["date"],since,until)]
    return {**family,"status":"active" if selected_commits or selected_pulls else "quiet","window":{"since":since,"until":until},"commits":selected_commits,"pull_requests":selected_pulls}
def gh_json(endpoint:str)->Any:
    result=subprocess.run(["gh","api",endpoint],check=True,text=True,capture_output=True); return json.loads(result.stdout)
def gh_pages(endpoint:str,source:str,since:str,until:str,max_pages:int=100)->tuple[list[dict],list[dict]]:
    items=[]; evidence=[]
    for page_no in range(1,max_pages+1):
        separator="&" if "?" in endpoint else "?"; page=gh_json(f"{endpoint}{separator}per_page=100&page={page_no}")
        if not isinstance(page,list): raise RuntimeError(f"{source} returned non-list page")
        exhausted=len(page)<100
        evidence.append(observed_page(source=source,count=len(page),cap=100,exhausted=exhausted,since=since,until=until,cursor=str(page_no)))
        items.extend(page)
        if exhausted: return items,evidence
    raise RuntimeError(f"{source} reached the {max_pages}-page safety cap")
def fetch_family(family:dict[str,str],since:str,until:str)->tuple[dict[str,Any],list[dict],list[str],dict[str,dict[str,str]]]:
    repo=family["repo"]
    commits,cp=gh_pages(f"repos/{repo}/commits?since={since}&until={until}",f"{repo}:commits",since,until)
    pulls,pp=gh_pages(f"repos/{repo}/pulls?state=all&sort=updated&direction=desc",f"{repo}:pulls",since,until)
    result=family_result(family,commits,pulls,since,until); included={f"{repo}:commit:{c['sha']}" for c in result["commits"]}|{f"{repo}:pull:{p['number']}" for p in result["pull_requests"]}
    ids=[f"{repo}:commit:{c['sha']}" for c in commits]+[f"{repo}:pull:{p['number']}" for p in pulls]
    disp={i:{"decision":"include" if i in included else "skip","reason":"activity timestamp is inside exact window" if i in included else "no activity timestamp inside exact window"} for i in ids}
    return result,cp+pp,ids,disp
def iso_midnight(day:datetime)->str: return day.astimezone(timezone.utc).strftime("%Y-%m-%dT00:00:00Z")
def main()->int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--since-days",type=int,default=8); p.add_argument("--until"); p.add_argument("--config",type=Path,default=DEFAULT_CONFIG); a=p.parse_args()
    started=datetime.now(timezone.utc).isoformat().replace("+00:00","Z")
    if os.environ.get("COMPASS_SOURCE_PASS_ID"):
        since=os.environ["COMPASS_WINDOW_SINCE"]; until=os.environ["COMPASS_WINDOW_UNTIL"]; until_day=parse_time(until)
    else:
        until_day=datetime.strptime(a.until,"%Y-%m-%d").replace(tzinfo=timezone.utc) if a.until else datetime.now(timezone.utc).replace(hour=0,minute=0,second=0,microsecond=0)+timedelta(days=1); since=iso_midnight(until_day-timedelta(days=a.since_days)); until=iso_midnight(until_day)
    config=json.loads(a.config.read_text()); families=[]; pages=[]; ids=[]; dispositions={}
    for family in config["spec_families"]:
        result,paged,candidates,disp=fetch_family(family,since,until); families.append(result); pages.extend(paged); ids.extend(candidates); dispositions.update(disp)
    payload={"generated_at":datetime.now(timezone.utc).isoformat(),"window":{"since":since,"until":until},"families":families}; OUTPUT_DIR.mkdir(parents=True,exist_ok=True); output=OUTPUT_DIR/f"spec_updates_{until_day.strftime('%Y-%m-%d')}.json"; output.write_text(json.dumps(payload,indent=2)+"\n")
    if os.environ.get("COMPASS_SOURCE_PASS_ID"):
        evidence=native_evidence(family="specs",since=since,until=until,started=started,pages=pages,candidate_ids=ids,dispositions=dispositions,query={"repositories":[f["repo"] for f in config["spec_families"]],"upper_bound_enforced":"server-for-commits,collector-for-pulls"}); emit_receipt(family="specs",artifact=output,collector=Path(__file__),evidence=evidence)
    print(f"Wrote {output}"); return 0
if __name__=="__main__": raise SystemExit(main())
