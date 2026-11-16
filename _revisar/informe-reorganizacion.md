# Informe de reorganización de la web estática

Fecha: 16 de noviembre de 2026. Todos los caminos de este informe son relativos a la carpeta del proyecto.

## Resultado

- Se ha aplicado el plan aprobado usando la distribución completa de `Home/dist/` como web principal.
- Se conservan los 77 archivos originales: 18 forman la web publicable y 59 están en `_revisar/`.
- Este informe es el único archivo nuevo dentro del proyecto; el total final es de 78 archivos.
- Se han actualizado 337 referencias de ruta en los 11 HTML publicados. Los textos, etiquetas, estructura y demás atributos HTML permanecen idénticos.
- Los otros 66 archivos conservan exactamente su SHA-256 original, incluidos todos los CSS, JS, imágenes y materiales archivados.
- No se han borrado archivos ni carpetas. Se han conservado también las carpetas vacías de la antigua distribución dentro de `_revisar/home/dist/`.
- No se han ejecutado comandos de git, instalado paquetes, minificado recursos ni convertido o comprimido imágenes.

## Estructura resultante

```text
/
├── index.html
├── become-partner/index.html
├── contacto/index.html
├── custom-development/index.html
├── diseno-web/index.html
├── gestion-documental/index.html
├── gestion-financiera/index.html
├── gestion-operativa/index.html
├── gobuilder-erp/index.html
├── precios/index.html
├── soporte/index.html
├── assets/
│   ├── css/
│   │   ├── brand.css
│   │   ├── home.css
│   │   └── styles.css
│   ├── js/
│   │   ├── home.js
│   │   └── script.js
│   ├── img/
│   │   ├── gonet-logo.jpeg
│   │   └── hero.webp
│   └── fonts/                     (vacia; no habia fuentes locales)
└── _revisar/
    ├── gobuilder/                 (34 archivos originales)
    ├── home/                      (24 archivos originales)
    ├── ds-store-raiz              (metadatos originales de la raiz)
    └── informe-reorganizacion.md  (este informe)
```

Para publicar basta con `index.html`, las diez carpetas de páginas y `assets/`. `_revisar/` contiene materiales históricos y el informe; no es necesario para servir la web.

## Archivos publicados: antes → después

| Antes | Después | Verificación |
|---|---|---|
| `Home/dist/Imagenes/Hero.webp` | `assets/img/hero.webp` | Bytes idénticos al original |
| `Home/dist/assets/gonet-logo.jpeg` | `assets/img/gonet-logo.jpeg` | Bytes idénticos al original |
| `Home/dist/become-partner/index.html` | `become-partner/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/brand.css` | `assets/css/brand.css` | Bytes idénticos al original |
| `Home/dist/contacto/index.html` | `contacto/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/custom-development/index.html` | `custom-development/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/diseno-web/index.html` | `diseno-web/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/gestion-documental/index.html` | `gestion-documental/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/gestion-financiera/index.html` | `gestion-financiera/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/gestion-operativa/index.html` | `gestion-operativa/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/gobuilder-erp/index.html` | `gobuilder-erp/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/home.css` | `assets/css/home.css` | Bytes idénticos al original |
| `Home/dist/home.js` | `assets/js/home.js` | Bytes idénticos al original |
| `Home/dist/index.html` | `index.html` | Solo atributos de rutas actualizados |
| `Home/dist/precios/index.html` | `precios/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/script.js` | `assets/js/script.js` | Bytes idénticos al original |
| `Home/dist/soporte/index.html` | `soporte/index.html` | Solo atributos de rutas actualizados |
| `Home/dist/styles.css` | `assets/css/styles.css` | Bytes idénticos al original |

## Archivos conservados en _revisar y motivo

Los 59 archivos de esta tabla se han movido y, cuando correspondía, renombrado. Su contenido conserva el SHA-256 original. La documentación, los generadores y las copias de HTML de esta carpeta son material histórico: conservan sus referencias y convenciones originales y no forman parte de las páginas publicadas.

