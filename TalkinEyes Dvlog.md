# TalkinEyes 👁️

**Dale voz a quien solo puede parpadear.**

Dispositivo de comunicación por parpadeos para personas con discapacidad motriz o de habla (como ELA). Usa visión computacional para detectar parpadeos intencionales y traducirlos en selecciones de un menú (comer, baño, dolor, etc.), que después se convierten en voz.

La idea está inspirada en los sistemas de comunicación asistida tipo Stephen Hawking, pero simplificada: selecciona una opción de un menú de necesidades básicas.

27 agosto
colocamos los puntos que son para los ojos  con eye left y una lista de valores de los landmarks 
luego haremos una funcion para detectar el EAR
---
28 agosto
comenzamos con mediciones de los ear
ear abierto == a promedios entre 0.20 a 0. 30
ear cerrado == a casi siempre 0 . 05 o similares hasta llegara al 0 ademas que hisimos una maquina de estados

## Cómo funciona (por ahora)

- **Detección facial**:  detecta 468 puntos de la cara en tiempo real con la cámara.
- **Detección de parpadeo**: se aíslan los puntos de los ojos y se calcula el **EAR** (qué tan abierto/cerrado está el ojo).
- **Verificación de mirada**: si el usuario no está viendo a la cámara, se cancela la selección (para evitar errores).
- **Menú → voz**: el parpadeo elige una opción del menú y esa opción se convierte en voz.

Es un proyecto **100% software**, sin sensores externos 


## Con qué está hecho

- Python
- MediaPipe (Face Mesh)
- OpenCV
- motor de texto a voz

---

## Uso de IA

Usé IA (Claude) para dudas y ayuda para destrabarme mientras aprendía Python y MediaPipe. Las decisiones de diseño (el sistema de menú por parpadeos, el uso de EAR, la exploración con máscaras de bits) y la mayoría del código son mías. Solo copié una plantilla para activar el Face Mesh de MediaPipe; el resto lo investigué y escribí yo.

---

## Por qué lo hago

Empezó como proyecto para un evento de física de la universidad, pero se volvió algo que quiero seguir construyendo más allá de eso. La meta es mantenerlo simple pero que de verdad le pueda servir a alguien que lo necesite.

---

## Autor

Hecho por [@maicol](https://github.com/maicolballeza7-web)
