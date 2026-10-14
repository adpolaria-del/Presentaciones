from pathlib import Path
from html import escape
import json,re
root=Path('/Users/josenicolassantiagomoreno/Documents/GitHub/Presentaciones')
mods=[]
def add(n,title,obj,lessons,task,check):
 mods.append({'n':n,'title':title,'objective':obj,'minutes':sum(l[1] for l in lessons),'lessons':[{'title':a,'minutes':b,'teach':c,'demo':d,'result':e} for a,b,c,d,e in lessons],'task':task,'check':check})
add(1,'Fundamentos, acceso y configuración inicial','Entender qué es GHL, acceder a la cuenta correcta y preparar el entorno de un negocio.',[
('Qué es GoHighLevel y qué puedes hacer con él',7,
'Se explicará qué es un CRM y cómo GHL reúne datos de contactos, conversaciones, oportunidades y automatizaciones. Se presentarán ejemplos de captación, atención y seguimiento. El alumno distinguirá el registro de una persona, el intercambio de mensajes y el proceso comercial que se puede automatizar.',
'Se recorrerá el caso de una persona que pide información, aparece en el CRM y queda asignada a un responsable.',
'Comprender la función de GHL y el resultado concreto que se construirá en el curso.'),
('Alta, acceso y puesta en marcha de la cuenta',8,
'Se aclarará que GHL se utiliza como servicio en la nube: la instalación del curso consiste en activar y configurar el acceso. Se mostrarán las rutas de alta o invitación y la diferencia entre vista de agencia y subcuenta de negocio. Se creará o seleccionará la subcuenta según los permisos disponibles.',
'El docente accederá con una cuenta de práctica, identificará el negocio correcto y mostrará dónde se cambia de subcuenta.',
'Entrar al espacio correcto sin confundir los ajustes de agencia con los del negocio.'),
('Credenciales, usuarios y permisos',8,
'Se distinguirán el usuario y la contraseña de GHL, las invitaciones al equipo y las autorizaciones de los canales conectados. Se revisarán recuperación de acceso, verificación en dos pasos y permisos por función. Las conexiones del proyecto se realizarán con autorizaciones nativas, sin copiar claves de API ni compartir contraseñas.',
'Se invitará a un usuario de prueba y se revisará su acceso a contactos, conversaciones y automatizaciones.',
'Preparar accesos individuales y reconocer cuándo una función no aparece por falta de permisos.'),
('Configura el negocio y reconoce el menú',7,
'Se revisarán nombre del negocio, zona horaria, datos de contacto y configuración del perfil. Después se ubicarán Dashboard, Contacts, Conversations, Opportunities, Calendars, Sites, Marketing, Automation y Settings, explicando qué problema resuelve cada sección y cuáles se usarán en el proyecto.',
'El docente completará los datos básicos y localizará las pantallas que acompañarán todo el recorrido.',
'Orientarse dentro de GHL y reconocer las áreas principales antes de construir automatizaciones.')],
'Entrar a una subcuenta de práctica, revisar sus datos y preparar un acceso de equipo con los permisos necesarios.',
'El alumno identifica el negocio, explica las áreas principales y puede abrir Contacts, Conversations y Automation.')
add(2,'Organiza el CRM y conoce sus herramientas','Preparar los datos y el seguimiento comercial que utilizará la automatización.',[
('Contactos, campos y etiquetas',10,
'Se enseñará a crear y revisar un contacto, distinguir los datos básicos de un campo personalizado y utilizar etiquetas para clasificar intereses u origen. Se explicará qué hacer cuando falta un teléfono o un correo y por qué no debe asumirse que dos perfiles sociales pertenecen a la misma persona.',
'Se creará un contacto de prueba, se añadirá una nota y se aplicarán etiquetas de interés y canal.',
'Guardar información útil y diferenciar identificación, clasificación y observaciones del contacto.'),
('Conversations: atender desde una sola bandeja',10,
'Se mostrará cómo localizar una conversación, reconocer su canal, leer el historial y responder desde GHL. Se revisarán responsable, estado y preferencias de contacto. El alumno aprenderá a verificar si un mensaje se envió y a distinguir una respuesta manual de una generada por una automatización.',
'El docente atenderá un mensaje de prueba y comprobará su recepción desde la cuenta que lo envió.',
'Gestionar una consulta y verificar el intercambio de mensajes en ambos sentidos.'),
('Oportunidades, etapas y responsables',8,
'Se explicará un pipeline como tablero de seguimiento comercial y una oportunidad como un posible negocio asociado a un contacto. Se prepararán tres etapas sencillas: Nuevo interés, En atención y Cerrado. Se revisarán asignación y tareas para que una respuesta automática termine en una acción útil del equipo.',
'Se creará una oportunidad de ejemplo, se moverá de etapa y se asignará una tarea de contacto.',
'Organizar las consultas recibidas sin confundir un contacto con una oportunidad comercial.'),
('Formularios, calendarios, sitios y marketing',7,
'Se hará un recorrido introductorio por formularios para captar datos, calendarios para reservas, sitios y funnels para presentar ofertas, Social Planner para contenido y reportes para seguimiento. Se explicarán usos posibles de correo y pagos mediante sus conexiones. El propósito será elegir herramientas, sin desarrollar una web ni un sistema de cobros.',
'El docente abrirá ejemplos preparados de formulario, calendario y publicación para relacionarlos con un caso de negocio.',
'Saber qué más puede hacerse en GHL y dónde continuar después del proyecto de mensajería.')],
'Preparar un contacto de prueba, las etiquetas del proyecto, el pipeline y un responsable de atención.',
'Los datos son comprensibles, el contacto tiene una clasificación y existe una etapa donde registrar el interés.')
add(3,'Conecta redes sociales y WhatsApp','Autorizar los canales necesarios y verificar que la mensajería funciona antes de automatizar.',[
('Conecta Facebook e Instagram para mensajes',12,
'Se identificarán la página de Facebook, la cuenta profesional de Instagram asociada y el acceso de Meta con permisos suficientes. Se realizará la conexión desde Integrations y se revisará la autorización de mensajes. Se comprobará la página seleccionada y el acceso de las herramientas conectadas al canal de Instagram.',
'Se completará la conexión en una cuenta preparada y se enviará un mensaje desde un perfil distinto para comprobarlo en Conversations.',
'Verificar mensajes entrantes y respuestas de prueba en los canales sociales conectados.'),
('Social Planner y el mapa de integraciones',10,
'Se distinguirá conectar un canal para publicar contenido de conectarlo para gestionar conversaciones. En Social Planner se enseñará a preparar un borrador y programar una publicación. Después se ubicarán otras conexiones, como calendario y correo, para entender qué credenciales requieren y qué función habilitan.',
'Se preparará una publicación de prueba con la invitación a escribir INFO por mensaje privado y se comprobará el canal de publicación.',
'Diferenciar contenido programado y mensajes automatizados, y localizar las conexiones nativas.'),
('Activa y conecta WhatsApp en la subcuenta',15,
'Se explicarán la habilitación de WhatsApp en GHL, la cuenta de negocio de Meta y el número que enviará y recibirá mensajes. Se mostrará el asistente de conexión usando un número de práctica. Si ya se utiliza WhatsApp Business, se explicará la opción de coexistencia cuando sea elegible, sin prometer compatibilidad universal.',
'El docente mostrará la autorización y los pasos de verificación aplicables a su número, y comprobará un intercambio desde Conversations.',
'Identificar los requisitos y comprobar que WhatsApp recibe y envía mensajes desde GHL.'),
('Ventanas de respuesta, plantillas y preferencias',13,
'Se explicará la ventana de atención de WhatsApp de 24 horas desde el último mensaje del usuario y cuándo se necesita una plantilla aprobada. Se mostrará cómo preparar una plantilla y consultar su estado. Se distinguirá responder una consulta de contar con autorización para futuras campañas, respetando bajas y restricciones de contacto.',
'Se comparará un mensaje de respuesta con una plantilla preparada y se localizarán sus estados y las preferencias del contacto.',
'Elegir el tipo de mensaje adecuado y reconocer por qué un envío puede no estar permitido.')],
'Conectar y probar los canales disponibles, identificar su número remitente y documentar qué permisos o activaciones faltan.',
'Hay evidencia de entrada y salida por canal. Una conexión pendiente se identifica como tal y no se presenta como funcional.')
add(4,'Fundamentos de automatización en GHL','Entender el constructor visual y definir cuándo debe responder el sistema y cuándo debe detenerse.',[
('Disparadores, filtros, acciones y condiciones',8,
'Se explicará un workflow como una secuencia de pasos. El disparador define qué lo inicia; un filtro limita los casos; una acción ejecuta una tarea; y una condición decide el camino. Se recorrerán ejemplos de mensaje recibido, etiqueta aplicada, aviso interno y comprobación de estado.',
'El docente dibujará el recorrido de una consulta y lo relacionará con los bloques visibles del constructor de GHL.',
'Leer una automatización sencilla y explicar por qué se ejecuta cada paso.'),
('Define la entrada por canal y palabra clave',9,
'Se utilizará Customer Replied para reconocer mensajes entrantes y se filtrará por canal y coincidencia de texto. El proyecto usará INFO como solicitud explícita en redes. Se mostrará por qué filtrar evita responder a cualquier mensaje y cómo dejar otros textos disponibles para la atención manual.',
'Se preparará un disparador en borrador y se contrastarán un mensaje que cumple la condición y otro que no.',
'Precisar quién entra en cada flujo y qué mensajes quedan fuera del recorrido automático.'),
('Prepara respuestas, etiquetas y avisos internos',10,
'Se redactará una respuesta breve con información útil y una siguiente acción clara. Se explicará el uso de etiquetas, asignación y notificaciones para el equipo. Se mostrará cómo revisar los datos antes de personalizar un mensaje, para no enviar saludos vacíos o información de otro contacto.',
'El docente configurará bloques de respuesta y de organización interna en un borrador, revisando sus destinatarios.',
'Distinguir las acciones dirigidas al cliente de las que sirven para organizar la atención del equipo.'),
('Reentrada, exclusiones y publicación',8,
'Se revisará si un contacto puede volver a entrar, cómo excluir los casos ya atendidos y cómo detener un flujo. Para esta demostración se limitará la entrada repetida por contacto en cada workflow. Se enseñará a comprobar etiquetas de control, restricciones de contacto y diferencias entre guardar un borrador y publicarlo.',
'Se revisará la configuración del borrador y se añadirá una salida para contactos ya atendidos o que no deben recibir el mensaje.',
'Preparar un flujo con límites claros y reducir respuestas repetidas durante la prueba.')],
'Definir en un borrador el evento de entrada, los filtros, el mensaje, las acciones internas y las condiciones de salida.',
'El alumno puede explicar qué dispara el flujo, qué lo detiene y por qué no debe responder a cualquier mensaje.')
add(5,'Proyecto: de redes sociales a WhatsApp','Construir una automatización de atención con tres workflows breves, todos dentro de GHL.',[
('Instagram: responde INFO y ofrece continuar',15,
'Se creará el workflow de Instagram con entrada por mensaje privado INFO. Se revisarán exclusiones, se añadirá una etiqueta de control y se enviará la respuesta mediante la acción del canal. El mensaje ofrecerá un enlace al WhatsApp del negocio con el texto INFO_IG preparado, sin iniciar por sí mismo una conversación allí.',
'El docente configurará la respuesta a un DM y verificará que el enlace abre el chat correcto con el texto previsto.',
'Tener un flujo de Instagram que responda a una solicitud concreta y permita continuar voluntariamente en WhatsApp.'),
('Facebook: adapta y comprueba el mismo recorrido',15,
'Se reproducirá la lógica en un workflow de Facebook Messenger, ajustando disparador, acción, etiqueta y texto del enlace a INFO_FB. Se explicará por qué copiar un flujo exige revisar el canal y cada destinatario. La automatización final tendrá una entrada independiente por red para facilitar su comprensión y revisión.',
'Se enviará INFO desde un perfil de prueba de Facebook y se revisará que la respuesta proviene de la página correcta.',
'Contar con la misma experiencia de atención para Facebook, sin reutilizar por error acciones de Instagram.'),
('WhatsApp: responde cuando la persona escribe',15,
'Se creará el workflow de WhatsApp con entradas por coincidencia exacta de INFO, INFO_IG o INFO_FB. Se comprobará la ventana de atención y se responderá con información breve si está abierta. Si está cerrada, el proyecto generará un aviso interno y finalizará, sin enviar texto libre. Se explicará qué cambia al usar una plantilla.',
'El usuario de prueba abrirá el enlace, enviará el texto y recibirá la respuesta desde el número conectado.',
'Completar el paso a WhatsApp a partir de un mensaje real del usuario, no solo de un clic.'),
('Organiza el interés y entrega la atención al equipo',15,
'Se añadirá la clasificación del origen según el texto recibido, la asignación del contacto y un aviso interno. En la ruta de WhatsApp se registrará una oportunidad sin repetirla si ya existe para ese contacto y pipeline. Se revisará el caso de identidades separadas entre redes y teléfono antes de unir registros.',
'El docente comprobará el contacto, el origen, la oportunidad y la notificación, y continuará la consulta manualmente desde Conversations.',
'Cerrar la automatización con una consulta organizada y un responsable que pueda atenderla.')],
'Completar los tres workflows del proyecto y recorrer Instagram o Facebook, enlace a WhatsApp, mensaje enviado y recepción por el responsable.',
'Cada canal usa su entrada correcta; la respuesta de WhatsApp requiere un mensaje real y el equipo recibe la consulta organizada.')
add(6,'Prueba, publica y mantén la automatización','Demostrar el funcionamiento y dejar un procedimiento sencillo de revisión y mantenimiento.',[
('Prueba el recorrido completo con cuentas reales de ensayo',10,
'Se preparará una matriz de pruebas: INFO por cada red, mensaje sin coincidencia, enlace abierto sin envío, mensaje enviado por WhatsApp y segundo intento del mismo contacto. Se comparará el resultado esperado con Conversations y el historial de ejecución. Las pruebas usarán perfiles y teléfonos de ensayo distintos del negocio.',
'El docente ejecutará el recorrido y registrará qué mensaje se recibió y qué acciones internas quedaron realizadas.',
'Demostrar el funcionamiento con evidencia y detectar pasos que solo parecen configurados.'),
('Diagnostica conexiones y envíos fallidos',8,
'Se enseñará a leer el historial para localizar el punto donde no se cumplió una condición o falló una acción. Se revisarán conexión, permisos, canal, remitente y ventana de atención antes de modificar el flujo. Se evitará reenviar todo automáticamente si eso puede duplicar mensajes o tareas ya completadas.',
'El docente analizará una incidencia controlada y repetirá únicamente la comprobación necesaria para validar su corrección.',
'Distinguir un error de conexión, un filtro no cumplido y un problema de envío.'),
('Publica y define una rutina de revisión',7,
'Se revisarán nombres, entradas, exclusiones y contactos de prueba antes de publicar. Se enseñará a activar o pausar los workflows y a observar sus primeras ejecuciones. Se definirá una revisión sencilla de mensajes recibidos, respuestas realizadas y consultas asignadas para comprobar la utilidad del sistema.',
'El docente activará los flujos de práctica, confirmará su estado y mostrará cómo detenerlos si detecta un comportamiento incorrecto.',
'Poner en marcha el proyecto con una rutina básica de supervisión.'),
('Documenta y entrega tu proyecto',5,
'Se preparará una guía con los tres workflows, sus condiciones, etiquetas, responsable y forma de pausar o volver a probar. Se registrarán también los canales conectados y las activaciones pendientes. La entrega contendrá evidencias del recorrido y nunca contraseñas, códigos de verificación ni claves de acceso.',
'El docente recorrerá una ficha de entrega y señalará dónde actualizar mensajes o cambiar al responsable.',
'Entregar una automatización que otra persona pueda comprender, revisar y mantener.')],
'Completar la matriz de pruebas, corregir incidencias y entregar los workflows con su guía operativa.',
'Hay pruebas positivas y negativas, control de reentrada, evidencia de respuesta y un procedimiento para pausar el sistema.')
assert [m['minutes'] for m in mods]==[30,35,50,35,60,30]
assert sum(m['minutes'] for m in mods)==240
assert sum(len(m['lessons']) for m in mods)==24
source=(root/'propuesta-curso-daxus-codex-wordpress.html').read_text()
css=re.search(r'<style>(.*?)</style>',source,re.S).group(1)
css+='''
.acceptance{table-layout:fixed;font-size:9pt}.acceptance td:first-child,.acceptance th:first-child{width:31%;font-size:9pt}.acceptance td:last-child,.acceptance th:last-child{width:69%;white-space:normal;text-align:left}.route-step{display:grid;grid-template-columns:9mm 1fr;gap:3mm;padding:3mm 0;border-bottom:1px solid #dce4dd}.route-step .stepnum{font-weight:700;color:#117465}.route-step p{margin:0;font-size:10pt}.source-list{font-size:8.5pt;line-height:1.4}.source-list li{margin-bottom:2.5mm}.source-list p{margin:1mm 0 0;color:#60716c}.channel-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}.channel-grid .card{padding:3mm}.channel-grid h3{font-size:11pt}.channel-grid p{font-size:9pt}.module-page .module h2{font-size:17pt}.ghl-note{font-size:8.5pt;color:#60716c}@media screen and (max-width:820px){.channel-grid{grid-template-columns:1fr}}
'''
pages=[]
def page(kicker,title,body,cls=''):
 i=len(pages)+1
 h=f'<p class="eyebrow">{kicker}</p><h2>{title}</h2>' if title else ''
 pages.append(f'<section class="page {cls}"><div class="top"><span class="brand">Propuesta de curso / Daxus</span><span>GoHighLevel · Desde cero</span></div><main>{h}{body}</main><footer class="foot"><span>Propuesta académica · Octubre 2026</span><span>{i:02d} / 11</span></footer></section>')