| Antes | Después | Motivo |
|---|---|---|
| `.DS_Store` | `_revisar/ds-store-raiz` | Metadatos del Finder; conservados fuera de la web publicable. |
| `GoBuilder/.DS_Store` | `_revisar/gobuilder/ds-store` | Metadatos del Finder; conservados fuera de la web publicable. |
| `GoBuilder/BRAND.md` | `_revisar/gobuilder/brand.md` | Documentacion original; conservada con su contenido anterior. |
| `GoBuilder/Imagenes/.DS_Store` | `_revisar/gobuilder/imagenes/ds-store` | Metadatos del Finder; conservados fuera de la web publicable. |
| `GoBuilder/Imagenes/Hero.webp` | `_revisar/gobuilder/imagenes/hero.webp` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/QA.md` | `_revisar/gobuilder/qa.md` | Documentacion original; conservada con su contenido anterior. |
| `GoBuilder/README.md` | `_revisar/gobuilder/readme.md` | Documentacion original; conservada con su contenido anterior. |
| `GoBuilder/assets/gonet-logo.jpeg` | `_revisar/gobuilder/assets/gonet-logo.jpeg` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/become-partner/index.html` | `_revisar/gobuilder/become-partner/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/brand.css` | `_revisar/gobuilder/brand.css` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/contacto/index.html` | `_revisar/gobuilder/contacto/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/custom-development/index.html` | `_revisar/gobuilder/custom-development/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/gestion-documental/index.html` | `_revisar/gobuilder/gestion-documental/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/gestion-financiera/index.html` | `_revisar/gobuilder/gestion-financiera/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/gestion-operativa/index.html` | `_revisar/gobuilder/gestion-operativa/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/gobuilder-erp/index.html` | `_revisar/gobuilder/gobuilder-erp/index.html` | Antigua pantalla provisional; se conserva y se mantiene publicada la landing real de GoBuilder. |
| `GoBuilder/index.html` | `_revisar/gobuilder/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/precios/index.html` | `_revisar/gobuilder/precios/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/qa/hero-desktop.jpg` | `_revisar/gobuilder/qa/hero-desktop.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/hero-mobile.jpg` | `_revisar/gobuilder/qa/hero-mobile.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/hero-resultados.json` | `_revisar/gobuilder/qa/hero-resultados.json` | Resultado historico de validacion; conservado como referencia. |
| `GoBuilder/qa/hero-sin-resaltados.jpg` | `_revisar/gobuilder/qa/hero-sin-resaltados.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/hero-sin-simbolo.jpg` | `_revisar/gobuilder/qa/hero-sin-simbolo.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/home-completa.jpg` | `_revisar/gobuilder/qa/home-completa.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/home-desktop.jpg` | `_revisar/gobuilder/qa/home-desktop.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/home-mobile.jpg` | `_revisar/gobuilder/qa/home-mobile.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/menu-completo.jpg` | `_revisar/gobuilder/qa/menu-completo.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/menu-movil.jpg` | `_revisar/gobuilder/qa/menu-movil.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/qa/resultados.json` | `_revisar/gobuilder/qa/resultados.json` | Resultado historico de validacion; conservado como referencia. |
| `GoBuilder/qa/vista-previa-actualizada.jpg` | `_revisar/gobuilder/qa/vista-previa-actualizada.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `GoBuilder/script.js` | `_revisar/gobuilder/script.js` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/soporte/index.html` | `_revisar/gobuilder/soporte/index.html` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/styles.css` | `_revisar/gobuilder/styles.css` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `GoBuilder/tools/build_pages.py` | `_revisar/gobuilder/tools/build-pages.py` | Generador original; la nueva web estatica ya contiene los HTML finales y no necesita compilacion. |
| `GoBuilder/tools/test_navigation.cjs` | `_revisar/gobuilder/tools/test-navigation.cjs` | Prueba original de navegacion; conservada junto al codigo fuente anterior. |
| `Home/.DS_Store` | `_revisar/home/ds-store` | Metadatos del Finder; conservados fuera de la web publicable. |
| `Home/README_GONET_HOME.md` | `_revisar/home/readme-gonet-home.md` | Documentacion original; conservada con su contenido anterior. |
| `Home/home.css` | `_revisar/home/home.css` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `Home/home.js` | `_revisar/home/home.js` | Original o copia identica de un archivo publicado; conservado sin alterar sus bytes. |
| `Home/index.html` | `_revisar/home/index.html` | Plantilla de la portada; se publica su version completa que estaba en Home/dist/index.html. |
| `Home/qa/copy.json` | `_revisar/home/qa/copy.json` | Resultado historico de validacion; conservado como referencia. |
| `Home/qa/diseno-web-desktop.jpg` | `_revisar/home/qa/diseno-web-desktop.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/diseno-web-mobile.jpg` | `_revisar/home/qa/diseno-web-mobile.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/estructura.json` | `_revisar/home/qa/estructura.json` | Resultado historico de validacion; conservado como referencia. |
| `Home/qa/gobuilder-comparacion.jpg` | `_revisar/home/qa/gobuilder-comparacion.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/gobuilder-integridad.json` | `_revisar/home/qa/gobuilder-integridad.json` | Resultado historico de validacion; conservado como referencia. |
| `Home/qa/home-completa.jpg` | `_revisar/home/qa/home-completa.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/home-desktop.jpg` | `_revisar/home/qa/home-desktop.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/home-mobile.jpg` | `_revisar/home/qa/home-mobile.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-cuenta-iconos-visibles.jpg` | `_revisar/home/qa/menu-cuenta-iconos-visibles.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-cuenta-iconos.jpg` | `_revisar/home/qa/menu-cuenta-iconos.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-cuenta-tarjetas.jpg` | `_revisar/home/qa/menu-cuenta-tarjetas.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-cuenta.jpg` | `_revisar/home/qa/menu-cuenta.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-enlace-gobuilder.jpg` | `_revisar/home/qa/menu-enlace-gobuilder.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-espaciado.jpg` | `_revisar/home/qa/menu-espaciado.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/menu-mobile.jpg` | `_revisar/home/qa/menu-mobile.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/navegacion-gobuilder-corregida.jpg` | `_revisar/home/qa/navegacion-gobuilder-corregida.jpg` | Captura historica de revision; no es una imagen utilizada por la web. |
| `Home/qa/navegador.json` | `_revisar/home/qa/navegador.json` | Resultado historico de validacion; conservado como referencia. |
| `Home/tools/build.py` | `_revisar/home/tools/build.py` | Generador original; la nueva web estatica ya contiene los HTML finales y no necesita compilacion. |

