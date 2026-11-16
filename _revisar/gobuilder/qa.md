# QA · GoNet / Overtake / paleta del logo

Actualización del 17 de octubre de 2026: fotografía `Imagenes/Hero.webp` en el bloque izquierdo y exactamente tres bullets de GoBuilder en el panel derecho. La imagen carga con sus dimensiones originales 1672 × 941. En escritorio se verificaron columnas en proporción 2,5:1 y altura idéntica de 481 px. En móvil se apilan.

Verificación de esta actualización: sin desbordamiento horizontal en 320, 375, 768, 1024 y 1440 px; fotografía cargada y tres elementos de lista en los cinco tamaños; consola sin avisos ni errores. Evidencias: `qa/hero-desktop.jpg`, `qa/hero-mobile.jpg` y `qa/hero-resultados.json`. La fotografía no se identifica como una captura del ERP; el espacio reservado de la sección de producto sigue pendiente.

El informe siguiente corresponde a la revisión base del 16 de octubre de 2026, antes del cambio de fotografía y panel. Esa revisión sustituyó el diseño basado en Holded por la composición de Overtake y la paleta indicada por el usuario.

## Resultado

- Cabecera con el logo original, navegación completa por páginas y desplegables de Funcionalidades, Soluciones, Servicios, Recursos y Cuenta.
- Portada con panel redondeado, titular grande, cápsula gráfica, botones con flecha circular y composición en azul marino y azul claro.
- Blanco como base y morado limitado a pequeños detalles. Paleta documentada en `BRAND.md` y aplicada desde `brand.css`.
- Copia del JPEG original verificada mediante SHA-256: mismos bytes, sin recorte de los elementos del logo, recoloreado o deformación.
- Ambas apariciones de la imagen cargan correctamente y declaran dimensiones 1600 × 800. La imagen conserva su proporción original.

## Contenido y estructura

Se verificaron los 97 fragmentos editoriales del documento original, conservando la corrección de marca GO NET y las once secciones. Se comprobó HTML en las diez páginas: etiquetas equilibradas, un solo H1 por página, identificadores y recursos válidos. No hay enlaces de cabecera que apunten a anclas; «Saltar al contenido» se conserva por accesibilidad. Title, description y metadatos sociales continúan presentes.

Los dos TODO de capturas reales del ERP se mantienen. El logotipo y los bloques editoriales no se presentan como pantallas reales del software. No se han añadido métricas, clientes o testimonios inventados.

## Responsive e imágenes

| Viewport | Disponible | Documento | Navegación |
| --- | --- | --- | --- |
| 320 px | 305 px | 305 px | Móvil |
| 375 px | 360 px | 360 px | Móvil |
| 768 px | 753 px | 753 px | Móvil |
| 1024 px | 1009 px | 1009 px | Escritorio |
| 1440 px | 1425 px | 1425 px | Escritorio |

No se detectó desplazamiento horizontal. Las imágenes estaban cargadas en los cinco tamaños. Se revisaron visualmente portada de escritorio, móvil y bloques interiores.

## Interacción y accesibilidad

- Los cinco desplegables principales muestran el grupo correspondiente, sin desbordamiento y con un único panel abierto a la vez.
- En móvil, Enter abre el menú y el submenú. El primer Escape cierra el submenú; el segundo cierra el menú general y devuelve el foco al botón, con indicador visible.
- Las seis FAQ se probaron con Enter y Espacio: todas alternan su estado y vuelven al estado inicial.
- Contraste calculado sobre 218 elementos visibles de texto en escritorio: sin resultados inferiores a 4,5:1; mínimo observado 5,20:1 frente al fondo opaco heredado.
- Movimiento reducido contemplado en CSS, sin modificar ajustes del usuario.
- Consola de la vista previa nueva: sin errores ni advertencias registradas.
- `node --check script.js`: correcto. No existían pruebas ni linter en el proyecto inicial; no se instalaron dependencias.

## Páginas de referencia

Se recorrieron las nueve rutas `/gestion-financiera`, `/gestion-operativa`, `/gestion-documental`, `/gobuilder-erp`, `/custom-development`, `/become-partner`, `/precios`, `/soporte` y `/contacto`. Todas muestran su título y la pantalla de preparación, cargan el logo y `brand.css`, y no producen desbordamiento. Conservan `noindex,nofollow`.

Estas pantallas permiten revisar el árbol completo; su contenido comercial todavía no está implementado. Vídeos, soporte remoto y cuentas sin URL siguen identificados como próximos.

## Evidencias

`qa/home-desktop.jpg`, `qa/home-mobile.jpg`, `qa/home-completa.jpg`, `qa/menu-completo.jpg`, `qa/menu-movil.jpg` y `qa/resultados.json` corresponden a esta versión.

## Pendientes y alcance

Faltan capturas reales del ERP, contenido de páginas secundarias, traducciones, recursos y backend de cuenta/contacto. Deben confirmarse dominio, correo y legales definitivos de GoNet. Una versión vectorial del logo permitiría un uso más flexible; el JPEG facilitado ya está incorporado.

No se ha realizado una auditoría WCAG exhaustiva con lector de pantalla ni pruebas en todos los navegadores y dispositivos. No se ha publicado la web en Internet. La vista previa local se mantiene activa a petición del usuario.