rows=''.join(f'<tr><td>{m["n"]:02d}</td><td>{m["title"]}</td><td>{m["minutes"]} min</td></tr>' for m in mods)
page('','',f'''
<p class="eyebrow">Título propuesto del curso</p><h1>GoHighLevel desde cero:<br>automatiza redes<br>sociales y WhatsApp</h1>
<p class="lead">Configura tu CRM, conecta tus canales y crea una automatización sencilla para responder consultas y organizar su atención.</p>
<div class="metrics"><div class="metric"><strong>4 h</strong><span>duración propuesta</span></div><div class="metric"><strong>6</strong><span>módulos progresivos</span></div><div class="metric"><strong>24</strong><span>lecciones de 5 a 15 min</span></div><div class="metric"><strong>1</strong><span>proyecto en GHL</span></div></div>
<div class="dark"><p class="eyebrow">Objetivo general</p><p>Aprender a preparar una cuenta de GoHighLevel, organizar contactos, conectar Facebook, Instagram y WhatsApp, y construir una automatización que responda solicitudes de información y las entregue a un responsable.</p></div>
<h3 class="section">Estructura propuesta</h3><table class="summary"><thead><tr><th>N.º</th><th>Módulo</th><th>Duración</th></tr></thead><tbody>{rows}</tbody><tfoot><tr><td></td><td>Total de contenido grabado</td><td>240 min</td></tr></tfoot></table>
<p class="small muted">Se propone mantener el formato de 4 horas de la serie. El tiempo incluye explicación y demostración; la práctica, las activaciones de servicios y las revisiones de Meta son adicionales.</p>
<div class="box"><strong>Herramienta central: GoHighLevel.</strong><br>El proyecto utiliza el CRM y sus workflows con las conexiones nativas de los canales. El alumno construye una solución de atención con respuestas predefinidas.</div>
''')
page('Perfil y condiciones de entrada','Empieza por la cuenta, los accesos y el CRM.','''
<div class="grid"><div class="card"><h3>¿Para quién es?</h3><p>Emprendedores, asistentes, equipos comerciales y profesionales de marketing que quieren ordenar consultas y automatizar respuestas iniciales.</p></div><div class="card"><h3>Nivel principiante</h3><p>No se requiere programar ni conocer GHL. Sí manejar un navegador y disponer de los accesos del negocio o de un entorno autorizado de práctica.</p></div></div>
<h3 class="section">Qué significa “instalar” en este curso</h3>
<p>Se enseña el alta o acceso por invitación, la selección o creación de la subcuenta y la configuración del negocio. GHL se utiliza en la nube; el recorrido principal se realiza desde el navegador.</p>
<h3 class="section">Accesos necesarios para el proyecto</h3>
<ul class="bullets small"><li><strong>GoHighLevel:</strong> cuenta o subcuenta de práctica con permisos para contactos, conversaciones, integraciones y workflows. La agencia debe habilitar las funciones necesarias.</li><li><strong>Facebook e Instagram:</strong> página de Facebook y cuenta profesional de Instagram vinculada, con acceso autorizado a los activos y a la mensajería para la ruta elegida.</li><li><strong>WhatsApp:</strong> servicio habilitado en la subcuenta, acceso al negocio de Meta y un número que pueda completar el proceso de conexión o coexistencia elegible.</li><li><strong>Pruebas:</strong> otra cuenta social y otro teléfono para representar al cliente, además de un usuario responsable que pueda recibir avisos en GHL.</li></ul>
<div class="box small"><strong>Credenciales que se explicarán:</strong> acceso a GHL, invitaciones al equipo, autorización de Meta, acceso al número y verificación. Las claves y códigos se introducen en los asistentes correspondientes; no se incluyen en material descargable ni se comparten con el grupo.</div>
<h3 class="section">Resultado del aprendizaje</h3>
<ol class="numberlist small"><li>Orientarse en GHL y configurar una subcuenta con sus usuarios.</li><li>Organizar contactos, conversaciones y oportunidades de atención.</li><li>Conectar y comprobar los canales antes de automatizarlos.</li><li>Construir, probar y mantener el proyecto de respuesta y derivación.</li></ol>
<p class="ghl-note">Los costos de GHL, WhatsApp y otros servicios activados no están incluidos. La disponibilidad depende de cuenta, permisos y canal. Si una aprobación sigue pendiente, el alumno podrá preparar borradores; la validación final exige probar los canales conectados.</p>
''')
page('Proyecto integrador','Una consulta, tres canales y un responsable.','''
<p class="lead">Caso propuesto: un negocio de servicios invita a escribir <strong>INFO</strong> para conocer su oferta. La persona decide si continúa por WhatsApp.</p>
<div class="channel-grid section"><div class="card"><h3>Workflow 1 · Instagram</h3><p>DM con INFO → comprobaciones → etiqueta → respuesta con enlace a WhatsApp.</p></div><div class="card"><h3>Workflow 2 · Facebook</h3><p>Mensaje con INFO → comprobaciones → etiqueta → respuesta con enlace a WhatsApp.</p></div><div class="card"><h3>Workflow 3 · WhatsApp</h3><p>Mensaje enviado por la persona → comprobar ventana → responder y organizar atención.</p></div></div>
<h3 class="section">Cómo se comportará la solución</h3>
<div class="route-step"><span class="stepnum">01</span><p><strong>Entrada por mensaje privado.</strong> La persona escribe INFO por Instagram o Facebook. Un filtro identifica el canal y la coincidencia esperada.</p></div>
<div class="route-step"><span class="stepnum">02</span><p><strong>Respuesta útil y siguiente paso.</strong> GHL entrega información breve y ofrece un enlace al WhatsApp conectado, con INFO_IG o INFO_FB como texto preparado.</p></div>
<div class="route-step"><span class="stepnum">03</span><p><strong>La persona continúa.</strong> Abre el enlace y envía el mensaje en WhatsApp. Abrir el chat sin enviarlo no activa la respuesta del tercer workflow.</p></div>
<div class="route-step"><span class="stepnum">04</span><p><strong>Respuesta en WhatsApp.</strong> Si el mensaje coincide y la ventana está abierta, GHL responde. Si no se puede enviar texto libre, se avisa internamente y termina esa ruta.</p></div>
<div class="route-step"><span class="stepnum">05</span><p><strong>Atención organizada.</strong> Se clasifica el origen, se asigna al responsable y se registra una oportunidad en WhatsApp, comprobando si ya existe para ese contacto.</p></div>
<div class="dark section"><p class="eyebrow">Ejemplo de respuesta social</p><p>“¡Hola! Aquí tienes la información inicial sobre nuestro servicio. Si quieres continuar por WhatsApp, abre este enlace y envía el mensaje que aparece preparado.”</p></div>
<p class="small section"><strong>Identidad del contacto:</strong> un perfil de Instagram o Facebook no aporta automáticamente su teléfono. GHL puede conservar registros separados al cambiar de canal. El curso enseñará a revisar coincidencias antes de unirlos; el origen se identifica por el texto enviado cuando se conserva.</p>
<p class="ghl-note">Es un proyecto con tres flujos breves para respetar las acciones de cada canal. Las automatizaciones por comentarios se explican como posibilidad posterior; el ejercicio evaluado se inicia por mensajes privados.</p>
''')
for m in mods:
 lessons=[]
 for i,l in enumerate(m['lessons'],1):
  lessons.append(f'<article class="detail-lesson"><div class="detail-heading"><span class="lesson-id">{m["n"]}.{i}</span><h3>{escape(l["title"])}</h3><span class="lesson-time">{l["minutes"]} min</span></div><p><b>Qué se enseñará.</b> {escape(l["teach"])}</p><p><b>Demostración en pantalla.</b> {escape(l["demo"])}</p><p class="learning"><b>Al terminar.</b> {escape(l["result"])}</p></article>')
 body=f'<p class="eyebrow">Programa detallado · Módulo {m["n"]} de 6</p><article class="module expanded-module"><div class="modulehead"><span class="num">{m["n"]:02d}</span><h2>{m["title"]}</h2><span class="duration">{m["minutes"]} min</span></div><p class="objective"><b>Objetivo:</b> {m["objective"]}</p>'+''.join(lessons)+f'<div class="exercise"><p><b>Ejercicio del módulo:</b> {m["task"]}</p><p><b>Cómo comprobar el aprendizaje:</b> {m["check"]}</p><p class="practice-note">Práctica independiente del alumno; adicional al tiempo de video.</p></div></article>'
 page('','',body,'module-page')