## Duplicados detectados y conservados

Se detectaron 17 pares de archivos con contenido idéntico. No se ha eliminado ninguna copia; la tabla anterior indica su destino.

| Archivo original | Copia idéntica original |
|---|---|
| `GoBuilder/Imagenes/Hero.webp` | `Home/dist/Imagenes/Hero.webp` |
| `GoBuilder/assets/gonet-logo.jpeg` | `Home/dist/assets/gonet-logo.jpeg` |
| `GoBuilder/become-partner/index.html` | `Home/dist/become-partner/index.html` |
| `GoBuilder/brand.css` | `Home/dist/brand.css` |
| `GoBuilder/contacto/index.html` | `Home/dist/contacto/index.html` |
| `GoBuilder/custom-development/index.html` | `Home/dist/custom-development/index.html` |
| `GoBuilder/gestion-documental/index.html` | `Home/dist/gestion-documental/index.html` |
| `GoBuilder/gestion-financiera/index.html` | `Home/dist/gestion-financiera/index.html` |
| `GoBuilder/gestion-operativa/index.html` | `Home/dist/gestion-operativa/index.html` |
| `GoBuilder/index.html` | `Home/dist/gobuilder-erp/index.html` |
| `GoBuilder/precios/index.html` | `Home/dist/precios/index.html` |
| `GoBuilder/qa/hero-sin-simbolo.jpg` | `GoBuilder/qa/vista-previa-actualizada.jpg` |
| `GoBuilder/script.js` | `Home/dist/script.js` |
| `GoBuilder/soporte/index.html` | `Home/dist/soporte/index.html` |
| `GoBuilder/styles.css` | `Home/dist/styles.css` |
| `Home/dist/home.css` | `Home/home.css` |
| `Home/dist/home.js` | `Home/home.js` |

