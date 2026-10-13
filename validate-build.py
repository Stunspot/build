"""Bounded structural check of BUILD, portable links and exact dependency snapshots."""
from pathlib import Path
import hashlib, json, re, sys
root=Path(__file__).resolve().parent / "package" / "build"
errors=[]
entry=(root/'SKILL.md').read_text(encoding='utf-8-sig')
meta=(root/'agents/openai.yaml').read_text(encoding='utf-8-sig')
desc=re.search(r'^description: "(.+)"$',entry,re.M).group(1)
short=re.search(r'^  short_description: "(.+)"$',meta,re.M).group(1)
if desc!=short: errors.append('metadata description mismatch')
manifest=root/'references/workflows/UPSTREAM.json'
if not manifest.exists(): errors.append('dependency snapshots absent')
else:
    data=json.loads(manifest.read_text(encoding='utf-8-sig'))
    if {s['name'] for s in data['snapshots']}!={'conceive','braid'}: errors.append('dependency roster differs')
    for source in data['snapshots']:
        base=manifest.parent/source['name']
        for member in source['files']:
            p=base/member['path']
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=member['sha256']:
                errors.append('snapshot mismatch: '+str(p))
        actual={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        if actual!={m['path'] for m in source['files']}: errors.append('unrecorded snapshot members: '+source['name'])
for p in root.rglob('*.md'):
    text=p.read_text(encoding='utf-8-sig')
    for raw in re.findall(r'\]\(([^)]+)\)',text):
        target=raw.split('#',1)[0].strip('<>')
        if not target or '://' in target or target.startswith(('mailto:','$','<')): continue
        if not (p.parent/target).is_file(): errors.append(f'missing reference: {p.relative_to(root)} -> {target}')
# These are product handoff resources, not a claim that model deliberation ran.
for expected in ['assets/build-handoff.md','assets/build-record.md','references/handoff.md','references/coordination.md','evals/cases.json','examples/walkthrough.md']:
    if not (root/expected).is_file(): errors.append('required resource absent: '+expected)
json.loads((root/'evals/cases.json').read_text(encoding='utf-8-sig'))
print(json.dumps({'ok':not errors,'scope':'metadata, reachable links, exact snapshots, expected handoff resources','errors':errors},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
