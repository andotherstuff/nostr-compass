#!/usr/bin/env python3
"""Conservative item/include/skip counts for source-pass receipts."""
import json, sys
from pathlib import Path
value=json.loads(Path(sys.argv[1]).read_text())
items=None
if isinstance(value,list): items=value
elif isinstance(value,dict):
    for key in ("items","events","results","projects","releases","updates","entries"):
        if isinstance(value.get(key),(list,dict)):
            candidate=value[key]; items=list(candidate.values()) if isinstance(candidate,dict) else candidate; break
if items is None: raise SystemExit("artifact schema has no countable collection")
skips=[]
if isinstance(value,dict) and isinstance(value.get("skipped"),list):
    for index,item in enumerate(value["skipped"]): skips.append({"index":index,"reason":item.get("reason","explicit collector skip") if isinstance(item,dict) else "explicit collector skip"})
count=len(items); print(json.dumps({"item_count":count,"page_count":1,"include_count":count,"skip_count":len(skips),"skip_evidence":skips},separators=(",",":")))
