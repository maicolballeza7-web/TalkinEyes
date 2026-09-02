# Fórmulas  — TalkinEyes

## EAR (Eye Aspect Ratio)

**Qué hace:** mide qué tan abierto está un ojo usando 6 puntos landmark
(4 en los párpados, 2 en las esquinas). Sirve para detectar parpadeos.

**Fórmula:**
EAR = (dist(p2,p6) + dist(p3,p5)) / (2 * dist(p1,p4))

**Fuente:** paper de Soukupová & Čech, "Real-Time Eye Blink Detection
using Facial Landmarks" (técnica estándar en visión computacional,
usada también en detectores de somnolencia al volante).

**Valores de referencia (medidos en mi propia cara):**
- Ojo abierto: ~0.28
- Ojo cerrado (parpadeo): (pendiente de confirmar)

## Índices de landmarks de MediaPipe Face Mesh

**Qué hacen:** de los 468 puntos totales del Face Mesh, estos son los
que corresponden a cada ojo (orden: esquina externa, párpado sup x2,
esquina interna, párpado inf x2).

LEFT_EYE  = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

**Fuente:** mapa oficial de landmarks de MediaPipe Face Mesh (Google).