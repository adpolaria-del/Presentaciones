from pathlib import Path
import re
s=Path('tmp/crear-plan-practico.py').read_text()
replacements={
'Practico':'Practiverso',
'PLAN DE ACCIÓN · OCTUBRE 2026':'PLAN DE ACCIÓN · 12–31 OCTUBRE 2026',
'Propuesta operativa · 02 de octubre de 2026':'Actualización · 03 de octubre de 2026',
'Plan de acción<br>para octubre.':'Plan de acción<br>Practiverso.',
'Una marca más visible. Una ruta clara a la compra.':'12–31 de octubre de 2026 · 20 días de pauta',
'$600.000':'$400.000',
'$450.000':'$300.000',
'$150.000':'$100.000',
'$75.000':'$50.000',
'$1.250.000':'$1.050.000',
'Total para 30 días de pauta':'Total para 20 días de pauta',
'R3 · Ideas para octubre':'R3 · Un producto, una solución',
'Uno de los cinco productos en una situación de octubre coherente con su uso. Referencia a Halloween solo si el catálogo y la disponibilidad lo permiten.':'Mostrar uno de los cinco productos en una situación cotidiana. Una imagen clara, un beneficio comprobable y una invitación a conocer sus detalles en el perfil.',
'“Dale una idea nueva a tus planes de octubre. Conoce la selección.”':'“Descubre una solución para tu día a día. Conoce los detalles en Practiverso.”',
'Primera mitad · Instagram':'12–21 de octubre · Instagram',
'Segunda mitad · Facebook':'22–31 de octubre · Facebook',
'Ángulo:</strong> utilidad en octubre. Escena real de temporada, producto visible y beneficio concreto. Sin descuentos ni escasez inventados.':'Ángulo:</strong> utilidad cotidiana. Mostrar el producto resolviendo una necesidad real, con su beneficio principal y precio vigente. Sin descuentos ni escasez inventados.',
'“Este octubre, [uso de temporada] con [producto]. Conoce sus detalles y consulta disponibilidad”.':'“Haz más fácil [tarea cotidiana] con [producto]. Conoce sus detalles y consulta disponibilidad”.',
'Productos y contenido de octubre':'Selección de productos y contenido',
'El perfil @practicocol sirve como referencia creativa; sus publicaciones no permiten determinar cuáles son los más vendidos.':'Los anuncios se centrarán en beneficios, usos y demostraciones. La selección comercial se confirma antes de producir las piezas.',
'Verificar que se puedan vender durante octubre':'Verificar disponibilidad del 12 al 31 de octubre',
'Asignar un uso de temporada':'Asignar una necesidad cotidiana',
'Adaptar el mensaje de P1–P5 a situaciones de octubre. Un producto estacional nuevo no sustituye automáticamente a un más vendido ni añade un sexto anuncio.':'Relacionar P1–P5 con una necesidad real: ambientar un espacio, organizar una rutina, disfrutar una bebida o resolver una tarea. Cada producto conserva un anuncio de ventas.',
'Ideas de octubre para validar con Alejandra':'Ideas de producto para validar con Alejandra',
'Idea de anuncio en octubre':'Idea de anuncio',
'“Dale ambiente a tus reuniones de octubre”':'“Dale ambiente a tus espacios y reuniones”',
'“Una pausa con estilo en tus planes de octubre”':'“Una pausa con estilo en tu día a día”',
'Ejemplos observados en publicaciones de <a href="https://www.instagram.com/practicocol/">@practicocol</a> el 02/10/2026; no constituyen el top 5 ni confirman inventario. Halloween puede aportar ambientación, sin afirmar que se venden disfraces o decoración. Alejandra decide qué referencias encajan en la selección.':'Ejemplos del <a href="https://www.instagram.com/practicocol/">perfil de referencia compartido</a>, revisado el 02/10/2026; no constituyen el top 5 ni confirman inventario. Alejandra decide cuáles referencias encajan. El enfoque creativo será el uso cotidiano del producto.',
'fotos o videos disponibles y uso posible en octubre':'fotos o videos disponibles y necesidad cotidiana que resuelve',
'Instagram de referencia: <a href="https://www.instagram.com/practicocol/">@practicocol</a>.':'Confirmar los perfiles vigentes de Practiverso antes de dirigir visitas; no se presupone un cambio de usuario o URL.',
'Plan de acción · Octubre 2026 · Practiverso / Polar IA':'Plan de acción · Practiverso · 12–31 octubre 2026',
'plan-accion-octubre-practico-polar-ia':'plan-accion-practiverso-12-31-octubre-2026',
'render-plan-practico.mjs':'render-plan-practiverso.mjs',
}
for old,new in replacements.items():
 assert old in s, old
 s=s.replace(old,new)