page('Materiales, pruebas y evaluación','Un proyecto que se pueda demostrar.','''
<div class="grid"><div class="card"><h3>240 minutos grabados</h3><p>Conceptos, demostraciones y consignas de práctica. Las esperas de activación y revisión se explican, pero no cuentan como tiempo de clase.</p></div><div class="card"><h3>Práctica sugerida</h3><p>Entre 4 y 6 horas adicionales para configurar, construir y probar. Los tiempos de proveedores pueden extender el calendario del alumno.</p></div></div>
<h3 class="section">Materiales propuestos a preparar por el docente</h3>
<ul class="bullets small"><li><strong>Guía de accesos y conexiones:</strong> qué cuenta o permiso se necesita en cada paso, sin recopilar contraseñas.</li><li><strong>Mapa de GHL y ficha del CRM:</strong> áreas principales, campos, etiquetas y etapas utilizadas.</li><li><strong>Recetas de los tres workflows:</strong> capturas, condiciones y orden de acciones para reproducirlos.</li><li><strong>Mensajes de ejemplo:</strong> respuestas sociales, respuesta de WhatsApp, aviso interno y ejemplo de plantilla.</li><li><strong>Matriz de pruebas y guía de operación:</strong> comprobación de cada canal, pausa y revisión de incidencias.</li></ul>
<h3 class="section">Pruebas mínimas de aceptación</h3>
<table class="summary acceptance"><thead><tr><th>Caso</th><th>Resultado esperado</th></tr></thead><tbody>
<tr><td>INFO en cada red</td><td>Respuesta en el canal correcto y enlace al número esperado.</td></tr>
<tr><td>Texto distinto</td><td>No activa la respuesta de la campaña; queda para atención manual.</td></tr>
<tr><td>Clic sin envío</td><td>No hay respuesta automática de WhatsApp.</td></tr>
<tr><td>Mensaje en WhatsApp</td><td>Respuesta permitida, clasificación y aviso al responsable.</td></tr>
<tr><td>Repetición / exclusión</td><td>No repite la bienvenida ni ignora las restricciones configuradas.</td></tr>
<tr><td>Ventana cerrada</td><td>No envía texto libre; genera aviso interno y finaliza la ruta.</td></tr>
</tbody></table>
<h3 class="section">Evaluación sugerida</h3>
<p class="small">Cuenta y accesos: <strong>15 %</strong> · organización del CRM: <strong>15 %</strong> · conexiones verificadas: <strong>25 %</strong> · funcionamiento y exclusiones: <strong>35 %</strong> · documentación: <strong>10 %</strong>.</p>
<div class="box small"><strong>Entrega:</strong> guía de los workflows y evidencias de entrada, respuesta y atención interna. Se propone 80/100 como referencia; los canales y el recorrido deben funcionar. Daxus definirá evaluación, soporte y certificación.</div>
''')
page('Alcance y respaldo técnico','Solo GHL, con sus conexiones nativas.','''
<h3>Alcance de estas cuatro horas</h3>
<p class="small">Se enseña la puesta en marcha, el CRM, las conexiones de mensajes y una automatización de atención. Formularios, sitios, calendarios, pagos y publicaciones se presentan para conocer sus posibilidades. No se desarrollan tiendas, campañas publicitarias, agentes de IA ni integraciones con código; el proyecto se construye en GHL.</p>
<h3 class="section">Condiciones para grabar y practicar</h3>
<ul class="bullets small"><li>Preparar una subcuenta de demostración, canales propios o autorizados y usuarios de prueba. Ocultar credenciales al grabar.</li><li>Comprobar que WhatsApp está habilitado y que el número puede completar el alta. La coexistencia depende de elegibilidad; revisar el caso antes de modificar un número utilizado por un negocio.</li><li>Disponer de conexiones funcionales y una plantilla de ejemplo previamente revisada para la demostración. No se promete una aprobación dentro de los 240 minutos.</li><li>El proyecto responde a mensajes entrantes. Cualquier campaña posterior necesita revisar permisos, preferencias del contacto, plantillas y reglas del canal.</li></ul>
<h3 class="section">Fuentes oficiales para preparar las clases</h3>
<p class="ghl-note">Se revisarán los nombres de menús y la disponibilidad al grabar. Las fuentes respaldan requisitos técnicos; los tiempos y la secuencia didáctica son una propuesta propia.</p>
<ol class="source-list">
<li><a href="https://help.gohighlevel.com/support/solutions/articles/155000002544">GHL · Usuarios y permisos de subcuenta</a><p>Base del acceso por función y visibilidad de datos.</p></li>
<li><a href="https://help.gohighlevel.com/support/solutions/articles/155000005068">GHL · Conectar Facebook e Instagram Messenger</a><p>Autorización, vinculación y pruebas de mensajes.</p></li>
<li><a href="https://help.gohighlevel.com/support/solutions/articles/155000005063-launchpad-setup-social-planner">GHL · Configurar Social Planner</a><p>Preparar y programar contenido social.</p></li>
<li><a href="https://help.gohighlevel.com/support/solutions/articles/155000001980">GHL · Configurar WhatsApp</a> · <a href="https://help.gohighlevel.com/support/solutions/articles/155000003417/">Coexistencia</a> · <a href="https://help.gohighlevel.com/support/solutions/articles/155000001624">WhatsApp en workflows</a><p>Conexión y respuesta por el canal de WhatsApp.</p></li>
<li><a href="https://help.gohighlevel.com/support/solutions/articles/155000002677">GHL · Customer Replied</a> · <a href="https://help.gohighlevel.com/support/solutions/articles/155000004662-action-instagram-interactive-messenger">Acción de Instagram</a> · <a href="https://help.gohighlevel.com/support/solutions/articles/155000004661">Acción de Facebook</a><p>Entradas, filtros y mensajes específicos de cada red.</p></li>
<li><a href="https://help.gohighlevel.com/support/solutions/articles/155000003533-workflow-action-whatsapp-customer-service-window-check">GHL · Comprobar ventana de atención</a> · <a href="https://help.gohighlevel.com/support/solutions/articles/155000000861-how-to-create-a-whatsapp-template-">Crear plantillas</a><p>Texto libre dentro de ventana y plantillas sujetas a aprobación.</p></li>
</ol>
<p class="tiny muted">Referencias consultadas el 2 de octubre de 2026. Esta propuesta no fija precios, cuotas de envío ni plazos de aprobación. El documento define el curso; los videos y materiales del alumno se producirán posteriormente.</p>
''')
assert len(pages)==11
html='<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Propuesta Daxus: GoHighLevel desde cero, configuración, CRM, integraciones y automatización de redes sociales y WhatsApp. 4 horas."><title>Propuesta Daxus | GHL desde cero</title><style>'+css+'</style></head><body>'+''.join(pages)+'</body></html>'
(root/'propuesta-curso-daxus-ghl.html').write_text(html)
(root/'tmp/pdfs/daxus-ghl/programa.json').write_text(json.dumps(mods,ensure_ascii=False,indent=2))
render=(root/'render-propuesta-daxus-codex.mjs').read_text().replace('propuesta-curso-daxus-codex-wordpress','propuesta-curso-daxus-ghl')
(root/'render-propuesta-daxus-ghl.mjs').write_text(render)
print(json.dumps({'modules':6,'lessons':24,'minutes':240,'pages':len(pages)}))
