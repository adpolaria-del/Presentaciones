from pathlib import Path
from html import escape as e
import json,shutil,re
R=Path.cwd(); O=R/'curso-ux-ui-guion-profesor-detallado'; O.mkdir(exist_ok=True)
old=R/'curso-ux-ui-paso-a-paso'
base=json.loads((old/'recursos/pasos.json').read_text())
extra=json.loads((R/'tmp/guion-profesor-ampliado.json').read_text())
assert [x['id'] for x in base]==[x['id'] for x in extra]
assert all(len(x['extras'])==5 for x in extra)
shutil.copytree(old/'recursos',O/'recursos',dirs_exist_ok=True)
shutil.copy2(old/'PANTALLA-PARA-GRABAR.html',O/'PANTALLA-PARA-GRABAR.html')
shutil.copy2(R/'output/pdf/curso-ux-ui-programa-estudiantes.pdf',O/'programa-estudiantes.pdf')
shutil.copy2(R/'tmp/guion-profesor-ampliado.json',O/'recursos/guion-ampliado.json')
P=[]
def page(k,t,b,id=None,cls=''):
 n=len(P)+1
 P.append(f'<section class="page {cls}" id="{id or "p"+str(n)}"><header><span>GUÍA DEL PROFESOR · GUION AMPLIADO</span><span>UX/UI PARA PÁGINAS WEB</span></header><main><p class="eyebrow">{k}</p><h1>{t}</h1>{b}</main><footer><span>Guía alineada con el programa del estudiante · Edición 07.10.2026</span><span>{n:02d} / 54</span></footer></section>')
