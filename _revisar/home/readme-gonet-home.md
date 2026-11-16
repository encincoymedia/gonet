# Home corporativo · GoNet Dynamics Technologies

Portada corporativa implementada a partir del documento `02_PROMPT_CODEX_HOME_CORPORATIVO.md`, dentro de la carpeta **Home** indicada por el usuario. Presenta software empresarial, desarrollo a medida y diseño web. GoBuilder ERP aparece como producto destacado, con acceso a su landing real.

## Arquitectura y vista previa

HTML, CSS y JavaScript locales, sin dependencias ni instalación. El directorio raíz del sitio generado es `Home/dist`: su `/index.html` corresponde a GoNet, y `/gobuilder-erp/index.html` corresponde a la landing de producto.

Desde esta carpeta:

```sh
python3 tools/build.py
python3 -m http.server 4174 --bind 127.0.0.1 --directory dist
```

Vista previa corporativa: <http://127.0.0.1:4174/>. La referencia original de GoBuilder conserva su vista previa independiente en el puerto 4173.

Se debe revisar mediante HTTP. Abrir el archivo con `file:` no resuelve las rutas del sitio. Tras editar los archivos fuente, regenerar `dist` y recargar el navegador.

## Archivos y reutilización

- `index.html`: contenido corporativo, once secciones, cabecera, pie y metadatos.
- `home.css`: composición corporativa adicional, usando los tokens existentes.
- `home.js`: complemento para gestionar anclas de navegación cuando corresponda.
- `tools/build.py`: genera el sitio estático y comprueba la integridad del producto.
- `dist/`: resultado listo para servir como sitio estático.
- `qa/`: capturas y resultados de comprobación.

`../GoBuilder/styles.css`, `../GoBuilder/brand.css` y `../GoBuilder/script.js` son las fuentes compartidas de fundamentos, componentes y navegación. El generador los incorpora a `dist` sin modificarlos. Así no se mantiene una segunda versión manual del sistema gráfico. Para cambiar estilos generales en el futuro, editar su fuente compartida y regenerar el Home; el CSS específico de esta portada permanece en `home.css`.

Se heredan exactamente la paleta, la pila tipográfica, la escala y pesos de títulos, los contenedores, los radios, los botones con flecha circular, las tarjetas de capacidades, las tarjetas financieras, los paneles de servicio, el proceso, los desplegables, las FAQ, el foco visible y las reglas de movimiento reducido. La pila es `Inter, Arial, Helvetica, sans-serif`; el repositorio no incluye un archivo de Inter ni se descargan fuentes externas, por lo que se usa el respaldo disponible en el navegador.

La paleta es la de GoBuilder: azul marino `#07182e`, azul claro `#a9def5`, azul de enlaces `#0062c6`, blanco y morado puntual `#6b46a8`. No se introduce una paleta alternativa, degradados ni resaltados de fondo en el párrafo del hero. El titular corporativo tampoco incorpora el símbolo que el usuario pidió retirar.

## Rutas

| Ruta | Contenido |
| --- | --- |
| `/` o `/index.html` | Nuevo Home corporativo de GoNet |
| `/gobuilder-erp/` | Copia íntegra de la landing real `GoBuilder/index.html` |
| `/diseno-web/` | Página de servicio generada con el mismo texto aprobado y los cuatro puntos de la sección de diseño web; CTA a contacto |
| `/gestion-financiera/`, `/gestion-operativa/`, `/gestion-documental/` | Páginas de referencia existentes |
| `/custom-development/`, `/become-partner/`, `/precios/`, `/soporte/`, `/contacto/` | Páginas de referencia existentes |

Las ocho páginas de referencia conservan su contenido y `noindex,nofollow`. Son pantallas de preparación, no se presentan como nuevas páginas comerciales completas. Contacto mantiene el enlace de correo ya existente. Los enlaces de la cabecera llevan a páginas; las anclas del hero sirven para explorar las tres áreas dentro de la portada.

El generador distingue la landing real del antiguo placeholder `GoBuilder/gobuilder-erp/index.html`: en la nueva distribución, la ruta de producto utiliza siempre `GoBuilder/index.html`. Ningún archivo fuente de GoBuilder se mueve, reemplaza o edita. Se verificaron 31 archivos del producto por hash durante la generación.

## Activos, contenido y SEO

- Logo auténtico: `GoBuilder/assets/gonet-logo.jpeg`, conservando sus bytes y proporción 1600 × 800, en cabecera, pie y metadatos sociales.
- La fotografía de obra `GoBuilder/Imagenes/Hero.webp` se incluye para que la landing del producto funcione; no se utiliza como imagen corporativa general.
- Al no existir una captura aprobada del ERP, el bloque de producto utiliza una composición tipográfica. No simula una interfaz.
- Los textos del documento se mantienen: 65 fragmentos editoriales verificados automáticamente, además de la revisión de títulos, etiquetas y pie.
- Title, description, `og:title` y `og:description` del Home coinciden con los solicitados. Hay un solo H1 y `lang="es"`.
- `og:image` apunta al activo oficial existente. Al confirmar el dominio definitivo, convertir esa ruta en URL absoluta y añadir canonical y `og:url`.
- No se anuncian cuentas, traducciones EN/DE, videotutoriales ni soporte remoto como publicados. No hay formularios simulados, estadísticas, clientes o testimonios inventados.

## Validación

- Sin desbordamiento horizontal en 320, 375, 768, 1024 y 1440 px, incluyendo tarjetas y contenedores interiores. También se comprobó 768 × 375 en horizontal.
- Menú móvil, apertura exclusiva de desplegables y Escape con retorno de foco comprobados. Al navegar a Diseño web, el menú vuelve cerrado.
- Las cinco FAQ responden a Enter y Espacio y recuperan su estado inicial.
- El CTA «Explorar soluciones» llega a su sección por debajo de la cabecera fija.
- Acceso a la landing real de GoBuilder comprobado en navegador. Ambas páginas usan la misma pila tipográfica, paleta y botones de radio 100 px; comparación visual guardada en `qa`.
- Contraste calculado sobre 151 elementos de texto visibles: sin incumplimientos AA en la muestra, mínimo observado 5,37:1. No sustituye una auditoría completa con lector de pantalla.
- Recursos y enlaces locales comprobados contra la distribución generada. Un H1 por página, sin identificadores duplicados. `node --check home.js` correcto.

## Antes de publicar

Confirmar dominio, imagen social definitiva, correo y páginas legales corporativas. Los destinos legales de GoSolutions se heredan de la referencia existente y deben confirmarse para GoNet. Completar el contenido de las páginas de referencia y confirmar la disponibilidad de documentación y materiales de ayuda. Validar el alcance comercial de las etapas de implementación y acompañamiento propuestas para marketing. Publicar traducciones y acceso de cuenta solo cuando existan sus URLs aprobadas.

Esta entrega es local para revisión. La vista previa queda activa a petición del usuario; no se ha publicado un sitio en Internet.
