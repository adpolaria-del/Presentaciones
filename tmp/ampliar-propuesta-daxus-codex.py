from pathlib import Path
import json, shutil
root=Path('/Users/josenicolassantiagomoreno/Documents/GitHub/Presentaciones')
details={
'1.1': {
 'teach':'Se explicará el recorrido que seguirá el proyecto: definir una necesidad, generar archivos con Codex, comprobarlos en el navegador, guardar versiones en GitHub e integrar el resultado en WordPress. Se aclarará la función de cada herramienta y la diferencia entre tener código generado y tener una página publicada.',
 'demo':'El docente mostrará la landing terminada y localizará su archivo HTML, su historial en GitHub y la página correspondiente en WordPress.',
 'outcome':'Identificar dónde se crea, dónde se guarda y dónde se publica cada parte del proyecto.'},
'1.2': {
 'teach':'Se presentarán los tres componentes de una página: HTML para títulos, textos, imágenes y enlaces; CSS para colores, tamaños y distribución; y JavaScript para interacciones. El alumno aprenderá a reconocerlos dentro de un archivo, localizar un elemento y entender qué tipo de cambio debe solicitar.',
 'demo':'Sobre una tarjeta sencilla, se cambiarán el texto, el color del botón y una interacción, mostrando qué parte del código produce cada resultado.',
 'outcome':'Distinguir un cambio de contenido, uno de diseño y uno de comportamiento.'},
'1.3': {
 'teach':'Se mostrará cómo acceder a Codex, iniciar sesión y seleccionar una carpeta de trabajo. Se explicará qué archivos puede utilizar el asistente, cómo dar contexto y por qué conviene revisar las acciones que propone. La configuración se demostrará con el entorno previamente preparado para el curso.',
 'demo':'El docente abrirá una carpeta vacía, solicitará un archivo de prueba, revisará el cambio y comprobará que el archivo se creó en la ubicación elegida.',
 'outcome':'Iniciar un proyecto y verificar que Codex está trabajando en la carpeta correcta.'},
'1.4': {
 'teach':'Se enseñará a completar un brief, es decir, una ficha que resume para quién se construye la página, qué servicio ofrece y qué acción se espera del visitante. Incluirá mensaje principal, secciones, colores, referencias, textos e imágenes disponibles para reducir decisiones improvisadas durante la construcción.',
 'demo':'Se completará la plantilla para un negocio de servicios y se pedirá a Codex una propuesta de estructura antes de generar la página.',
 'outcome':'Preparar una instrucción de trabajo con objetivo, contenido y límites claros.'},
'2.1': {
 'teach':'Se explicarán Git como historial de cambios y GitHub como lugar donde compartir y conservar el repositorio. Se introducirán copia local, commit como versión identificada y sincronización con el repositorio remoto. También se aclarará que guardar el código no respalda automáticamente la base de datos, los plugins ni los ajustes de WordPress.',
 'demo':'Se compararán dos versiones de un título y se mostrará cómo identificar el cambio y el momento en que se guardó.',
 'outcome':'Entender qué conserva el historial y cuándo hace falta una copia de seguridad del sitio.'},
'2.2': {
 'teach':'Se enseñará a crear un repositorio, asignarle un nombre y elegir su visibilidad. Después se iniciará sesión en GitHub Desktop y se clonará el repositorio, creando una copia en el computador. Se mostrará cómo ubicar esa carpeta y comprobar su correspondencia con el repositorio de GitHub.',
 'demo':'El docente creará un repositorio de práctica, lo clonará y abrirá la misma carpeta desde el explorador de archivos y GitHub Desktop.',
 'outcome':'Disponer de un repositorio remoto y una copia local correctamente relacionados.'},
'2.3': {
 'teach':'Se abrirá en Codex la carpeta clonada para que los cambios se realicen sobre el proyecto versionado. Se organizarán el brief, el archivo HTML y los recursos. Se explicará AGENTS.md como documento de instrucciones: conservar estilos específicos, limitar los cambios solicitados y revisar el resultado antes de publicarlo.',
 'demo':'Se redactarán reglas sencillas para una página de Elementor y se pedirá a Codex que explique el proyecto y proponga su siguiente paso.',
 'outcome':'Preparar una carpeta comprensible y establecer reglas reutilizables para trabajar con Codex.'},
'2.4': {
 'teach':'Se practicará el ciclo cambiar, revisar, guardar y sincronizar. El alumno aprenderá a leer una comparación de archivos para reconocer qué se añadió o eliminó, escribir un mensaje de commit descriptivo y enviar la versión a GitHub. Se distinguirá entre guardar un archivo y registrar un cambio en el historial.',
 'demo':'Se modificará un texto con Codex, se revisará en GitHub Desktop, se creará el commit y se comprobará su aparición en GitHub.',
 'outcome':'Guardar una versión identificable y confirmar que también existe en el repositorio remoto.'},
'3.1': {
 'teach':'Se convertirá el brief en un orden de secciones que responda las preguntas del visitante: qué se ofrece, para quién sirve, qué beneficios tiene y cómo contactar. Se explicará la función de la cabecera, la presentación principal, los servicios y las preguntas frecuentes, manteniendo una llamada a la acción principal.',
 'demo':'El docente dibujará un esquema simple de la landing y asignará a cada sección su contenido y el siguiente paso esperado del visitante.',
 'outcome':'Tener una estructura de página razonada y una acción de contacto definida.'},
'3.2': {
 'teach':'Se enseñará a traducir una referencia visual en decisiones concretas: paleta, tipografías, tamaños de títulos, anchos, espacios e imágenes. Se explicará cómo mantener esas decisiones entre secciones y cómo cambiar la distribución en pantallas pequeñas sin perder claridad ni legibilidad.',
 'demo':'Se preparará una ficha visual breve y se indicará cómo una sección de varias columnas debe reorganizarse en móvil.',
 'outcome':'Describir el diseño deseado con criterios que Codex pueda aplicar y el alumno pueda comprobar.'},
'3.3': {
 'teach':'Se construirá un prompt que reúna objetivo, contexto, contenido, referencia visual, formato de entrega y condiciones de aceptación. Se pedirá código preparado para Elementor, con estilos limitados al bloque y una adaptación móvil definida. Se explicará cómo dividir una solicitud grande en instrucciones pequeñas para revisar cada avance.',
 'demo':'Se comparará una petición vaga con otra concreta y se redactará el prompt para generar la primera sección del proyecto.',
 'outcome':'Solicitar una sección con instrucciones suficientes para evaluar si el resultado cumple lo pedido.'},
'3.4': {
 'teach':'Se generarán la cabecera y el bloque de presentación principal utilizando el prompt anterior. Se enseñará a abrir una vista previa, comparar el resultado con la referencia y detectar diferencias de tamaño, alineación o contenido. Las correcciones se pedirán indicando el elemento afectado y el resultado esperado.',
 'demo':'El docente ajustará el espacio o tamaño del título principal, comprobará que el resto de la sección se conserva y guardará el avance.',
 'outcome':'Obtener una primera sección revisada y aprender a mejorarla mediante cambios puntuales.'},
'4.1': {
 'teach':'Se ampliará la página con beneficios y servicios, reutilizando las decisiones visuales de la primera sección. Se explicará cómo dar a Codex textos definitivos, indicar imágenes y pedir tarjetas o columnas consistentes. Se revisarán orden de lectura, longitudes de texto y repetición de estilos para mantener una página coherente.',
 'demo':'Se construirán las secciones de beneficios y servicios a partir de un mismo patrón, corrigiendo una diferencia visual entre ellas.',
 'outcome':'Completar el contenido principal sin que cada sección parezca pertenecer a un diseño distinto.'},
'4.2': {
 'teach':'Se crearán enlaces que lleven a secciones de la misma página, un bloque desplegable de preguntas frecuentes y un botón de contacto. Se explicará qué resuelve cada interacción y cuándo utilizar JavaScript. El contacto del proyecto se realizará mediante un enlace; el procesamiento de formularios pertenece a otro alcance.',
 'demo':'Se probarán el desplazamiento entre secciones, la apertura de respuestas con ratón y teclado, y el destino del botón de contacto.',
 'outcome':'Incorporar navegación e interacciones sencillas y verificar que cada acción tiene un resultado correcto.'},
'4.3': {
 'teach':'Se mostrará cómo revisar la página a distintos anchos con las herramientas del navegador. Se identificarán problemas frecuentes: columnas demasiado estrechas, imágenes deformadas, textos que se salen del contenedor y botones pequeños. Se enseñará a describir el problema a Codex y comprobar también las vistas que antes funcionaban.',
 'demo':'Se corregirá una sección que genera desplazamiento horizontal en móvil y se volverá a revisar en escritorio, tablet y teléfono.',
 'outcome':'Detectar y corregir problemas visibles de adaptación sin limitarse a una única captura de pantalla.'},
'4.4': {
 'teach':'Se preparará la versión que se pegará en el widget HTML: contenido, estilos y scripts dentro de un bloque autocontenido. Se distinguirá ese bloque del documento completo utilizado para previsualizar, evitando trasladar etiquetas generales como html, head o body. Se limitarán los estilos mediante un contenedor propio para reducir conflictos.',
 'demo':'El docente revisará el archivo final, identificará los recursos y enlaces pendientes de sustituir y guardará una versión lista para integrar.',
 'outcome':'Tener un archivo identificable para Elementor y saber qué parte del proyecto debe copiarse.'},
'5.1': {
 'teach':'Se revisará el sitio de práctica antes de insertar código: permisos, copia de seguridad y página donde se hará la prueba. Se enseñará a crear un borrador, abrirlo con Elementor y elegir una plantilla que conserve o retire la cabecera y el pie del tema según el diseño previsto.',
 'demo':'Se preparará la página y se comparará su estructura vacía con la landing para evitar duplicar cabeceras o introducir márgenes inesperados.',
 'outcome':'Disponer de una página de prueba preparada para recibir el bloque sin alterar otras páginas.'},
'5.2': {
 'teach':'Se enseñará a insertar el widget HTML y pegar el bloque revisado. Se subirán las imágenes a la biblioteca de medios y se sustituirán las rutas del computador por URLs del sitio. Se comprobarán enlaces, estilos e interacciones para identificar recursos que todavía dependen de la carpeta local.',
 'demo':'El docente trasladará la landing a Elementor, corregirá una imagen que no carga y verificará el funcionamiento del bloque fuera del editor.',
 'outcome':'Integrar una página cuyos recursos se puedan cargar desde WordPress sin depender del equipo del docente.'},
'5.3': {
 'teach':'Se explicará por qué la página puede verse diferente al integrarse: anchos del contenedor, espacios de Elementor, estilos heredados del tema o caché. Se revisará cada causa por separado y se solicitarán correcciones limitadas al bloque. Como alternativa breve, se mostrará una sección simple en el bloque HTML personalizado de WordPress.',
 'demo':'Se corregirá una diferencia de ancho o tipografía y se comparará nuevamente la vista publicada con la referencia del proyecto.',
 'outcome':'Diagnosticar diferencias de integración y reconocer cuándo revisar permisos del editor o caché antes de modificar código.'},
'5.4': {
 'teach':'Se enseñará a definir el título y la dirección de la página, revisar el borrador y publicarlo en el sitio de práctica. La validación se hará desde la URL real, también sin sesión iniciada. Se comprobarán navegación, imágenes, contacto y visualización móvil para distinguir la vista del editor de la experiencia del visitante.',
 'demo':'El docente abrirá la página publicada en una ventana privada, recorrerá sus secciones y probará los enlaces principales.',
 'outcome':'Publicar una página y demostrar que puede visitarse y utilizarse desde su dirección final.'},
'6.1': {
 'teach':'Se realizará una revisión básica del resultado: orden de encabezados, descripción de imágenes, legibilidad, contraste, navegación con teclado y peso de los recursos. Se explicará qué puede corregirse dentro del bloque y qué depende de la configuración de WordPress. El alcance es una revisión introductoria, sin promesas de posicionamiento.',
 'demo':'Se detectará una incidencia, como una imagen sin descripción o un título mal jerarquizado, y se comprobará su corrección.',
 'outcome':'Usar una lista sencilla para mejorar la calidad de la página antes de darla por terminada.'},
'6.2': {
 'teach':'Se enseñará a describir un error mediante tres datos: qué debería ocurrir, qué ocurre realmente y cómo reproducirlo. Se mostrará cómo aportar a Codex una captura y, cuando corresponda, un mensaje de la consola. Se pedirá una explicación y una corrección sobre la parte afectada, revisando sus efectos.',
 'demo':'El docente resolverá un fallo sencillo de enlace o interacción y repetirá los pasos que lo provocaban para verificar la solución.',
 'outcome':'Pedir ayuda técnica con evidencia y comprobar que una respuesta de Codex realmente resuelve el problema.'},
'6.3': {
 'teach':'Se practicará una actualización completa: modificar el archivo, comprobarlo, guardar el commit, sincronizar GitHub y sustituir el bloque en Elementor. Se enseñará a recuperar el contenido de un archivo anterior, guardarlo como una nueva versión y volver a publicarlo. Se conservará el resto del historial del proyecto.',
 'demo':'Se cambiará un texto o estilo y después se recuperará su versión anterior, verificando tanto el archivo como la página en WordPress.',
 'outcome':'Actualizar y restaurar el bloque sabiendo que el repositorio y la página publicada se revisan por separado.'},
'6.4': {
 'teach':'Se organizará la entrega con la URL, el archivo final, el repositorio y un README: una guía breve de dónde está el código y cómo actualizarlo. Se explicará cómo reutilizar el proceso en otro negocio cambiando el brief, los contenidos y la identidad visual, sin arrastrar enlaces o datos del proyecto anterior.',
 'demo':'El docente recorrerá la entrega, señalará los archivos que se utilizaron y mostrará cómo iniciar una adaptación a un nuevo servicio.',
 'outcome':'Presentar un proyecto comprensible para otra persona y repetir el flujo de trabajo con orden.'}
}
exercises={
1:{'task':'Elegir un negocio de servicios, completar su brief y pedir a Codex un plan de secciones sin generar todavía la página completa. Guardar la ficha en la carpeta del proyecto.','evidence':'Brief con público, oferta, objetivo, contenidos y referencias. El alumno debe poder explicar qué hará cada herramienta.'},
2:{'task':'Crear y clonar el repositorio de práctica, abrirlo en Codex y guardar el brief y un archivo inicial. Hacer un cambio pequeño, revisarlo y sincronizar su commit.','evidence':'El archivo local y el de GitHub reflejan el mismo cambio; el mensaje del commit permite entender qué se modificó.'},
3:{'task':'Definir la estructura y el estilo de la landing, escribir el prompt de la primera sección y generar una vista previa. Solicitar una mejora puntual y guardar la versión revisada.','evidence':'La sección contiene el mensaje y la acción principal del brief; la corrección respeta los elementos que ya estaban aprobados.'},
4:{'task':'Completar beneficios, servicios, preguntas frecuentes y contacto. Revisar tres tamaños de pantalla, corregir una incidencia y guardar el bloque autocontenido que se insertará en Elementor.','evidence':'Los enlaces y el acordeón funcionan, no hay desplazamiento horizontal en móvil y el archivo para el widget está claramente identificado.'},
5:{'task':'Crear la página de práctica, insertar el bloque, sustituir las rutas de imágenes y publicar. Abrir la URL sin sesión y guardar capturas de escritorio y móvil.','evidence':'La página carga desde su URL, muestra sus recursos y permite utilizar la navegación y el contacto fuera del editor.'},
6:{'task':'Aplicar la lista de revisión, resolver una incidencia y demostrar una actualización con recuperación del archivo anterior. Preparar el README y la entrega final del proyecto.','evidence':'Hay una versión final identificable en GitHub, una página funcional y pasos escritos para repetir una actualización o recuperación.'}
}
assert len(details)==24
(root/'tmp/pdfs/daxus-codex/lecciones-ampliadas.json').write_text(json.dumps({'lessons':details,'exercises':exercises},ensure_ascii=False,indent=2))
p=root/'tmp/crear-propuesta-daxus-codex.py'
s=p.read_text()
if 'lecciones-ampliadas.json' not in s:
    shutil.copy2(p,root/'tmp/pdfs/daxus-codex/crear-propuesta-version-inicial.py')
    s=s.replace("pages=[]", "expanded=json.loads((root/'tmp/pdfs/daxus-codex/lecciones-ampliadas.json').read_text())\npages=[]")
    s=s.replace('{i:02d} / 07', '{i:02d} / 10')
    start=s.index('def render_mod(m):')
    end=s.index("page('Metodología y entrega'",start)
    replacement='''def render_mod(m):
    lessons=[]
    for i,(title,minutes,_) in enumerate(m['lessons'],1):
        key=f"{m['n']}.{i}"
        d=expanded['lessons'][key]
        lessons.append(f'<article class="detail-lesson"><div class="detail-heading"><span class="lesson-id">{key}</span><h3>{escape(title)}</h3><span class="lesson-time">{minutes} min</span></div><p><b>Qué se enseñará.</b> {escape(d["teach"])}</p><p><b>Demostración en pantalla.</b> {escape(d["demo"])}</p><p class="learning"><b>Al terminar.</b> {escape(d["outcome"])}</p></article>')
    exercise=expanded['exercises'][str(m['n'])]
    content=''.join(lessons)
    return f'<article class="module expanded-module"><div class="modulehead"><span class="num">{m["n"]:02d}</span><h2>{m["title"]}</h2><span class="duration">{m["min"]} min</span></div><p class="objective"><b>Objetivo:</b> {m["objective"]}</p>{content}<div class="exercise"><p><b>Ejercicio del módulo:</b> {exercise["task"]}</p><p><b>Cómo comprobar el aprendizaje:</b> {exercise["evidence"]}</p><p class="practice-note">Práctica independiente del alumno; adicional al tiempo de video.</p></div></article>'
for m in mods:
    page('Programa detallado', '', f'<p class="eyebrow">Programa detallado · Módulo {m["n"]} de 6</p>'+render_mod(m), 'module-page')
'''
    s=s[:start]+replacement+s[end:]
    s=s.replace('assert len(pages)==7', 'assert len(pages)==10')
    extra='''
.detail-lesson{padding:3mm 0;border-bottom:1px solid #dce4dd}.detail-heading{display:flex;gap:2.5mm;align-items:baseline;margin-bottom:1.5mm}.detail-heading h3{font-size:11pt;flex:1;margin:0;line-height:1.2}.detail-heading .lesson-id{font-size:9.3pt;min-width:7mm}.detail-lesson p{font-size:9.4pt;line-height:1.38;margin:0 0 1.2mm;color:#42564d}.detail-lesson p:last-child{margin-bottom:0}.detail-lesson p b{color:#1d3e32}.detail-lesson .learning{color:#176858}.expanded-module .objective{margin:0 0 1mm}.expanded-module .exercise{font-size:9.2pt;padding:3mm;margin-top:3mm}.practice-note{font-size:8.2pt;color:#66796b}.module-page .module h2{font-size:18pt}.module-page .modulehead{margin-bottom:3mm}
@media screen and (max-width:820px){.detail-heading{flex-wrap:wrap}.detail-heading h3{font-size:12pt}.detail-lesson p{font-size:10.5pt}.module-page .module h2{font-size:16pt}}
'''
    s=s.replace("expanded=json.loads", "css+='''"+extra+"'''\nexpanded=json.loads")
    # More explicit supporting resource descriptions, within the established scope.
    s=s.replace('público, objetivo, secciones, contenido y referencias visuales.</li>', 'ficha para definir público, oferta, objetivo, secciones y referencias antes de pedir código.</li>')
    s=s.replace('planificación, construcción, adaptación móvil, corrección de errores y revisión final.</li>', 'ejemplos comentados para planificar, construir, adaptar a móvil, corregir errores y revisar el resultado.</li>')
    s=s.replace('archivo inicial, versiones de cada módulo, bloque HTML final y README con instrucciones.</li>', 'archivo inicial, versiones por módulo y bloque final para comparar avances; README con pasos de uso y actualización.</li>')
    s=s.replace('textos, imágenes de ejemplo y referencias de estilos.</li>', 'textos e imágenes de ejemplo para seguir la demostración aunque el alumno no tenga una marca propia.</li>')
    s=s.replace('lista de comprobación y pasos para recuperar una versión.</li>', 'lista para verificar enlaces, imágenes y móvil; pasos para actualizar el widget y recuperar una versión.</li>')
    p.write_text(s)
print('Ampliadas 24 lecciones y 6 ejercicios; previstos 10 folios.')