def panel(title,text,cls='box'): return f'<div class="{cls}"><h3>{title}</h3><p>{text}</p></div>'
def speech(title,text): return panel(title,'«'+e(text)+'»','speech')
page("EMPIEZA POR ESTA GUÍA","Qué hacer en pantalla<br>y qué decir en cada momento.",
'<p class="lead">Un guion desarrollado para preparar y grabar las 24 clases del curso. Conserva los seis módulos, los ejercicios y las cuatro horas previstas en el programa del estudiante.</p>'
+panel("Tu ruta para empezar","Abre <strong>PANTALLA-PARA-GRABAR.html</strong> en el navegador. Mantén esta guía en otra ventana, fuera del área grabada. Ve a la clase 1.1 de esta guía y prepara la pantalla indicada. Ensaya una vez sus acciones antes de grabar.")
+'<h2>Cómo está organizada cada clase</h2><div class="flow"><b>Primera página</b><span>Preparación exacta, apertura literal y pasos 1 y 2. Incluye una comparación adicional para ensayar y cómo resolver un tropiezo.</span><b>Segunda página</b><span>Pasos 3, 4 y 5, ejercicio para el alumno, una respuesta de referencia y cierre literal.</span></div>'
+'<h2>Qué lees tú y qué dices en voz alta</h2><ul><li><strong>Prepara, Haz, Comprueba y Si te atoras:</strong> instrucciones para ti. No las leas al alumno.</li><li><strong>Di al abrir, Di y Di al cerrar:</strong> texto completo que puedes decir en voz alta.</li><li><strong>Pide este ejercicio:</strong> frase para que el alumno pause y practique.</li><li><strong>Después de la pausa:</strong> explicación de una posible respuesta. No significa que todas deban ser idénticas.</li></ul>'
+speech("Tu primera frase del curso","En este curso vamos a aprender a tomar decisiones de UX/UI con una página de ejemplo. Verás problemas, cambios y sus razones. Cuando aparezca un ejercicio, pausa el video y pruébalo. Al final presentarás tres mejoras explicando qué dificultad atiende cada una.")
+panel("Qué necesitas preparar","Computador, navegador, micrófono y esta carpeta completa. No necesitas crear un archivo de Figma ni programar para seguir las demostraciones. Para la clase 6.2 prepara un participante o identifica el ensayo como simulación.")
+'<p class="note">El guion es una base literal para ensayar. Puedes adaptar el tono conservando el significado, las acciones y el ejercicio. No necesitas memorizar todo el documento para empezar con una clase.</p>')
page("CONOCE LA PANTALLA","Página, boceto y pizarra: tres usos distintos.",
'<img class="screen" src="recursos/mapa-pantalla.png" alt="Pantalla de práctica del curso">'
+'<div class="tool"><h3>1. Página web: demostrar un recorrido</h3><p>Usa «Versión inicial» para mostrar problemas y «Versión mejorada» para mostrar una propuesta. Aquí funcionan los enlaces y el formulario simulado. «Escritorio» y «Móvil 390» cambian el ancho. «Reiniciar caso» permite repetir la demostración.</p></div>'
+'<div class="tool"><h3>2. Editar diseño: cambiar un boceto delante del alumno</h3><p>Selecciona palabras dentro de un texto y escribe para reemplazarlas. «Subir» y «Bajar» cambian el orden de las tarjetas. Los controles de tamaño y separación modifican su aspecto. El botón verde es editable: no envía nada. El taller no modifica la página preparada.</p></div>'
+'<div class="tool"><h3>3. Escribir un ejemplo: tu pizarra de trabajo</h3><p>Selecciona el número de clase y escribe después de sus etiquetas. Sirve para mostrar objetivos, preguntas y observaciones. No genera páginas ni envía tareas. En la guía lo llamaremos también «pizarra», manteniendo el nombre del botón real.</p></div>'
+speech("Di al usar la pizarra por primera vez","Aquí voy a escribir cómo estoy pensando el diseño. Lo que anote no cambia la página. Primero dejamos claro el objetivo o el problema; después vamos al ejemplo para relacionarlo con una decisión visible.")
+panel("Antes de cerrar o reiniciar","En la pizarra pulsa «Guardar lo que escribí». Captura el boceto si quieres conservar sus cambios. Reiniciar el taller elimina modificaciones. Al cerrar o recargar no debes contar con recuperar texto que no descargaste.")
+'<p class="small">Faro y sus condiciones son ficticios. El formulario no envía información real. Usa Ana y ana@example.com en las demostraciones. Mantén la carpeta «recursos» junto a los archivos HTML.</p>')
mods=[("Fundamentos de UX/UI",30,4),("Usuarios y organización del contenido",35,5),("Fundamentos visuales de UI",40,6),("Heurísticas aplicadas a una web",55,7),("Aplicación práctica a la página",40,8),("Prueba, mejora y presentación",40,9)]
rows=''.join(f'<tr><td>{i+1:02d}</td><td><strong>{m[0]}</strong><br>Clases {i+1}.1 a {i+1}.4 · {m[1]} min previstos</td><td>pp. {5+i*8}-{12+i*8}</td><td>p. {m[2]}</td></tr>' for i,m in enumerate(mods))
page("MISMO CURSO, DOS DOCUMENTOS","Cómo se alinea con el material del estudiante.",
'<p>Esta guía desarrolla exactamente las clases 1.1 a 6.4 del programa. El estudiante ve la demostración y practica; tú utilizas estas instrucciones para prepararla, explicarla y comentar el ejercicio.</p>'
+f'<table><thead><tr><th>Módulo</th><th>Contenido</th><th>Esta guía</th><th>Estudiante</th></tr></thead><tbody>{rows}</tbody></table>'
+'<h2>Heurísticas: el refuerzo solicitado</h2><p>La clase 4.1 comienza explicando qué es una heurística y cómo orienta una mejora. Las clases 4.1, 4.2 y 4.3 desarrollan las diez con problema, demostración y beneficio esperado. La 4.4 convierte lo encontrado en una ficha de trabajo.</p>'
+'<p>En el PDF del estudiante, las páginas 10 a 12 amplían esa explicación. Utilízalas como lectura de apoyo; en la grabación muestra la página y realiza las acciones descritas aquí.</p>'
+'<h2>Proyecto final</h2><p>Las clases construyen el objetivo, la estructura, los hallazgos y las mejoras. En 6.4 el estudiante presenta tres cambios en un video breve. El proyecto y su autoevaluación están en las páginas 13 y 14 del programa; aquí tienes orientación para explicarlos en la página 53.</p>'
+panel("Sobre las cuatro horas","Los tiempos de clase suman 240 minutos previstos de video. No son un cronómetro garantizado por leer el guion: incluyen explicación y demostraciones. Las pausas de práctica autónoma van aparte. Cronometra una toma piloto para ajustar profundidad y ritmo; no completes tiempo con silencios o repeticiones.")
+'<p class="note">La página 54 reúne dudas frecuentes y referencias. El programa del estudiante está incluido en esta carpeta como «programa-estudiantes.pdf».</p>')
page("ANTES DE PULSAR GRABAR","Prepara una clase y grábala por partes.",
'<ol class="record"><li><strong>Abre los dos materiales.</strong> Guía para ti y pantalla de práctica para el alumno. Coloca la guía fuera del área que vas a grabar; puede estar en otra pantalla, impresa o en una ventana que no captures.</li><li><strong>Ensaya la preparación.</strong> Sigue «Prepara antes de grabar». Deja la versión, pestaña y datos en el estado indicado. Así cada clase puede grabarse de forma independiente.</li><li><strong>Haz una prueba breve.</strong> Graba treinta segundos diciendo una apertura y realizando un clic. Reproduce el resultado: comprueba voz, tamaño del texto y que el cursor se vea.</li><li><strong>Graba la apertura y una acción.</strong> Haz el movimiento indicado, espera a que se vea el resultado y explica su significado con el texto «Di». Si hablas mientras se desplaza la página, hazlo sin correr.</li><li><strong>Continúa en fragmentos.</strong> Puedes detenerte para consultar el siguiente paso fuera de la toma y grabar otro fragmento. Al unirlos, conserva el orden de las acciones y el estado de la página.</li><li><strong>Pide el ejercicio.</strong> Lee la instrucción y pide pausar. No dejes varios minutos de silencio. A continuación graba el comentario de la respuesta y el cierre.</li><li><strong>Revisa y nombra.</strong> Comprueba que lo que dices coincide con lo que se ve. Guarda, por ejemplo, M01-L01-toma01.mov.</li></ol>'
+panel("Si grabas en Mac","Pulsa Mayúsculas + Comando + 5, selecciona la opción para grabar una parte de la pantalla y delimita la ventana de práctica. En Opciones elige el micrófono. Pulsa Grabar y detén desde el control de la barra de menús. La interfaz puede variar según la versión del sistema.")
+'<p class="small">Referencia: <a href="https://support.apple.com/es-es/102618">Apple: cómo grabar la pantalla del Mac</a>.</p>'
+'<h2>Cómo usar el guion sin sonar leído</h2><p>Ensaya el párrafo mirando el elemento al que se refiere. Puedes dividirlo en dos frases y señalar mientras explicas. Si hay una pregunta retórica al alumno, deja un instante para que mire, pero no inventes su respuesta.</p>'
+panel("Para la clase con participante","En 6.2 graba primero las instrucciones, después el intento y al final tu explicación. No leas comentarios de diseño mientras la persona intenta la tarea. Las frases dirigidas al participante se distinguen de las dirigidas al alumno."))
def stepblock(x,z,j):
 s=dict(x['steps'][j])
 if x['id']=='6.2' and j==0:
  s['action']='Di a la persona: «Estamos probando la página, no tus habilidades. Puedes detenerte cuando lo necesites». Lee la tarea del recuadro siguiente sin señalar botones. Entrega a la persona el ratón o trackpad.'
 actions=re.split(r'(?<!\d\.)(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])',s['action'])
 action='<ol class="actions">'+''.join('<li>'+e(t)+'</li>' for t in actions)+'</ol>'
 special=x['id']=='6.2' and j<4
 if special:
  spoken=f'<p class="label">AL PARTICIPANTE, SI CORRESPONDE</p><p class="spoken">«{e(s["say"])}»</p><p class="label">EXPLICA AL ALUMNO FUERA DEL INTENTO</p><p class="spoken">«{e(z["extras"][j])}»</p>'
 else:
  spoken=f'<p class="label">DI</p><p class="spoken">«{e(s["say"]+" "+z["extras"][j])}»</p>'
 return f'<article class="step"><div class="do"><h2>Paso {j+1} · Haz en pantalla</h2>{action}</div>{spoken}<p class="check"><strong>Comprueba:</strong> {e(s["see"])}</p></article>'
