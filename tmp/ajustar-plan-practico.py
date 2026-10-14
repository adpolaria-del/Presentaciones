from pathlib import Path
p=Path('tmp/crear-plan-practico.py');s=p.read_text()
s=s.replace('/ 06','/ 07').replace('6 páginas.','7 páginas.')
s=s.replace('.section{margin:20px 0 11px;', '.section{margin:16px 0 10px;').replace('padding:11px 10px;border-bottom','padding:9px 10px;border-bottom')
s=s.replace('posiciones del ranking que Practico debe confirmar','referencias que Alejandra seleccionará según su conocimiento de la marca y sus ventas')
s=s.replace('Las referencias no incluyen el catálogo ni el ranking de ventas. Esta selección define el método y las oportunidades de temporada, sin atribuirle a Practico productos que no se han confirmado.','Alejandra elegirá los cinco productos por su conocimiento de la marca. El perfil @practicocol sirve como referencia creativa; sus publicaciones no permiten determinar cuáles son los más vendidos.')
s=s.replace('Consultar el histórico reciente','Alejandra selecciona los cinco productos')
s=s.replace('Revisar los últimos 60–90 días: unidades, ingresos, devoluciones, precio y margen por producto. Identificar los cinco más vendidos; validar con el equipo comercial si no existe un reporte.','Alejandra entrega P1–P5 con base en lo que conoce de la marca. Si hay historial disponible, contrastar los últimos 60–90 días de ventas; si no, registrar la selección como criterio comercial, no como ranking comprobado.')
s=s.replace("section('02','Ideas concretas, según el catálogo')","section('02','Ideas de octubre para validar con Alejandra')")
a=s.index('<table class="data"><thead><tr><th>Si Practico vende…')
b=s.index("'''+section('03','Material necesario para producir')",a)
s=s[:a]+'''<table class="data"><thead><tr><th>Referencia visible</th><th>Idea de anuncio en octubre</th><th>Validación</th></tr></thead><tbody><tr><td><strong>Radios retro</strong></td><td>“Dale ambiente a tus reuniones de octubre”. Video del producto en un espacio real, con funciones confirmadas.</td><td>Modelo, stock, precio y prestaciones.</td></tr><tr><td><strong>Reloj digital</strong></td><td>“Un detalle práctico para renovar tu espacio”. Foto en escritorio o mesa de noche.</td><td>Referencia, medidas y funciones.</td></tr><tr><td><strong>Taza para café</strong></td><td>“Una pausa con estilo en tus planes de octubre”. Demostración del producto y sus detalles.</td><td>Nombre comercial, uso y disponibilidad.</td></tr></tbody></table>
<p class="micro">Ejemplos observados en publicaciones de <a href="https://www.instagram.com/practicocol/">@practicocol</a> el 02/10/2026; no constituyen el top 5 ni confirman inventario. Halloween puede aportar ambientación, sin afirmar que se venden disfraces o decoración. Alejandra decide qué referencias encajan en la selección.</p>
'''+s[b:]
s=s.replace('Practico suministra y aprueba el material comercial.','Alejandra selecciona P1–P5 y aprueba precios y disponibilidad; Practico suministra el material comercial.')
s=s.replace('Confirmar P1–P5, stock, zona de entrega y canal de venta.','Alejandra confirma P1–P5 y stock. Definir zona de entrega y canal de venta.')
needle="'''+section('02','Reglas prácticas de optimización')+'''"
replacement="""'''+section('02','Convertir consultas en pedidos')+'''
<div class="step"><span>1</span><div><h3>Identificar producto y necesidad</h3><p>Registrar qué producto interesa, ciudad de entrega y origen de la consulta. Evitar pedir nuevamente datos que la persona ya compartió.</p></div></div>
<div class="step"><span>2</span><div><h3>Resolver y facilitar la compra</h3><p>Confirmar disponibilidad, precio total, envío, tiempos y forma de pago. Responder durante el horario comercial acordado y entregar un siguiente paso claro.</p></div></div>
<div class="step"><span>3</span><div><h3>Registrar el resultado</h3><p>Marcar consulta, pedido, pago o venta perdida. Compartir con Polar IA producto, valor y motivo de no compra, sin confundir una conversación con una venta.</p></div></div>
<p class="source">[3] <a href="https://www.facebookblueprint.com/student/page/652744-optimize-for-purchases-with-ads-that-click-to-message">Meta Blueprint · Compras mediante anuncios de mensajería y señales de compra</a>.</p>
''')
page('Responsables y próximos pasos','''
<p class="kicker">Ejecución y responsabilidades</p><h2 class="title">Cada tarea tiene<br>un responsable.</h2><p class="sub">La primera decisión es de Alejandra: escoger los cinco productos. Con esa selección, Polar IA adapta los guiones, configura la pauta y coordina el lanzamiento.</p>
'''+section('01','Reglas prácticas de optimización')+'''"""
assert needle in s;s=s.replace(needle,replacement)
s=s.replace("section('03','Qué entrega cada parte')","section('02','Qué entrega cada parte')")
s=s.replace('<h3>Practico</h3><p>Material y aprobaciones, stock actualizado y atención de consultas. Registro de pedidos, ingresos y estado de pago para contrastar resultados con la plataforma.','<h3>Alejandra / Practico</h3><p>Selección de P1–P5, precios, inventario y aprobación de piezas. Atención de consultas y registro de pedidos pagados para contrastar resultados.')
s=s.replace('<p class="admin"><strong>Antes del lanzamiento:</strong> confirmar catálogo y P1–P5, Instagram/Facebook oficiales, canal de venta, zonas de entrega, fecha de inicio y responsables de producción. Este documento es un plan; no implica que las campañas ya estén activas.</p>', '''<div class="notice"><strong>Ficha que debe entregar Alejandra por cada producto:</strong> nombre / referencia, precio, inventario, beneficio principal, fotos o videos disponibles y uso posible en octubre. Identificar las cinco fichas como P1, P2, P3, P4 y P5.</div>
<p class="admin"><strong>Antes del lanzamiento:</strong> selección de Alejandra aprobada; confirmar Facebook oficial, canal de venta, cobertura de entrega, fecha de inicio y responsable de producción. Instagram de referencia: <a href="https://www.instagram.com/practicocol/">@practicocol</a>. Este plan no implica que las campañas estén activas.</p>''')
s=s.replace('print(\'HTML completo y renderizador creados: 7 páginas.\')','print(\'HTML completo y renderizador creados: 7 páginas.\')')
p.write_text(s)
