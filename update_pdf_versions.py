from pathlib import Path
import hashlib
import re

root = Path(__file__).resolve().parent
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
for pdf in root.glob('article_*.pdf'):
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()[:12]
    pattern = re.compile(r'(?P<name>' + re.escape(pdf.name) + r')(?:\?v=[0-9a-f]+)?(?=["\'])')
    html = pattern.sub(lambda m: m.group('name') + '?v=' + digest, html)
page.write_text(html, encoding='utf-8')
print('Updated PDF links using file content hashes')