for x,z in zip(base,extra):
 mod=int(x['id'][0]); studentpage=mods[mod-1][2]
 reset=[]
 if 'página web' in x['where'].lower(): reset.append('En «1. Página web», pulsa «Reiniciar caso» y deja la vista en «Escritorio».')
 if 'editar diseño' in x['where'].lower(): reset.append('En «2. Editar diseño», pulsa «Reiniciar taller».')
 prep=' '.join(reset)+' '+x['prep']
 note='<p class="participant">En esta clase, las intervenciones al participante y las explicaciones al alumno se graban por separado. No leas tus comentarios de diseño durante su intento.</p>' if x['id']=='6.2' else ''
 b=f'<p class="meta">Tiempo objetivo: {x["minutes"]} min · Programa del estudiante: p. {studentpage} · Pantalla: {e(x["where"])}</p>'
 b+=panel("Prepara antes de grabar",e(prep),'prep')+speech("Di al abrir la clase",z['opening'])
 b+=stepblock(x,z,0)+stepblock(x,z,1)
 b+=panel("Comparación adicional para ensayar",e(z['extra']),'extra')
 b+=panel("Si te atoras",e(z['trouble']),'trouble')
 page('CLASE '+x['id']+' · PARTE A: PREPARAR Y EMPEZAR',e(x['title']),b,id='clase-'+x['id'].replace('.','-'),cls='lesson first')
 b=f'<p class="meta">Sigue desde el paso 2; no reinicies la pantalla.</p>'
 b+=''.join(stepblock(x,z,j) for j in range(2,5))
 task=x['task'].removeprefix('Dile: “').removesuffix('”.')
 if not task.startswith('Pausa'): task='Pausa el video. '+task
 b+=speech("Pide este ejercicio al alumno",task+'.')
 b+=speech("Después de la pausa, comenta una respuesta",z['answer'])
 b+=speech("Di al cerrar la clase",z['close'])
 page('CLASE '+x['id']+' · PARTE B: DEMOSTRAR Y CERRAR',"Continúa la clase "+x['id'],b,id='cierre-'+x['id'].replace('.','-'),cls='lesson second')
