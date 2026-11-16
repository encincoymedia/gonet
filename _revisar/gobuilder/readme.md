# GO NET · GoBuilder ERP

Home revisada a partir de la composición visual de [Overtake](https://overtake-wbs.framer.website/) y el [árbol web facilitado](https://docs.google.com/spreadsheets/d/12StqEJvQQ1nreYd8sGZFJEwhO6A7xL6GPlrhQDizeQI/edit?gid=1723711605#gid=1723711605).

HTML, CSS y JavaScript sin dependencias, instalación o compilación. Marca **GO NET** y producto **GoBuilder ERP**. La carpeta inicial estaba vacía.

## Ver la web

Desde la carpeta del proyecto:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Abrir <http://127.0.0.1:4173/>. Si el servidor ya está activo, basta con abrir o recargar esa dirección. Las rutas parten de la raíz: revisar mediante el servidor, no con una URL `file:`.

## Diseño e identidad GoNet

La revisión actual utiliza la composición de Overtake: cabecera de una sola fila, panel principal redondeado, titular grande, una cápsula gráfica de construcción y botones con flecha circular. Las secciones alternan blanco, azul marino y azul claro. El morado se reserva para pequeños detalles.

La paleta procede de la imagen facilitada por el usuario:

| Uso | Color |
| --- | --- |
| Azul marino, titulares y CTA | `#07182e` |
| Azul de enlaces | `#0062c6` |
| Azul claro, superficies | `#a9def5` |
| Blanco | `#ffffff` |
| Morado de acento | `#6b46a8` |
| Morado claro de apoyo | `#eee8fa` |

`assets/gonet-logo.jpeg` es una copia intacta del JPEG facilitado. Se utiliza en la cabecera, con dimensiones explícitas y manteniendo su proporción. No se han eliminado elementos del logo, recoloreado o generado una identidad alternativa. El JPEG pesa aproximadamente 141 KB.

La portada utiliza `Imagenes/Hero.webp`, la fotografía de obra facilitada por el usuario. A su derecha, un panel azul marino presenta tres puntos sobre GoBuilder: control de costes, seguimiento de obra y organización de documentos. La fotografía y el panel tienen la misma altura en escritorio y se apilan en móvil.

La referencia orienta la composición; los colores y el logo son de GoNet. No se copian logotipos, métricas, testimonios o pantallas de Overtake. No se cargan fuentes o bibliotecas remotas.

Se mantienen las once secciones y el contenido editorial. Continúa pendiente la captura real del ERP en la sección de producto, indicada mediante el comentario `TODO: reemplazar por captura real GoBuilder`. La fotografía de portada no se presenta como una captura del software.

## Menú del sitio completo

Fuente: hoja «Árbol web», gid `1723711605`. El menú no usa anclas a secciones de la home.

| Grupo | Destinos y contenido previsto |
| --- | --- |
| Inicio | `/`, desde la marca |
| Funcionalidades | `/gestion-financiera`: Facturación, Contabilidad, Cobros en línea; `/gestion-operativa`: Proyectos, Stock, Integraciones; `/gestion-documental`: Gestión documental, Firma digital |
| Soluciones | `/gobuilder-erp`: Sistema de ofertas, Análisis, Precálculo de costes, Planificación, Tramitación de pedidos, Ejecución de pedidos, Almacenes, Facturación, Finanzas y Controlling |
| Servicios | `/custom-development` y `/become-partner` |
| Precios | `/precios` |
| Recursos | `/soporte`; Videotutoriales GoBuilder y Soporte remoto, sin URL en la hoja |
| Contacto | `/contacto` |
| Cuenta | Empezar gratis e Iniciar sesión, sin URL en la hoja |
| Idiomas | Español disponible; inglés y alemán previstos, pendientes de traducción |
| Legal | Política de privacidad, Términos y condiciones y Política de cookies |

Las nueve rutas definidas tienen una pantalla con cabecera, nombre de sección, aviso «Página en preparación» y regreso al inicio. Permiten recorrer el menú sin errores. **No constituyen la implementación de esas nueve páginas.** Llevan `noindex,nofollow`.

Vídeos, soporte remoto y cuenta se muestran como «Próximamente», sin inventar destinos o formularios. La cabecera solo presenta el idioma español disponible. Los legales conservan los destinos externos verificados de GoSolutions. El correo `info@gosolutions.ch` también procede de esa referencia y debe confirmarse para GO NET.

La única ancla de navegación es «Saltar al contenido», necesaria para accesibilidad.

## Archivos

- `index.html`: home, cabecera y footer.
- `styles.css`: estructura, responsive, interacción, movimiento reducido e impresión.
- `brand.css`: paleta GoNet, composición Overtake y adaptaciones de marca.
- `assets/gonet-logo.jpeg`: imagen original del logo facilitado.
- `Imagenes/Hero.webp`: fotografía de obra facilitada para la portada.
- `script.js`: menú móvil, desplegables, cierre exterior y con Escape, foco y página actual.
- Nueve directorios de ruta con `index.html`: pantallas de preparación.
- `tools/build_pages.py`: regenera esas pantallas con la cabecera y el pie actuales de la home.
- `QA.md` y `qa/`: revisión y capturas actualizadas.

Tras modificar cabecera o footer de `index.html`, sincronizar:

```sh
python3 tools/build_pages.py
node --check script.js
```

## Pendiente

Capturas reales del ERP y, si existe, una versión vectorial del logotipo; contenido de páginas secundarias; recursos y cuenta; traducciones; dominio y destinos definitivos de correo, contacto y legales. No hay formularios simulados ni backend nuevo. Añadir canonical, `og:url` e imagen social al confirmar dominio e imagen reales.

Entrega local para revisión. La vista previa se mantiene activa a petición del usuario. No se ha publicado un sitio en Internet.
