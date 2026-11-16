from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
header = re.search(r'<header class="site-header">.*?</header>', html, re.S).group()

footer = re.search(r'<footer class="site-footer">.*?</footer>', html, re.S).group()
icons = re.search(r'<svg class="icon-definitions".*?</svg>', html, re.S).group()
routes = {
    '/gestion-financiera': ('Gestión financiera', 'Funcionalidades', 'Presupuestos y ofertas, control de costes, facturación y contabilidad.'),
    '/gestion-operativa': ('Gestión operativa', 'Funcionalidades', 'Proyectos, planificación, compras, almacenes y seguimiento del trabajo.'),
    '/gestion-documental': ('Gestión documental', 'Funcionalidades', 'Documentación de obra, gestión de archivos y firma digital.'),
    '/gobuilder-erp': ('GoBuilder ERP', 'Soluciones', 'Del presupuesto al cierre de obra: conoce el software para construcción.'),
    '/custom-development': ('Desarrollo a medida', 'Servicios', 'Un espacio para las soluciones adaptadas a las necesidades de tu empresa.'),
    '/become-partner': ('Programa Partners', 'Servicios', 'Un espacio para conocer el programa de colaboración de GO NET.'),
    '/precios': ('Planes y precios', 'GO NET', 'Aquí podrás consultar las opciones para tu empresa.'),
    '/soporte': ('Centro de ayuda', 'Recursos', 'Documentación, recursos y ayuda para conocer GoBuilder ERP.'),
    '/contacto': ('Contacto', 'GO NET', 'Ponte en contacto con el equipo para conocer GoBuilder ERP.'),
}
for route, (title, parent, description) in routes.items():
    if route == '/contacto':
        action = '<a class="button button-blue" href="mailto:info@gosolutions.ch">Escribir a info@gosolutions.ch</a>'
    else:
        action = '<a class="button button-blue" href="/">Volver al inicio</a>'
    content = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><link rel="icon" href="data:,"><title>{title} | GO NET</title><meta name="description" content="{description}"><link rel="stylesheet" href="/styles.css?v=5"><link rel="stylesheet" href="/brand.css?v=10"><script src="/script.js?v=4" defer></script></head><body><a class="skip-link" href="#contenido">Saltar al contenido</a>{icons}{header}<main id="contenido" class="planned-page" tabindex="-1"><div class="container"><p class="eyebrow">{parent}</p><h1>{title}</h1><p class="planned-intro">{description}</p><div class="page-in-preparation"><span>Página en preparación</span><p>Esta sección forma parte de la estructura del sitio. Su contenido se incorporará en una próxima fase.</p></div>{action}</div></main>{footer}</body></html>'''
    directory = root / route.lstrip('/')
    directory.mkdir(exist_ok=True)
    (directory / 'index.html').write_text(content)

print('Nueve páginas de referencia regeneradas con la cabecera y el pie actuales.')