page("EXPLICAR LA ENTREGA FINAL","Qué pedirás y cómo comentarás el proyecto.",
speech("Presenta la entrega","Tu proyecto reúne las decisiones que has ido tomando. Explica quién visita la página y qué necesita; muestra su estructura, tres problemas y tres mejoras. Para cada mejora, enseña el antes y el después y di qué dificultad intentas resolver. Termina indicando qué comprobaste y qué sigue pendiente.")
+'<h2>Revisa el trabajo con estas preguntas</h2><table><thead><tr><th>Parte</th><th>Qué buscas</th><th>Cómo lo comentas</th></tr></thead><tbody>'
+'<tr><td>Objetivo</td><td>Necesidad y acción principal relacionadas.</td><td>«Entiendo qué quiere hacer la persona. Ahora explica cómo la página le ayuda».</td></tr>'
+'<tr><td>Estructura</td><td>Cinco secciones con una función.</td><td>«Esta sección necesita responder una pregunta distinta para justificar su lugar».</td></tr>'
+'<tr><td>Problemas</td><td>Ubicación, descripción y razón.</td><td>«Señala dónde ocurre y qué dificultad podría generar».</td></tr>'
+'<tr><td>Mejoras</td><td>Cambio concreto y beneficio esperado.</td><td>«Explica qué mejora para la tarea, además de lo que cambia visualmente».</td></tr>'
+'<tr><td>Prueba</td><td>Hechos separados de interpretación.</td><td>«Distingue lo que observaste de la causa que supones».</td></tr>'
+'<tr><td>Presentación</td><td>Tres comparaciones comprensibles.</td><td>«Conserva problema, cambio y razón; elimina repeticiones».</td></tr></tbody></table>'
+speech("Explica cómo guardar el avance","Guarda tus notas y capturas en una carpeta. En la pizarra usa Guardar lo que escribí antes de cerrar. Si cambiaste el taller, conserva una captura antes de reiniciarlo. Eso te permitirá mostrar tus decisiones aunque después vuelvas a practicar desde el inicio.")
+panel("Cómo evitar una promesa que el curso no hizo","La entrega es una propuesta de diseño y revisión. No exige publicar una web ni construir una integración real. Los criterios sirven para autoevaluación; el canal de entrega, una calificación o una devolución individual se acordarán con Daxus.")
+'<p class="note">Si comentas un ejemplo durante la grabación, identifícalo como ejemplo. No presentes una respuesta inventada como trabajo recibido de un estudiante.</p>')
page("APOYO PARA EL PROFESOR","Respuestas breves cuando aparezcan dudas.",
speech("«¿Qué es una heurística, dicho fácil?»","Es una idea general que uso para revisar un diseño. Por ejemplo, me pregunto si la persona puede saber qué ocurre después de pulsar. Si no hay una respuesta clara, tengo una dificultad que revisar y un cambio que proponer.")
+speech("«¿Aplicar las diez hace perfecto mi diseño?»","Me ayuda a detectar posibles problemas y a razonar mis decisiones. Después necesito comprobar cómo lo entienden las personas y revisar otros aspectos, como contenido y accesibilidad. No puedo garantizar un resultado solo por completar una lista.")
+speech("«¿Qué escribo en Escribir un ejemplo?»","Selecciona el número de la clase y completa sus etiquetas. Es una pizarra para mostrar tus ideas. Si dice La persona necesita, escribe esa necesidad. Si dice Problema, describe la dificultad que encontraste. Nada de eso modifica automáticamente la web.")
+speech("«¿Por qué mi edición no aparece en la página?»","Porque el taller es un boceto editable y Página web es una demostración preparada. Usamos el primero para proponer decisiones y la segunda para observar una aplicación con interacciones.")
+speech("«¿El contraste comprueba toda la accesibilidad?»","No. Aquí mide la relación entre texto y fondo sólidos. También tendríamos que revisar estructura, controles, teclado y otras necesidades. En el curso comprobamos algunas partes y dejamos claro su alcance.")
+'<h2>Referencias para ampliar tu preparación</h2><ul class="refs"><li><a href="https://www.nngroup.com/articles/ten-usability-heuristics/">Nielsen Norman Group: diez heurísticas de usabilidad</a>. Nombres y principios generales; los ejemplos de Faro son didácticos.</li><li><a href="https://www.nngroup.com/articles/usability-testing-101/">Nielsen Norman Group: introducción a pruebas de usabilidad</a>. Preparación de tareas y observación.</li><li><a href="https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html">W3C: contraste mínimo, WCAG 1.4.3</a>. AA: 4.5:1 en texto normal y 3:1 en texto grande, según las definiciones y excepciones del criterio.</li><li><a href="https://support.apple.com/es-es/102618">Apple: grabación de pantalla en Mac</a>.</li></ul>'
+'<p class="note">Las condiciones de Faro son ficticias. El programa del estudiante y la guía usan el mismo ejemplo, los mismos nombres de pestañas y las mismas 24 prácticas. Esta edición amplía la explicación del profesor; conserva el recorrido del curso.</p>')
assert len(P)==54
css="""@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;background:#e8ede8;color:#193d35;font:10.2pt/1.37 Arial,Helvetica,sans-serif}.page{width:210mm;height:297mm;padding:14mm 14mm 15mm;background:#fffefa;position:relative;margin:8mm auto;page-break-after:always;scroll-margin-top:75px}.page:last-child{page-break-after:auto}header{display:flex;justify-content:space-between;color:#60816e;font-size:7pt;letter-spacing:.5px;border-bottom:1px solid #c6d7c8;padding-bottom:3.5mm}main{padding-top:5mm}footer{position:absolute;bottom:9mm;left:14mm;right:14mm;display:flex;justify-content:space-between;border-top:1px solid #c6d7c8;padding-top:2.5mm;font-size:6.8pt;color:#6d8274}.eyebrow{font-size:7.8pt;letter-spacing:.8px;color:#2f8060;font-weight:700;margin:0 0 2mm}h1{font-size:23pt;line-height:1.12;letter-spacing:-.4px;margin:0 0 4mm}h2{font-size:12.5pt;margin:4mm 0 2mm}h3{font-size:10.5pt;margin:0 0 1.6mm}p{margin:0 0 2.8mm}.lead{font-size:13pt;line-height:1.45;color:#5c7a66}.box,.prep,.extra,.trouble{padding:3mm 4mm;margin:3mm 0;background:#eaf2e8;border-left:3px solid #478363}.box p,.prep p,.extra p,.trouble p{margin:0}.speech{border-left:2px solid #b9cdbb;padding:2mm 0 2mm 3mm;margin:3mm 0}.speech p{margin:0}.flow{display:grid;grid-template-columns:35mm 1fr;gap:3mm;padding:4mm;background:#eef4ed;margin:4mm 0}.small,.note{font-size:9pt}.note{color:#6b7f71}.screen{width:100%;border:1px solid #cbdacc;border-radius:2mm;margin:1mm 0 4mm}.tool{margin:3mm 0}.tool p{font-size:10pt}.meta{font-size:8.4pt;color:#5b7464;margin:0 0 3mm}table{border-collapse:collapse;width:100%;font-size:9.4pt}th,td{padding:3mm 2mm;text-align:left;vertical-align:top;border-bottom:1px solid #d5dfd4}th{background:#193d35;color:white;font-size:8.7pt}ul{padding-left:5mm}li{margin:2mm 0}.record{padding-left:6mm}.record li{margin:3.8mm 0}a{color:#30745a}.step{margin:2mm 0;padding-top:1.5mm;border-top:1px solid #cbdaca}.step h2{font-size:10.7pt;margin:0 0 1.5mm;color:#297452}.do{background:#edf3e9;padding:1.4mm 3mm;font-size:9.2pt;margin:0 0 2mm}.actions{margin:1mm 0 0;padding-left:4mm}.actions li{margin:.5mm 0}.label{font-size:7.1pt;letter-spacing:.6px;font-weight:700;color:#487960;margin:1.4mm 0 1mm}.spoken{font-size:10pt;line-height:1.31;margin:0 0 1.5mm}.check{font-size:8.5pt;color:#60745f;margin:0}.lesson h1{font-size:19pt}.second .meta{margin-bottom:1mm}.second main{padding-top:4mm}.lesson .speech{margin:1.8mm 0;padding-top:.5mm;padding-bottom:.5mm}.lesson .speech p{font-size:9.8pt;line-height:1.31}.lesson .prep{font-size:9pt;margin:2.5mm 0;padding:2.5mm 3mm}.lesson .extra,.lesson .trouble{font-size:8.8pt;padding:2.4mm 3mm;margin:2.5mm 0}.lesson .extra h3,.lesson .trouble h3{font-size:9pt;margin-bottom:1mm}.trouble{background:#f4f0e4;border-color:#b39856}.participant{font-size:8.5pt;background:#f4f0e4;padding:2mm}.refs{font-size:9.5pt}nav{position:sticky;top:0;z-index:2;background:#193d35;color:white;padding:12px 24px;display:flex;align-items:center;gap:14px}nav a{color:white}nav select{max-width:500px;padding:8px;font:inherit}nav strong{font-size:14px}@media print{body{background:white}.page{margin:0}nav{display:none}}"""
opts='<option value="p1">Cómo usar esta guía</option><option value="p2">Pantalla y pizarra</option><option value="p3">Alineación con estudiantes</option><option value="p4">Preparar la grabación</option>'+''.join(f'<option value="clase-{x["id"].replace(".","-")}">{x["id"]} · {e(x["title"])}</option>' for x in base)
nav='<nav><strong>GUION DEL PROFESOR</strong><select aria-label="Ir a una clase" onchange="document.getElementById(this.value).scrollIntoView()">'+opts+'</select><a href="PANTALLA-PARA-GRABAR.html" target="_blank">Abrir pantalla de práctica</a><a href="guia-profesor-detallada.pdf" target="_blank">PDF</a></nav>'
out='<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Guía del profesor UX/UI · Guion ampliado</title><style>'+css+'</style><body>'+nav+''.join(P)+'</body></html>'
(O/'EMPEZAR-AQUI.html').write_text(out,encoding='utf-8')
(O/'LEEME.txt').write_text('ABRE EMPEZAR-AQUI.html\n\nEsta edición contiene el guion ampliado del profesor, alineado con el programa de estudiantes.\nElige una clase en el menú y sigue sus dos páginas: parte A y parte B.\nAbre PANTALLA-PARA-GRABAR.html para mostrar la práctica.\nDi y Di al abrir/cerrar son textos para decir en voz alta. Las otras instrucciones son para ti.\nConserva recursos junto a los archivos. La herramienta funciona localmente; no envía solicitudes reales.\nEl programa del estudiante está en programa-estudiantes.pdf.\n',encoding='utf-8')
print(json.dumps({'html':str(O/'EMPEZAR-AQUI.html'),'pages':len(P),'classes':len(base),'expanded_steps':120},ensure_ascii=False))