## Corrección de rutas

- Todas las referencias locales de los HTML publicados son relativas; no se usa `/` como raíz del dominio para cargar archivos o navegar entre páginas.
- Desde la portada se usan rutas como `assets/css/styles.css`, `assets/js/script.js`, `assets/img/gonet-logo.jpeg` y `gobuilder-erp/`.
- Desde las subpáginas se usan rutas como `../assets/css/styles.css`, `../assets/img/hero.webp`, `../` y `../contacto/`.
- Se han conservado las consultas de versión de CSS/JS, los fragmentos SVG y las anclas de navegación.
- También se han corregido las referencias locales de metadatos como `og:image`.
- No había referencias `url()` en los CSS ni rutas de archivos incrustadas en los JS que requiriesen edición; esos archivos se han movido sin modificar su contenido.
- Los enlaces externos, de correo y las URL `data:` se conservan tal como estaban.

## Verificación

| Comprobación | Resultado |
|---|---|
| Archivos originales conservados | 77 de 77 |
| Archivos con SHA-256 idéntico | 66; los otros 11 solo cambian atributos de rutas |
| Referencias locales verificadas | 337 correctas |
| Fragmentos internos e identificadores SVG verificados | 155 correctos |
| Nombres normalizados | Minúsculas, sin espacios, tildes ni caracteres especiales; `_revisar/` conserva el nombre solicitado |
| HTTP desde la raíz | 18 URL, todas con respuesta 200 |
| HTTP desde una subcarpeta de prueba | 18 URL, todas con respuesta 200 |
| Páginas abiertas en navegador | Las 11 desde raíz y las 11 bajo el prefijo de prueba |
| Consola del navegador | Sin errores ni advertencias registrados en las 22 cargas |
| Imágenes de carga inmediata | Sin imágenes rotas en las 22 cargas; todas las imágenes locales también se comprobaron por HTTP |
| Navegación real bajo subcarpeta | Inicio → Soluciones → GoBuilder ERP → Inicio: correcta |
| Contenido y presentación | HTML idéntico salvo rutas; CSS, JS e imágenes idénticos byte a byte |

Vista previa principal: [abrir la web](http://127.0.0.1:4174/). El servidor principal sirve ahora la raíz del proyecto. La prueba de prefijo `prueba-subcarpeta/` se realizó con un servidor temporal independiente para comprobar el comportamiento bajo una subcarpeta como la de un proyecto de GitHub Pages.

Para abrir la web desde esta carpeta en otra sesión, se puede usar Python si ya está disponible:

```sh
python3 -m http.server 4174 --bind 127.0.0.1 --directory .
```

## Problemas, dudas y límites de la comprobación

- No quedan referencias locales rotas ni errores de consola detectados en la web publicable.
- No hay fuentes locales: `assets/fonts/` se deja vacía. Se conserva la pila tipográfica existente, sin descargar fuentes.
- Las páginas «en preparación», los estados «Próximamente» y los destinos externos se mantienen sin cambios, como exige el alcance de la tarea.
- Los enlaces externos no se han verificado por red; la comprobación de HTTP y recursos se refiere a los archivos locales del sitio.
- La comprobación de subcarpeta valida las rutas para ese tipo de alojamiento. No se ha configurado ningún repositorio ni publicado la web en GitHub Pages o en un servidor externo.
- Las antiguas herramientas de generación y los informes de `_revisar/` se conservan como referencia histórica y no se han ejecutado después de la reorganización.
