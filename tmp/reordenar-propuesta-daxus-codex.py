from pathlib import Path
import json, shutil
root=Path('/Users/josenicolassantiagomoreno/Documents/GitHub/Presentaciones')
work=root/'tmp/pdfs/daxus-codex'
old=json.loads((work/'lecciones-ampliadas.json').read_text())
mods=[]; details={}; exercises={}
def module(n,title,objective,lessons,task,evidence):
    short=[]
    for i,(name,minutes,teach,demo,outcome) in enumerate(lessons,1):
        key=f'{n}.{i}'
        details[key]={'teach':teach,'demo':demo,'outcome':outcome}
        short.append([name,minutes,teach])
    mods.append({'n':n,'title':title,'min':sum(x[1] for x in lessons),'objective':objective,'lessons':short,'exercise':task,'result':evidence})
    exercises[str(n)]={'task':task,'evidence':evidence}
module(1,'Fundamentos: entiende cada herramienta','Comprender qué hace cada herramienta y cómo HTML, CSS y JavaScript forman un único bloque para la página.',[
('Qué es Codex y cómo te ayuda a crear una web',10,
'Se explicará qué es un asistente de programación y cómo Codex transforma instrucciones en código. Se presentarán sus usos en el curso: crear una sección, cambiar su diseño, corregir un fallo y explicar un archivo. El alumno entenderá que debe definir el objetivo y revisar el resultado antes de publicarlo.',
'El docente mostrará una petición sencilla, el código generado y su resultado visual, señalando qué decidió la persona y qué produjo Codex.',
'Reconocer para qué utilizar Codex y cómo dirigir su trabajo con instrucciones concretas.'),
('Qué son Git y GitHub y por qué guardar versiones',10,
'Se explicará Git como sistema que registra cambios y GitHub como plataforma donde conservar el repositorio. Se introducirán los términos archivo, carpeta, repositorio, copia local y commit con un ejemplo. Se aclarará que el historial del código permite recuperar versiones, mientras que WordPress necesita además su propia copia de seguridad.',
'Se compararán dos versiones de una misma sección y se localizará el cambio en un historial de ejemplo.',
'Entender por qué se guarda cada avance y qué se podrá recuperar desde el repositorio.'),
('Hostinger, dominio, WordPress y Elementor: qué hace cada uno',10,
'Se distinguirán el hosting, que aloja el sitio, y el dominio, que permite localizarlo. Se explicará Hostinger como proveedor y hPanel como su panel de gestión; WordPress como sistema para administrar la web; y Elementor como editor que se instala dentro de WordPress. Se presentará la relación entre estas piezas.',
'El docente recorrerá un esquema del sistema y señalará en pantalla el panel del alojamiento, el de WordPress y el editor de Elementor.',
'Identificar dónde se administra el alojamiento, dónde se gestiona la web y dónde se coloca el código.'),
('HTML, CSS y JavaScript: tres funciones, un mismo código',10,
'Se explicará HTML como estructura y contenido, CSS como diseño y distribución, y JavaScript como comportamiento e interacción. Los tres se mostrarán dentro del mismo bloque: estilos en una etiqueta style, contenido HTML y lógica en una etiqueta script. Ese será el formato de trabajo que después se pegará en Elementor.',
'Se abrirá un único archivo con una tarjeta interactiva y se cambiarán su texto, su color y su comportamiento, identificando cada parte.',
'Comprender la función de cada lenguaje y reconocerlos integrados en un mismo archivo. Aquí se utiliza JavaScript.')],
'Identificar en el ejemplo dónde están HTML, CSS y JavaScript, y explicar el recorrido desde la petición a Codex hasta la publicación en WordPress alojado en Hostinger.',
'El alumno distingue las funciones de las herramientas y entiende que entregará un único bloque con contenido, estilos e interacciones.')
module(2,'Prepara WordPress en Hostinger','Crear un WordPress de práctica en Hostinger, reconocer su panel y preparar Elementor para recibir el código.',[
('Prepara el alojamiento y la dirección de práctica',10,
'Se enseñará a localizar un plan de alojamiento activo compatible con WordPress dentro de hPanel y el espacio donde se creará el sitio. Se explicará qué datos conviene tener listos y cómo elegir una dirección disponible para practicar. Se usará un dominio temporal cuando corresponda para evitar depender de la conexión de un dominio externo.',
'El docente accederá a hPanel, ubicará su alojamiento y mostrará las opciones de dirección para el sitio nuevo, sin completar compras durante la clase.',
'Reconocer los accesos necesarios y definir dónde se instalará el WordPress de práctica.'),
('Instala WordPress y entra a su administración',12,
'Se demostrará el asistente de instalación de WordPress en Hostinger: selección del sitio, datos de administración y dirección de práctica. Se elegirá una instalación inicial sencilla. Después se accederá al panel de WordPress y se explicará la diferencia entre visitar la página pública y entrar como administrador.',
'El docente completará la instalación en su cuenta de práctica, abrirá el panel de WordPress y comprobará que la dirección elegida carga.',
'Tener una instalación accesible y saber volver tanto al panel de administración como al sitio público.'),
('Conoce WordPress e instala Elementor',10,
'Se explicará para qué sirven las secciones Páginas, Medios, Apariencia y Plugins. Se distinguirá un tema, que define una base visual del sitio, de un plugin, que añade funciones. Se instalará y activará Elementor, mostrando dónde se abre el editor y cómo localizar el widget HTML que se utilizará después.',
'Se recorrerán las áreas esenciales de WordPress, se activará Elementor y se abrirá una página vacía para identificar sus controles.',
'Ubicar contenidos y recursos e identificar el editor y el widget donde se insertará el bloque completo.'),
('Crea la página de pruebas y prepara una copia',8,
'Se creará una página en borrador y se elegirá una plantilla que encaje con el diseño previsto. Se explicará cómo conservar o retirar cabecera y pie del tema para evitar duplicarlos. También se localizará la opción de copia de seguridad disponible en el entorno y qué debe conservarse antes de modificar el sitio.',
'El docente dejará la página de práctica lista, comprobará su vista previa y mostrará cómo identificar una copia recuperable del sitio.',
'Disponer del espacio de pruebas y saber qué revisar antes de insertar o sustituir código.')],
'Crear el sitio de práctica siguiendo la instalación guiada, entrar a WordPress, activar Elementor y dejar una página en borrador preparada para el proyecto.',
'El alumno accede al sitio y a su administración, encuentra el widget HTML y reconoce cómo disponer de una copia antes de hacer cambios.')
module(3,'Configura Codex y conéctalo con GitHub','Preparar el proyecto local, relacionarlo con un repositorio y guardar una primera versión del bloque de código.',[
('Accede a Codex y prueba tu carpeta de trabajo',8,
'Se mostrará cómo acceder a Codex desde la aplicación elegida para el curso, iniciar sesión y seleccionar una carpeta. Se explicará qué significa dar acceso a los archivos y revisar las acciones propuestas. El alumno hará una primera petición pequeña para verificar que el asistente trabaja en el lugar correcto.',
'El docente abrirá una carpeta de prueba, solicitará un archivo HTML sencillo y comprobará que existe en la ubicación seleccionada.',
'Iniciar una tarea en Codex y encontrar el archivo que genera.'),
('Crea el repositorio de GitHub y clónalo',10,
'Se creará un repositorio con un nombre reconocible y una visibilidad elegida conscientemente. Se iniciará sesión en GitHub Desktop y se clonará, obteniendo una copia local. Se explicará cómo distinguir la ubicación del computador de la dirección remota de GitHub y comprobar que ambas corresponden al mismo proyecto.',
'El docente creará y clonará el repositorio, y localizará su carpeta desde GitHub Desktop y desde el explorador de archivos.',
'Tener una carpeta local relacionada con un repositorio remoto donde guardar los avances.'),
('Abre el repositorio en Codex y define el formato',9,
'Se abrirá en Codex la carpeta clonada y se trasladará allí el archivo de práctica. Se creará un AGENTS.md breve con las reglas del proyecto: entregar un único bloque con HTML, CSS y JavaScript integrados, usar estilos propios y conservar las partes que funcionan. Se distinguirán el archivo de código, el brief y las imágenes de apoyo.',
'Se escribirá la regla de formato y se pedirá a Codex que revise el archivo sin separar los estilos ni la lógica en archivos adicionales.',
'Trabajar con Codex sobre el repositorio correcto y mantener el formato de código acordado.'),
('Revisa, guarda y sincroniza tu primera versión',8,
'Se practicará el ciclo cambiar, revisar, guardar un commit y sincronizar con GitHub. Se leerá una comparación sencilla para saber qué se añadió o eliminó y se escribirá un mensaje que describa el cambio. Se comprobará que guardar el archivo en el computador y enviarlo a GitHub son pasos diferentes.',
'Se cambiará un título con Codex, se revisará en GitHub Desktop y se confirmará la nueva versión desde GitHub.',
'Conservar un avance identificable y verificar que también está guardado en el repositorio remoto.')],
'Clonar el repositorio, abrirlo en Codex, definir la regla de código integrado y guardar un primer cambio en el archivo HTML mediante un commit sincronizado.',
'La copia local y GitHub contienen el cambio, y el archivo conserva su contenido, sus estilos y su lógica juntos.')
module(4,'Diseña y construye tu página en un solo código','Crear una landing de servicios con ayuda de Codex, integrando contenido, diseño e interacciones desde el primer bloque.',[
('Define el brief, el diseño y la instrucción para Codex',10,
'Se completará una ficha breve con público, servicio, objetivo, textos, secciones y acción principal. Se elegirá una referencia de colores y distribución. Con esa información se redactará un prompt que indique el resultado esperado, el comportamiento móvil y la entrega en un bloque para Elementor con HTML, CSS y JavaScript integrados.',
'El docente usará una plantilla para redactar el brief de un negocio de servicios y convertirlo en una petición concreta de construcción.',
'Pedir una página con contenido, referencia visual y formato de entrega definidos.'),
('Genera la cabecera y el bloque principal',15,
'Se construirá la presentación inicial de la página con título, descripción, imagen y botón. Se localizará el HTML del contenido y el CSS incluido en el mismo archivo, junto con el espacio para el JavaScript cuando se necesite. Se abrirá una vista previa y se solicitará un ajuste concreto de diseño.',
'El docente generará el primer bloque, revisará el resultado en el navegador y corregirá un espacio o tamaño sin rehacer toda la sección.',
'Obtener una primera sección revisada que ya utiliza el formato integrado del proyecto.'),
('Completa servicios, preguntas frecuentes y contacto',15,
'Se añadirán beneficios y servicios conservando los estilos establecidos. Después se incorporarán enlaces internos, preguntas desplegables y un botón de contacto. Se mostrará cómo el JavaScript del mismo bloque aporta comportamiento a los elementos HTML y cómo el CSS mantiene una apariencia coherente. El contacto será un enlace funcional.',
'El docente ampliará el bloque existente y comprobará los enlaces y la apertura de las preguntas con ratón y teclado.',
'Completar la landing manteniendo contenido, estilos e interacciones en un único código reutilizable.'),
('Ajusta móvil y revisa el bloque para Elementor',15,
'Se revisará el diseño en escritorio, tablet y móvil para corregir columnas, imágenes y desbordamientos. Se limitarán los estilos a un contenedor propio. Se distinguirá el bloque para Elementor del documento de vista previa, evitando copiar etiquetas generales como html, head o body dentro del widget. HTML, style y script permanecerán juntos.',
'Se corregirá un problema móvil y se guardará la versión final del bloque, comprobando su formato y las rutas de los recursos.',
'Tener una página adaptable y un único bloque claramente identificado para pegar en Elementor.')],
'Completar la landing del negocio de ejemplo, corregir su adaptación móvil y guardar el archivo del bloque listo para Elementor en el repositorio.',
'El código contiene HTML, CSS y JavaScript integrados; los enlaces y la interacción funcionan y la página se visualiza en tres tamaños de pantalla.')
module(5,'Integra y publica tu página en WordPress','Insertar el bloque completo en Elementor, ajustar sus recursos y validar la página publicada en el sitio de Hostinger.',[
('Pega el código completo en el widget HTML',12,
'Se retomará la página preparada en el módulo 2 y se insertará un widget HTML. Se copiará el bloque completo, incluidos el contenido, style y script. Se explicará cómo reconocer el inicio y el final del código y cómo comprobar que no falta ninguna parte al trasladarlo desde el archivo hacia Elementor.',
'El docente copiará el bloque completo, lo pegará en un único widget y abrirá la vista previa del borrador.',
'Trasladar el diseño y sus interacciones a Elementor en una sola inserción de código.'),
('Prepara imágenes, enlaces y recursos del sitio',13,
'Se subirán las imágenes del proyecto a la biblioteca de medios y se reemplazarán las rutas del computador por sus URLs de WordPress. Se revisarán enlaces internos y destino de contacto. Se explicará que unificar HTML, CSS y JavaScript no significa incrustar todos los archivos multimedia dentro del código.',
'El docente corregirá una imagen que depende de la carpeta local y probará nuevamente la navegación y el contacto desde la página.',
'Conseguir que los recursos carguen desde el sitio y que el bloque no dependa del computador de trabajo.'),
('Resuelve diferencias de diseño e integración',10,
'Se identificarán diferencias entre la vista previa y WordPress debidas a anchos, espacios del editor, estilos del tema o caché. Se enseñará a revisar una causa a la vez y pedir a Codex una corrección limitada al contenedor del bloque. Se probará de nuevo el conjunto tras sustituir el código.',
'El docente corregirá un ancho o espaciado que cambió dentro de Elementor y comparará el resultado en escritorio y móvil.',
'Ajustar el bloque dentro de WordPress sin extender sus cambios a otras partes del sitio.'),
('Publica y comprueba la experiencia del visitante',10,
'Se revisarán título, dirección de la página y visualización antes de publicar. Después se abrirá la URL real sin sesión de administración para comprobar recursos, navegación, interacción y contacto. Se recordará que la dirección de práctica debe estar disponible y que guardar una versión en GitHub no publica automáticamente el widget.',
'El docente publicará en el sitio de práctica, lo abrirá en una ventana privada y recorrerá sus acciones principales.',
'Publicar la landing y comprobar que funciona para un visitante desde su URL.')],
'Pegar el bloque en Elementor, corregir las rutas de recursos y publicar en el WordPress de práctica creado en Hostinger. Guardar capturas de escritorio y móvil.',
'La URL carga sin sesión, las imágenes se muestran y funcionan la navegación, el contacto y la interacción del bloque.')
module(6,'Corrige, actualiza y conserva tu trabajo','Aplicar una revisión básica y mantener el bloque publicado con apoyo de Codex y el historial de GitHub.',[
('Revisa calidad visual, accesibilidad y estructura básica',7,
'Se aplicará una lista breve de comprobación: lectura del contenido, orden de encabezados, descripción de imágenes, contraste y acceso con teclado. Se revisará también el tamaño de los recursos. El alumno identificará una mejora concreta que pueda resolverse en el bloque sin cambiar el diseño general del sitio.',
'El docente detectará y corregirá una incidencia, como una imagen sin descripción o un título con una jerarquía inadecuada.',
'Revisar la calidad básica de la página y documentar una corrección comprobable.'),
('Describe un fallo y corrígelo con Codex',7,
'Se enseñará a comunicar qué debería pasar, qué pasa realmente y cómo reproducir el problema. Se utilizará una captura o un mensaje de error cuando aporte información. Se pedirá una corrección puntual que conserve el bloque integrado y se revisará el cambio antes de llevarlo otra vez a WordPress.',
'El docente resolverá un enlace o una interacción defectuosa y repetirá los pasos que antes provocaban el fallo.',
'Pedir ayuda con evidencia y verificar que la solución funciona.'),
('Guarda una mejora y recupera el bloque anterior',6,
'Se repasará el ciclo de edición local, vista previa, commit, sincronización y actualización del widget. Se mostrará cómo recuperar el contenido de una versión anterior y guardarlo como un nuevo cambio. Se aclarará que recuperar el archivo en GitHub no sustituye por sí solo el código que está publicado en Elementor.',
'El docente guardará una mejora sencilla y recuperará el bloque anterior, comprobando la versión del archivo y la página.',
'Actualizar o recuperar el bloque sin perder la trazabilidad del proyecto.'),
('Entrega tu proyecto y repite el proceso',5,
'Se organizará la entrega con URL, bloque final, historial y README con las instrucciones de actualización. Se explicará cómo iniciar otra página a partir del mismo procedimiento cambiando brief, contenido e identidad visual. Se revisará que no queden enlaces ni datos de ejemplo ajenos al nuevo negocio.',
'El docente recorrerá la entrega e identificará qué archivo se copia en Elementor y cómo localizar su versión más reciente.',
'Presentar un proyecto comprensible y repetir el proceso de creación con una nueva página.')],
'Revisar la página, resolver una incidencia y conservar una versión final del bloque. Entregar la URL, el repositorio y una guía breve de actualización y recuperación.',
'El archivo final coincide con el bloque publicado y otra persona puede entender cómo se construyó y cómo se actualiza.')
assert len(mods)==6 and len(details)==24
assert [m['min'] for m in mods]==[40,40,35,55,45,25]
assert sum(m['min'] for m in mods)==240
(work/'programa-fundamentos.json').write_text(json.dumps(mods,ensure_ascii=False,indent=2))
(work/'lecciones-ampliadas.json').write_text(json.dumps({'lessons':details,'exercises':exercises},ensure_ascii=False,indent=2))
p=root/'tmp/crear-propuesta-daxus-codex.py'
s=p.read_text()
shutil.copy2(p,work/'crear-propuesta-antes-fundamentos.py')
a=s.index('mods=['); b=s.index('assert sum(',a)
s=s[:a]+"mods=json.loads((root/'tmp/pdfs/daxus-codex/programa-fundamentos.json').read_text())\n"+s[b:]
s=s.replace('De tu idea a una landing page publicada con Elementor, con el código organizado y un proceso para seguir mejorándola.', 'Desde los fundamentos y WordPress en Hostinger hasta una landing publicada con Elementor, con HTML, CSS y JavaScript en un mismo código.')
s=s.replace('Aprender a dirigir a Codex para crear y mejorar una página de servicios en HTML, CSS y JavaScript, guardar sus versiones en GitHub e integrarla en WordPress mediante Elementor.', 'Comprender las herramientas, preparar WordPress en Hostinger y crear con Codex una página cuyo HTML, CSS y JavaScript se integren en un único bloque, guardado en GitHub y publicado con Elementor.')
s=s.replace('Amplía la oferta visible en las capturas con un recorrido aplicado a Codex, repositorios y publicación en WordPress. La ubicación final queda a criterio de Daxus.', 'Ruta desde fundamentos hasta publicación: Hostinger, WordPress, Codex y GitHub, con un bloque de código integrado. La ubicación final queda a criterio de Daxus.')
a=s.index("page('Perfil y resultado'"); b=s.index('def render_mod(m):',a)
s=s[:a]+'''page('Perfil y resultado','Primero entender; después configurar y construir.', \'\'\'
<div class="grid"><div class="card"><h3>¿Para quién es?</h3><p>Freelancers, emprendedores y profesionales que quieren crear una página de servicios con IA. Se empieza explicando las herramientas y su relación.</p></div><div class="card"><h3>Nivel de entrada</h3><p>Principiante. Manejo básico del computador, archivos y navegador. No se requiere experiencia previa programando ni tener WordPress instalado.</p></div></div>
<h3 class="section">Al finalizar, el alumno podrá</h3>
<ol class="numberlist"><li>Explicar qué hacen Codex, GitHub, Hostinger, WordPress y Elementor dentro del proyecto.</li><li>Crear un WordPress de práctica en Hostinger y preparar una página con Elementor.</li><li>Dirigir a Codex para crear un bloque que reúna HTML, CSS y JavaScript en el mismo archivo.</li><li>Guardar versiones en GitHub, pegar el bloque en Elementor y comprobar la página publicada.</li><li>Corregir, actualizar y recuperar el código mediante un proceso sencillo y documentado.</li></ol>
<h3 class="section">Qué necesita el alumno antes de comenzar</h3>
<ul class="bullets small"><li>Computador con internet, navegador actualizado y acceso a Codex mediante una aplicación compatible.</li><li>Cuenta de GitHub y GitHub Desktop instalado. Se enseñan el repositorio, la conexión de la carpeta y el guardado de versiones.</li><li>Acceso a una cuenta de Hostinger con alojamiento activo compatible con WordPress. La instalación de WordPress y la preparación de Elementor se enseñan en el módulo 2.</li><li>Una dirección de práctica disponible; se puede utilizar la opción temporal del proveedor. Textos e imágenes del kit de ejemplo o del propio negocio.</li></ul>
<p class="tiny muted">Las cuentas, el alojamiento y las licencias que correspondan se preparan antes de grabar o practicar. Sus costos no están incluidos. No es obligatorio comprar un dominio para seguir la demostración en una dirección temporal.</p>
<div class="dark section"><p class="eyebrow">Un único bloque de código</p><p><strong>HTML:</strong> contenido y estructura. <strong>CSS:</strong> diseño dentro de &lt;style&gt;. <strong>JavaScript:</strong> interacciones dentro de &lt;script&gt;. Las tres partes se conservan juntas y se pegan en un mismo widget HTML de Elementor.</p></div>
<div class="box small"><strong>Proyecto:</strong> una landing de servicios con presentación, beneficios, preguntas frecuentes y contacto. GitHub guarda el código; WordPress lo publica en Hostinger. Las imágenes se alojan como recursos del sitio.</div>
\'\'\')
'''+s[b:]
s=s.replace('Estimación orientativa: 3 a 5 horas adicionales', 'Estimación orientativa: 4 a 6 horas adicionales')
s=s.replace('Explicación breve, demostración en pantalla, comprobación del resultado y consigna del ejercicio. Las herramientas se presentan cuando el proyecto las necesita.', 'Fundamentos al inicio, configuración guiada, construcción y publicación. Cada lección combina explicación y demostración. Las esperas de instalación se editan en el video.')
s=s.replace('archivo inicial, versiones por módulo y bloque final para comparar avances; README con pasos de uso y actualización.', 'archivo de código integrado, versiones por módulo y bloque final; README con pasos de instalación, uso y actualización.')
s=s.replace('lista para verificar enlaces, imágenes y móvil; pasos para actualizar el widget y recuperar una versión.', 'pasos para preparar WordPress en Hostinger, comprobar la página y actualizar o recuperar el bloque integrado.')
a=s.index("page('Alcance y preparación'"); b=s.index('assert len(pages)==10',a)
s=s[:a]+'''page('Alcance y preparación','Del fundamento a una página publicada.', \'\'\'
<h3>Decisiones que hacen viable el recorrido</h3>
<ul class="bullets small"><li><strong>Fundamentos antes de ejecutar:</strong> se explica cada herramienta y el papel de HTML, CSS y JavaScript. Después se prepara WordPress y se configura el trabajo de Codex con GitHub.</li><li><strong>Instalación guiada en Hostinger:</strong> cuenta y alojamiento activos antes de la clase. Se crea un sitio nuevo de práctica con una dirección disponible, usando la opción temporal cuando corresponda.</li><li><strong>Un mismo código durante todo el proyecto:</strong> HTML, CSS en style y JavaScript en script permanecen juntos en el bloque para Elementor. Los recursos multimedia se alojan en WordPress.</li><li><strong>Un proyecto acotado:</strong> una landing de servicios, con una interacción sencilla. Se revisa antes de publicar y se conserva el historial del bloque y una copia del sitio.</li></ul>
<h3 class="section">Límites de estas cuatro horas</h3>
<p class="small">Incluye la instalación básica de WordPress y Elementor. Quedan fuera las compras en directo, las migraciones, la resolución avanzada de DNS, la administración de servidores, el desarrollo de plugins, WooCommerce, formularios con backend y automatizaciones con GHL o n8n. La práctica y las esperas del alumno son adicionales.</p>
<h3 class="section">Preparación de la grabación</h3>
<ol class="numberlist small"><li>Confirmar con Daxus público, formato de video y acceso de los alumnos a las herramientas.</li><li>Disponer de una cuenta de Hostinger de demostración y un sitio vacío; preparar el ejemplo integrado y los recursos visuales.</li><li>Grabar una lección piloto y validar el ritmo. Registrar los 24 videos con versiones del código por módulo.</li><li>Comprobar la instalación, la publicación y la recuperación del bloque; revisar el kit y las instrucciones de entrega.</li></ol>
<hr class="rule">
<h3>Notas técnicas y fuentes de apoyo</h3>
<p class="small">El flujo de instalación se apoya en el asistente de WordPress de Hostinger, que contempla una dirección propia o temporal.<sup>1</sup> El widget HTML de Elementor admite HTML, CSS y scripts según los permisos del sitio.<sup>2</sup> Se comprobarán las interfaces utilizadas antes de grabar.</p>
<p class="small">El bloque integrado permite enseñar las funciones de los tres lenguajes sin repartir el código de la página en archivos CSS y JavaScript separados. Los textos del brief y la documentación del repositorio se conservan como apoyo.</p>
<ol class="refs"><li><a href="https://www.hostinger.com/support/6640339-how-to-add-a-wordpress-website-in-hostinger/">Hostinger · Crear un sitio WordPress</a></li><li><a href="https://elementor.com/help/html-widget/">Elementor · HTML widget</a></li><li><a href="https://learn.chatgpt.com/docs/quickstart">OpenAI · Guía de inicio</a></li><li><a href="https://learn.chatgpt.com/docs/features">OpenAI · Funciones de Codex</a></li></ol>
<p class="tiny muted">Referencia de estructura: «Propuesta de Curso para Daxus_Meli Navarro (1).pdf». Se conserva el esquema de objetivos, lecciones, tiempos y ejercicios. Programa de 240 minutos con fundamentos y configuración inicial incluidos. Referencias técnicas consultadas el 2 de octubre de 2026.</p>
\'\'\')
'''+s[b:]
p.write_text(s)
print(json.dumps({'modules':[{'title':m['title'],'minutes':m['min']} for m in mods],'lessons':len(details),'total':sum(m['min'] for m in mods)},ensure_ascii=False))
