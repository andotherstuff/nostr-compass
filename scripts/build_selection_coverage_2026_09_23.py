#!/usr/bin/env python3
"""Build the Compass #41 editorial ledger from pinned, local exact-window inputs.

No collection or network access. Artifact provenance is not a collector record ID.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path('data/source_runs/source_run_2026-09-23_tuesday-2026-09-23-codex-1.json')
PROVISIONAL = Path('data/newsletter_workspace/selection_coverage_2026-09-23.json')
TRIAGE = Path('data/newsletter_workspace/triage_2026-09-23.md')
DRAFT = Path('content/en/newsletters/2026-09-23-newsletter.md')
EXPECTED_MANIFEST_HASH = '20249ed569dca8fb20b27d4d0df7d4f1cf830116b84d0da4670b8d7311844656'
GATES = {'direct_primary_evidence': 'primary_evidence', 'material_window_progress': 'in_window_progress',
         'nostr_surface': 'nostr_surface', 'distinct_from_recent_coverage': 'continuity_delta'}
AXES = ('nostr_significance', 'user_operator_impact', 'novelty', 'evidence_maturity', 'explanatory_value')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def load(path):
    return json.loads((ROOT / path).read_text())


def build():
    manifest = load(MANIFEST)
    provisional = load(PROVISIONAL)
    triage = (ROOT / TRIAGE).read_text()
    require(digest(ROOT / MANIFEST) == EXPECTED_MANIFEST_HASH, 'source manifest digest drift')
    require(manifest['schema_version'] == 2 and manifest['finalized'] is True and manifest['pass_id'] == 'tuesday-2026-09-23-codex-1', 'source pass drift')
    require(provisional['source_manifest_sha256'] == EXPECTED_MANIFEST_HASH and provisional['pass_id'] == manifest['pass_id'], 'provisional source binding drift')
    require(provisional['reporting_window'] == {'start': manifest['window']['since'], 'end': manifest['window']['until']}, 'source window drift')
    require(provisional['selected_count'] == len(provisional['selected']) == 35, 'selected count drift')
    require(len(provisional['source_reconciliation']['tagged_release_projects']) == 50 and
            len(provisional['source_reconciliation']['zapstore_only']) == 42 and
            provisional['source_reconciliation']['app_discovery']['count'] == 37, 'triage inventory count drift')
    families = manifest['families']
    require(set(families) == set(manifest['expected_families']) and len(families) == 10, 'source families drift')
    artifacts = {}
    for family, meta in families.items():
        if family == 'monthly-history':
            require(meta['status'] == 'not_applicable' and meta['artifact_path'] is None and not meta['candidate_ids'], 'monthly history drift')
            continue
        path = Path(meta['artifact_path'])
        require((ROOT / path).is_file() and digest(ROOT / path) == meta['artifact_sha256'], f'{family} artifact digest drift')
        artifacts[family] = json.loads((ROOT / path).read_text())
    projects = artifacts['projects']['projects']
    discovery = artifacts['app-discovery']['candidates']
    require(len(discovery) == 37, 'app discovery artifact count drift')
    numbered = {}
    for match in re.finditer(r'^([1-9]\d*)\. \*\*([SW]) — (.*?):\*\* (.*)$', triage, re.M):
        numbered[int(match[1])] = (match[2], match[3], match[4], match.group(0))
    require(set(numbered) == set(range(1, 93)), 'triage numbered inventory drift')
    for heading in ('## App discovery — 37/37', '## Owner-submitted and non-tagged projects'):
        require(heading in triage, f'missing triage decision section: {heading}')
    discovery_groups = {}
    for match in re.finditer(r'^- \*\*S — ([^*]+?) \((\d+)\):\*\* ([^\n]+)', triage, re.M):
        title, count, body = match.groups()
        if title not in ('repository discovery without a discrete in-window release or verified launch',
                         'mirror, fixture, template, fork, or test repository',
                         'tracked-owner sibling without a verified Nostr product milestone',
                         'outside scope or false-positive metadata'):
            continue
        names = [name.strip() for name in body.split('. Each ')[0].split('. These ')[0].split('. Owner ')[0].split('. Their ')[0].rstrip('.').split(';')]
        require(len(names) == int(count), f'app discovery group mismatch: {title}')
        for name in names:
            require(name not in discovery_groups, f'duplicate discovery name: {name}')
            discovery_groups[name] = (title, match.group(0))
    require(len(discovery_groups) == 37, 'triage discovery inventory drift')

    ledger = copy.deepcopy(provisional)
    ledger.update(final=True, source_pass_id=manifest['pass_id'], draft_sha256=digest(ROOT / DRAFT),
                  finalization_owner='Stage 5 selection ledger build; checker acceptance remains separate',
                  finalization_note='Deterministic local exact-window expansion. Artifact-only references are explicit; final checker acceptance requires artifact provenance and owner catch-up policy support.',
                  selection_policy={'minimum_score': 8, 'maximum_score': 10, 'require_no_zero_axis': True,
                                    'fixed_item_cap': None, 'qualified_items_must_publish': True},
                  hard_gate_fields=list(GATES.values()), score_axes=list(AXES))
    ledger['editorial_sources'], ledger['source_expansion'], ledger['candidates'] = [], [], []
    seen = set()
    project_releases = {}
    manifest_ids = {family: set(meta['candidate_ids']) for family, meta in families.items()}
    for repo, project in projects.items():
        for release in project.get('releases', []):
            raw = f'/repos/{repo}/releases:{release["id"]}'
            if raw in manifest_ids['projects']:
                project_releases[release['url']] = raw
    review_path = ROOT / 'data/newsletter_workspace/selection_review_2026-09-23.md'
    review_text = review_path.read_text()
    review_hash = digest(review_path)
    editorial_only = {'top:fips-initramfs-0.1.0', 'top:mintradar', 'top:relaykit',
                      'top:threshold-sessions', 'protocol:nwc13-pr7',
                      'deep-dive:nip-30', 'deep-dive:nip-71', 'release:white-noise-android-2026.9.21'}
    def record(candidate, family, locator, raw_id=None):
        cid = candidate['candidate_id']
        require(cid not in seen, f'duplicate candidate: {cid}')
        seen.add(cid)
        meta = families[family]
        require(locator and candidate.get('triage_decision_ref'), f'missing evidence or decision for {cid}')
        source_id = 'editorial:' + cid
        provenance = {'family': family, 'artifact_path': meta['artifact_path'],
                      'artifact_sha256': meta['artifact_sha256'], 'locator': locator}
        row = {'source_id': source_id, 'collector_source_ids': [f'{family}:{raw_id}'] if raw_id is not None else []}
        if cid in editorial_only and raw_id is None:
            primary = candidate['primary_sources'][0]
            require(primary in review_text, f'editorial review lacks primary URL: {cid}')
            row['editorial_provenance'] = {'path': str(review_path), 'sha256': review_hash, 'locator': primary}
        else:
            text = (ROOT / meta['artifact_path']).read_text()
            require(any(isinstance(value, str) and value and value in text for value in locator.values()),
                    f'no artifact locator: {cid}')
            row['artifact_provenance'] = provenance
        if raw_id is not None:
            require(raw_id in meta['candidate_ids'] and meta['dispositions'][raw_id]['decision'] == 'include', f'unknown collector include {family}:{raw_id}')
        ledger['editorial_sources'].append(row)
        ledger['source_expansion'].append({'source_id': source_id, 'candidate_ids': [cid]})
        ledger['candidates'].append(candidate)

    def project_evidence(name, url=None):
        matching = [(repo, project) for repo, project in projects.items() if project['name'].casefold() == name.casefold()]
        if url:
            releases = [(repo, rel) for repo, project in projects.items() for rel in project['releases'] if rel.get('url') == url]
            if len(releases) == 1:
                repo, rel = releases[0]
                raw_id = f'/repos/{repo}/releases:{rel["id"]}'
                return repo, raw_id if raw_id in families['projects']['candidate_ids'] else None
        return (matching[0][0], None) if len(matching) == 1 else (None, None)

    for item in provisional['selected']:
        cid = item['id']
        gates = {target: item['hard_gates'][source] for source, target in GATES.items()}
        override = item.get('override')
        require(all(gates.values()) or (cid == 'top:fips-initramfs-0.1.0' and override == 'owner_queued_catch_up' and not gates['in_window_progress'] and all(v for k, v in gates.items() if k != 'in_window_progress')), f'unexplained selected gate failure: {cid}')
        require(set(item['score_axes']) == set(AXES) and item['score_total'] == sum(item['score_axes'].values()), f'selected scores drift: {cid}')
        primary = item['primary_sources']
        require(primary and all(u.startswith('https://') for u in primary), f'selected primary evidence missing: {cid}')
        family = 'specs' if cid.startswith(('protocol:nip', 'protocol:bud', 'deep-dive:nip')) else 'projects'
        if cid.startswith('protocol:marmot') or cid.startswith('protocol:nwc'): family = 'projects'
        repo, raw_id = project_evidence(item['name'].split(' 0.')[0], primary[0]) if family == 'projects' else (None, None)
        candidate = {'candidate_id': cid, 'name': item['name'], 'hard_gate': gates,
                     'scores': copy.deepcopy(item['score_axes']), 'score_total': item['score_total'],
                     'triage': 'GREEN', 'final_disposition': 'include', 'reason': item['summary'],
                     'primary_sources': primary, 'draft_sources': [u for u in primary if u in (ROOT / DRAFT).read_text()],
                     'section': item['section'], 'triage_decision_ref': str(TRIAGE) + ('#owner-submitted-and-non-tagged-projects' if item['section'] == 'top_stories' else '#tagged-release-projects--5050' if item['section'] == 'tagged_releases' else '#other-source-families'),
                     'original_hard_gates': item['hard_gates']}
        if override:
            candidate['override'] = override
            if override == 'owner_queued_catch_up' and cid == 'top:fips-initramfs-0.1.0':
                owner_path = ROOT / 'data/newsletter_workspace/human_overrides_2026-09-23.md'
                require(primary[0] in owner_path.read_text() and 'catch-up' in owner_path.read_text().lower(),
                        f'owner override evidence missing: {cid}')
            elif override == 'owner_requested_after_release_verification' and cid == 'release:white-noise-android-2026.9.21':
                owner_path = ROOT / TRIAGE
                require(primary[0] in owner_path.read_text() and 'owner requested' in owner_path.read_text().lower(),
                        f'owner override evidence missing: {cid}')
            else:
                raise ValueError(f'unknown owner override: {cid}')
            candidate['owner_override_evidence'] = {'path': str(owner_path), 'sha256': digest(owner_path)}
        if family == 'projects':
            raw_id = next((project_releases[url] for url in primary if url in project_releases), raw_id)
        record(candidate, family, {'primary_url': primary[0], 'repository': repo} if repo else {'primary_url': primary[0]}, raw_id)

    for index in range(1, 93):
        section = 'tagged_release_projects' if index <= 50 else 'zapstore_only'
        row = provisional['source_reconciliation'][section][index - 1 if index <= 50 else index - 51]
        decision, label, reason, full = numbered[index]
        require((decision == 'W') == (row['verdict'] == 'selected'), f'triage disposition mismatch: {index}')
        if row['verdict'] == 'skip':
            require(label.split(' (`')[0].casefold() == row['name'].casefold(), f'triage name mismatch: {index}')
        if row['verdict'] == 'selected':
            continue
        family = 'projects' if index <= 50 else 'zapstore'
        if family == 'projects':
            repo, raw_id = project_evidence(row['name'])
            require(repo is not None, f'missing tagged project artifact: {row["name"]}')
            url = 'https://github.com/' + repo if 'github.com' not in repo else 'https://' + repo
            locator = {'project_key': repo}
        else:
            app_id = row['source_id'].removeprefix('zapstore:')
            apps = artifacts['zapstore']['apps']
            matches = [a for a in apps if a['app_id'] == app_id]
            require(len(matches) == 1, f'missing Zapstore app artifact: {app_id}')
            app = matches[0]
            matching_releases = [r for r in artifacts['zapstore']['releases'] if r['app_id'] == app_id]
            require(matching_releases, f'missing Zapstore release: {app_id}')
            raw_candidates = [r['release_id'] for r in matching_releases if r['release_id'] in families['zapstore']['candidate_ids'] and families['zapstore']['dispositions'][r['release_id']]['decision'] == 'include']
            raw_id = raw_candidates[0] if len(raw_candidates) == 1 else None
            url = app.get('app_repository') or next((u for u in re.findall(r'https://[^\s.]+(?:\.[^\s.]+)*', reason) if u), None)
            locator = {'app_id': app_id, 'release_ids': [r['release_id'] for r in matching_releases]}
        if url and not url.startswith('https://'):
            url = None
        candidate = {'candidate_id': row['source_id'], 'name': row['name'],
                     'hard_gate': {**dict.fromkeys(GATES.values()),
                                   'continuity_delta' if family == 'projects' else 'in_window_progress': False},
                     'scores': None, 'triage': 'SKIP', 'final_disposition': 'skip', 'reason': reason,
                     'primary_sources': [url.rstrip('.,')] if url else [], 'draft_sources': [], 'triage_decision_ref': row['decision_source'] + f':{index}'}
        record(candidate, family, locator, raw_id)

    artifact_names = {a['name']: a for a in discovery}
    artifact_repositories = {a['repository'].split('github.com/', 1)[-1].casefold(): a for a in discovery}
    matched = []
    for name in sorted(discovery_groups):
        app = artifact_names.get(name) or artifact_repositories.get(name.casefold())
        require(app is not None, f'triage/app-discovery name mismatch: {name}')
        matched.append(app['repository'])
        group, line = discovery_groups[name]
        url = app['repository']
        require(url.startswith('https://'), f'discovery primary URL missing: {name}')
        candidate = {'candidate_id': 'discovery:' + url.removeprefix('https://'), 'name': name,
                     'hard_gate': {**dict.fromkeys(GATES.values()), 'in_window_progress': False}, 'scores': None,
                     'triage': 'SKIP', 'final_disposition': 'skip', 'reason': group + ': ' + line.split(':** ', 1)[-1],
                     'primary_sources': [url], 'draft_sources': [],
                     'triage_decision_ref': str(TRIAGE) + '#app-discovery--3737:' + name}
        record(candidate, 'app-discovery', {'repository': url, 'name': name})
    require(len(set(matched)) == 37, 'duplicate or unmatched discovery artifact')
    require(len(ledger['candidates']) == 144 and len(seen) == 144, 'canonical editorial candidate count drift')
    return ledger


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        ledger = build()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + '\n')
    except (KeyError, IndexError, OSError, ValueError, TypeError) as exc:
        parser.exit(2, f'FAIL: {exc}\n')
    print(f'WROTE {args.output} ({len(ledger["candidates"])} candidates)')


if __name__ == '__main__':
    main()
