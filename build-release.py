"""Build this product's complete portable v0.1.0 candidate. Does not publish/install."""
from pathlib import Path
import hashlib, json, os, re, shutil, tempfile, unicodedata, zipfile
ROOT=Path(__file__).resolve().parent
PACKAGE=ROOT/'package'
meta=json.loads((PACKAGE/'VERSION.json').read_text(encoding='utf-8'))
TITLE,ID,VERSION=meta['name'],meta['id'],meta['version']
OUT=ROOT/f'release-v{VERSION}'
OUT.mkdir(exist_ok=True)
required=['README.md','INSTALL.md','NOTICE.md','VERSION.json',f'{TITLE}.png',meta['skill_root']+'/SKILL.md',meta['skill_root']+'/agents/openai.yaml']
if meta['product_kind']=='augment':required.append('.codex-plugin/plugin.json')
if ID=='build':required += ['build/references/workflows/UPSTREAM.json','build/references/workflows/conceive/SKILL.md','build/references/workflows/braid/SKILL.md']
for rel in required:
    if not (PACKAGE/rel).is_file():raise RuntimeError('Required package member missing: '+rel)
files=sorted(p for p in PACKAGE.rglob('*') if p.is_file())
if any(p.is_symlink() for p in PACKAGE.rglob('*')):raise RuntimeError('Package contains a symlink')
keys=set();maxlen=0
reserved=re.compile(r'^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?$',re.I)
for path in files:
    rel=path.relative_to(PACKAGE).as_posix();parts=rel.split('/')
    key=unicodedata.normalize('NFC',rel).casefold()
    if key in keys:raise RuntimeError('Case/Unicode member collision: '+rel)
    keys.add(key)
    for part in parts:
        if part in ('.','..') or reserved.match(part) or part.endswith(('.', ' ')) or re.search(r'[<>:"\\|?*\x00-\x1f]',part):raise RuntimeError('Nonportable member: '+rel)
        if len(part.encode('utf-8'))>255:raise RuntimeError('Long component: '+rel)
    destination=f'C:/Users/Customer/Downloads/{TITLE} v{VERSION}/'+rel
    size=len(destination.encode('utf-16-le'))//2;maxlen=max(maxlen,size)
    if size>=260:raise RuntimeError('Windows extraction length exceeds contract: '+rel)
    if any(part in ('.git','__pycache__','.pytest_cache') for part in parts):raise RuntimeError('Development cargo in package: '+rel)
    if path.suffix.lower()=='.md':
        text=path.read_text(encoding='utf-8')
        if re.search(r'(?i)(?:[A-Z]:\\|C:/Users/|E:/Indranet/|E:/Github/)',text):raise RuntimeError('Private absolute path in customer Markdown: '+rel)
        for link in re.findall(r'\]\(([^)]+)\)',text):
            target=link.strip('<>').split('#',1)[0]
            if not target or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',target):continue
            if not (path.parent/target).exists():raise RuntimeError('Broken relative resource: '+rel+' -> '+link)
# Catalog description parity is an exact routing requirement.
skill=(PACKAGE/meta['skill_root']/'SKILL.md').read_text(encoding='utf-8')
yaml=(PACKAGE/meta['skill_root']/'agents/openai.yaml').read_text(encoding='utf-8')
description=re.search(r'^description:\s*["\'](.*)["\']\s*$',skill,re.M)
short=re.search(r'^\s*short_description:\s*["\'](.*)["\']\s*$',yaml,re.M)
if not description or not short or description[1]!=short[1]:raise RuntimeError('Description/short_description parity failed')
zip_path=OUT/f'{TITLE} v{VERSION}.zip';candidate=OUT/(zip_path.name+'.candidate')
with zipfile.ZipFile(candidate,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for path in files:archive.write(path,path.relative_to(PACKAGE).as_posix())
with zipfile.ZipFile(candidate) as archive:
    if archive.testzip():raise RuntimeError('ZIP CRC failed')
    for path in files:
        if archive.read(path.relative_to(PACKAGE).as_posix())!=path.read_bytes():raise RuntimeError('ZIP/source parity failed')
    with tempfile.TemporaryDirectory(prefix=ID+'-extract-') as temp:
        archive.extractall(temp)
        for path in files:
            if (Path(temp)/path.relative_to(PACKAGE)).read_bytes()!=path.read_bytes():raise RuntimeError('Fresh extraction differs')
os.replace(candidate,zip_path)
for name in (f'{TITLE}.png',f'{TITLE} v{VERSION}.md',f'{TITLE} v{VERSION} Extra.md'):
    source=ROOT/'sidecars'/name
    if not source.is_file():raise RuntimeError('Missing staged sidecar: '+name)
    shutil.copy2(source,OUT/name)
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
report={'product_id':ID,'title':TITLE,'version':VERSION,'product_kind':meta['product_kind'],'package_members':len(files),'zip_sha256':digest(zip_path),'zip_bytes':zip_path.stat().st_size,'max_extracted_windows_utf16_units':maxlen,'checks':{'portable_namespace':'PASS','relative_links':'PASS','metadata_parity':'PASS','crc':'PASS','member_source_parity':'PASS','fresh_extraction':'PASS'},'independent_review':'not claimed','source_member_sha256':{p.relative_to(PACKAGE).as_posix():digest(p) for p in files},'bundle_artifacts':{p.name:{'sha256':digest(p),'bytes':p.stat().st_size} for p in [zip_path,OUT/f'{TITLE}.png',OUT/f'{TITLE} v{VERSION}.md',OUT/f'{TITLE} v{VERSION} Extra.md']}}
(OUT/'PACKAGE-CHECK.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('source_member_sha256','bundle_artifacts')},ensure_ascii=False,indent=2))