a=s.index('<p class="small">*Los valores diarios')
b=s.index('</p>',a)+4
s=s[:a]+'''<p class="small">*Periodo de pauta: <strong>del 12 al 31 de octubre, ambos días incluidos: 20 días</strong>. Ventas: $15.000 × 20 = $300.000. Visitas: $5.000 × 20 = $100.000. Se fijarán presupuestos totales y fecha de cierre para controlar la inversión.</p>'''+s[b:]
a=s.index("page('Calendario de ejecución',")
b=s.index("page('Medición y operación',",a)
s=s[:a]+'''page('Calendario de ejecución',\'\'\'
<p class="kicker">12–31 de octubre · contenido de producto</p><h2 class="title">Tres semanas para lanzar,<br>aprender y optimizar.</h2><p class="sub">La preparación se realizará del 5 al 11 de octubre. La pauta comienza el 12 y termina el 31: 20 días activos. Las piezas se enfocarán en beneficios, demostraciones y usos cotidianos.</p>
<table class="data"><thead><tr><th>Etapa</th><th>Qué se hará</th><th>Resultado de trabajo</th></tr></thead><tbody>
<tr><td><strong>5–11 octubre</strong><br>Preparación<br>Sin pauta</td><td>Alejandra confirma P1–P5, precios y stock. Preparar y aprobar los 8 anuncios; revisar accesos, identidad de Practiverso, medición, destinos y recorrido de compra.</td><td>Piezas aprobadas y campañas programadas para el 12, sujetas a revisión de la plataforma.</td></tr>
<tr><td><strong>12–18 octubre</strong><br>Lanzar y medir<br>7 días</td><td>Activar V1–V5 y el bloque de Instagram con R1/R3. Revisar entrega, enlaces, gasto y calidad de consultas. Corregir fallos y establecer la línea base.</td><td>Primer corte de visitas, consultas, ventas y gasto por anuncio.</td></tr>
<tr><td><strong>19–25 octubre</strong><br>Comparar y ajustar<br>7 días</td><td>Analizar consultas y ventas; rotar piezas con poca entrega. Terminar Instagram el 21 e iniciar Facebook con R2 el 22. Mantener la campaña de ventas.</td><td>Ajustes documentados y señales de los productos con mayor interés de compra.</td></tr>
<tr><td><strong>26–31 octubre</strong><br>Optimizar y cerrar<br>6 días</td><td>Priorizar anuncios con mejor desempeño y productos disponibles. Ajustar argumentos según objeciones reales. Finalizar la pauta el 31 y consolidar resultados.</td><td>Informe de cierre, aprendizajes y recomendación para el siguiente ciclo.</td></tr>
</tbody></table>
\'\'\'+section('01','Inversión por semana')+\'\'\'
<table class="data"><thead><tr><th>Periodo de pauta</th><th>Días</th><th>Ventas</th><th>Visitas</th><th>Total</th></tr></thead><tbody>
<tr><td>12–18 octubre</td><td>7</td><td>$105.000</td><td>$35.000</td><td>$140.000</td></tr>
<tr><td>19–25 octubre</td><td>7</td><td>$105.000</td><td>$35.000</td><td>$140.000</td></tr>
<tr><td>26–31 octubre</td><td>6</td><td>$90.000</td><td>$30.000</td><td>$120.000</td></tr>
<tr class="total"><td>Total</td><td>20</td><td>$300.000</td><td>$100.000</td><td>$400.000</td></tr>
</tbody></table>
<p class="small">Distribución de referencia, no promesa de gasto idéntico cada día. Visitas: Instagram del 12 al 21 y Facebook del 22 al 31, diez días y $50.000 por bloque. Ventas permanece activa durante los veinte días.</p>
<div class="notice"><strong>Si el lanzamiento se retrasa:</strong> mantener como referencia $15.000 diarios para ventas y $5.000 para visitas, terminar el 31 y reducir el total según los días realmente disponibles. No aumentar el ritmo diario ni extender la pauta sin acuerdo previo.</div>
\'\'\')
'''+s[b:]
# Keep the public social URL supplied by the client, without inventing a new handle.
for forbidden in ['Halloween','temporada','estacional','30 días','27 días','$600.000','$450.000','$150.000','$75.000','$1.250.000','@practicocol','Practico']:
 assert forbidden not in s, forbidden
Path('tmp/crear-plan-practiverso.py').write_text(s)
