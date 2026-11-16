"""Genera un sitio estático conservando GoBuilder como fuente compartida, solo lectura."""
from pathlib import Path
import hashlib
import json
import re
import shutil

HOME = Path(__file__).resolve().parent.parent
PRODUCT = HOME.parent / 'GoBuilder'
DIST = HOME / 'dist'

def product_fingerprint():
    return {
        str(path.relative_to(PRODUCT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(PRODUCT.rglob('*'))
        if path.is_file() and path.name != '.DS_Store'
    }

before = product_fingerprint()
product_html = (PRODUCT / 'index.html').read_text()
icons = re.search(r'<svg class="icon-definitions".*?</svg>', product_html, re.S).group()
DIST.mkdir(exist_ok=True)
home_html = (HOME / 'index.html').read_text().replace('<!-- shared:icons -->', icons)
(DIST / 'index.html').write_text(home_html)
# Página de servicio a partir del mismo contenido aprobado, sin duplicar su fuente.
head = re.search(r'<head>.*?</head>', home_html, re.S).group()
head = head.replace('GoNet Dynamics Technologies | Software, desarrollo y diseño web', 'Diseño web | GoNet Dynamics Technologies')
header = re.search(r'<header class="site-header">.*?</header>', home_html, re.S).group()
footer = re.search(r'<footer class="site-footer">.*?</footer>', home_html, re.S).group()
web = re.search(r'<section id="diseno-web".*?</section>', home_html, re.S).group()
web = web.replace('<h2 id="web-title">', '<h1 id="web-title">').replace('</h2>', '</h1>')
web = web.replace('href="/diseno-web/">Descubrir diseño web', 'href="/contacto/">Cuéntanos tu proyecto')
web_route = DIST / 'diseno-web'
web_route.mkdir(exist_ok=True)
(web_route / 'index.html').write_text(f'''<!doctype html><html lang="es">{head}<body class="corporate-home"><a class="skip-link" href="#contenido">Saltar al contenido</a>{icons}{header}<main id="contenido" tabindex="-1">{web}</main>{footer}</body></html>''')
for filename in ('home.css', 'home.js'):
    shutil.copy2(HOME / filename, DIST / filename)
for filename in ('styles.css', 'brand.css', 'script.js'):
    shutil.copy2(PRODUCT / filename, DIST / filename)
shutil.copytree(PRODUCT / 'assets', DIST / 'assets', dirs_exist_ok=True, ignore=shutil.ignore_patterns('.DS_Store'))
shutil.copytree(PRODUCT / 'Imagenes', DIST / 'Imagenes', dirs_exist_ok=True, ignore=shutil.ignore_patterns('.DS_Store'))
# La landing real está en GoBuilder/index.html; el antiguo gobuilder-erp/ es un placeholder.
product_route = DIST / 'gobuilder-erp'
product_route.mkdir(exist_ok=True)
(product_route / 'index.html').write_text(product_html)
routes = ('gestion-financiera', 'gestion-operativa', 'gestion-documental',
          'custom-development', 'become-partner', 'precios', 'soporte', 'contacto')
for route in routes:
    shutil.copytree(PRODUCT / route, DIST / route, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.DS_Store'))
after = product_fingerprint()
if before != after:
    raise RuntimeError('Se ha detectado un cambio externo en GoBuilder durante la generación.')
qa = HOME / 'qa'
qa.mkdir(exist_ok=True)
(qa / 'gobuilder-integridad.json').write_text(json.dumps({'unchanged': before == after, 'files': before}, indent=2))
print(f'Home corporativo generado: {DIST}')
print(f'GoBuilder conservado sin cambios: {len(before)} archivos verificados.')
