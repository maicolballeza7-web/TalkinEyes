import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
# pip install pyttsx3
import threading
import queue
import colorsys
import pyttsx3
try:
    import pythoncom
except ImportError:
    pythoncom = None

cola_voz = queue.Queue()

def _worker_voz():
    if pythoncom:
        pythoncom.CoInitialize()
    while True:
        texto = cola_voz.get()
        if texto is None:
            break
        try:
            motor = pyttsx3.init()
            motor.setProperty('rate', 165)
            motor.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
            motor.say(texto)
            motor.runAndWait()
            motor.stop()
            del motor
        except Exception as e:
            print(f"Error de voz: {e}")

hilo_voz = threading.Thread(target=_worker_voz, daemon=True)
hilo_voz.start()

def hablar(texto):
    cola_voz.put(texto)
# aqui colocaremos el menu interactivo
ventana = tk.Tk()
ventana.title("TalkinEyes")
ventana.geometry("800x600")
ventana.configure(bg="#FFFFFF")

# abrimos un submenu como frame en lugar de abrir otra ventana de tkinter
submenu_comer = tk.Frame(ventana, width=800, height=600, bg="#FCFCFC")

# las frases
opciones_comer = [
    ("HAY ALGO DE COMER", "#e992a1"),
    ("TENGO HAMBRE", "#c9aa54"),
    ("QUIERO TOMAR ALGO", "#d2e67a"),
    ("NO QUIERO COMER", "#daa48b"),
]

# posicionamos las frases
posiciones_comer = [(50, 50, 750, 150), (50, 170, 750, 270), (50, 290, 750, 390), (50, 410, 750, 510)]

canvas_comer = tk.Canvas(submenu_comer, width=800, height=600, bg="#F4F7FB", highlightthickness=0)
canvas_comer.pack()
rectangulos_comer = []

canvas_comer.create_text(400, 25, text="🍽️ COMER", fill="#1E293B", font=("Segoe UI", 25, "bold"))
canvas_comer.create_text(400, 550, text="Selecciona con la mirada", fill="#64748B", font=("Segoe UI", 13, "bold"))

for i, (texto, color) in enumerate(opciones_comer):
    x1, y1, x2, y2 = posiciones_comer[i]
    canvas_comer.create_rectangle(x1 + 5, y1 + 6, x2 + 5, y2 + 6, fill="#D9E2F1", outline="")
    rect = canvas_comer.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    canvas_comer.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=texto, fill="white", font=("Segoe UI", 24, "bold"))
    rectangulos_comer.append(rect)

def resaltar_comer():
    global indice_comer
    aplicar_resaltado(
        canvas_comer,
        rectangulos_comer,
        [color for _, color in opciones_comer],
        indice_comer,
    )


# SUBMENU BAÑO
submenu_bano = tk.Frame(ventana, width=800, height=600, bg="#F4F7FB")

opciones_bano = [
    ("QUIERO IR AL BAÑO", "#4D6594"),
    ("NECESITO PAPEL", "#8CAFEE"),
    ("QUIERO LAVARME", "#82CFFD"),
    ("NO NECESITO IR", "#293C5E"),
]

posiciones_bano = [(50, 50, 750, 150), (50, 170, 750, 270), (50, 290, 750, 390), (50, 410, 750, 510)]

canvas_bano = tk.Canvas(submenu_bano, width=800, height=600, bg="#F4F7FB", highlightthickness=0)
canvas_bano.pack()
rectangulos_bano = []

canvas_bano.create_text(400, 25, text="🚿 BAÑO", fill="#1E293B", font=("Segoe UI", 25, "bold"))
canvas_bano.create_text(400, 550, text="Selecciona con la mirada", fill="#64748B", font=("Segoe UI", 13, "bold"))

for i, (texto, color) in enumerate(opciones_bano):
    x1, y1, x2, y2 = posiciones_bano[i]
    canvas_bano.create_rectangle(x1 + 5, y1 + 6, x2 + 5, y2 + 6, fill="#D9E2F1", outline="")
    rect = canvas_bano.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    canvas_bano.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=texto, fill="white", font=("Segoe UI", 24, "bold"))
    rectangulos_bano.append(rect)

def resaltar_bano():
    global indice_bano
    aplicar_resaltado(
        canvas_bano,
        rectangulos_bano,
        [color for _, color in opciones_bano],
        indice_bano,
    )


# SUBMENU DOLOR
submenu_dolor = tk.Frame(ventana, width=800, height=600, bg="#F4F7FB")

opciones_dolor = [
    ("ME DUELE LA CABEZA", "#FFB84D"),
    ("ME DUELE EL ESTÓMAGO", "#F5A65B"),
    ("ME DUELE EL PECHO", "#FF8E6E"),
    ("ME SIENTO MAL", "#E992A1"),
]

posiciones_dolor = [(50, 50, 750, 150), (50, 170, 750, 270), (50, 290, 750, 390), (50, 410, 750, 510)]

canvas_dolor = tk.Canvas(submenu_dolor, width=800, height=600, bg="#F4F7FB", highlightthickness=0)
canvas_dolor.pack()
rectangulos_dolor = []

canvas_dolor.create_text(400, 25, text="🩹 DOLOR", fill="#1E293B", font=("Segoe UI", 25, "bold"))
canvas_dolor.create_text(400, 550, text="Selecciona con la mirada", fill="#64748B", font=("Segoe UI", 13, "bold"))

for i, (texto, color) in enumerate(opciones_dolor):
    x1, y1, x2, y2 = posiciones_dolor[i]
    canvas_dolor.create_rectangle(x1 + 5, y1 + 6, x2 + 5, y2 + 6, fill="#D9E2F1", outline="")
    rect = canvas_dolor.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    canvas_dolor.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=texto, fill="white", font=("Segoe UI", 24, "bold"))
    rectangulos_dolor.append(rect)

def resaltar_dolor():
    global indice_dolor
    aplicar_resaltado(
        canvas_dolor,
        rectangulos_dolor,
        [color for _, color in opciones_dolor],
        indice_dolor,
    )


# SUBMENU DORMIR
submenu_dormir = tk.Frame(ventana, width=800, height=600, bg="#F4F7FB")

opciones_dormir = [
    ("TENGO SUEÑO", "#63C687"),
    ("QUIERO DORMIR", "#78CFA0"),
    ("NECESITO AYUDA", "#86CFA5"),
    ("NO TENGO SUEÑO", "#A4DB96"),
]

posiciones_dormir = [(50, 50, 750, 150), (50, 170, 750, 270), (50, 290, 750, 390), (50, 410, 750, 510)]

canvas_dormir = tk.Canvas(submenu_dormir, width=800, height=600, bg="#F4F7FB", highlightthickness=0)
canvas_dormir.pack()
rectangulos_dormir = []

canvas_dormir.create_text(400, 25, text="😴 DORMIR", fill="#1E293B", font=("Segoe UI", 25, "bold"))
canvas_dormir.create_text(400, 550, text="Selecciona con la mirada", fill="#64748B", font=("Segoe UI", 13, "bold"))

for i, (texto, color) in enumerate(opciones_dormir):
    x1, y1, x2, y2 = posiciones_dormir[i]
    canvas_dormir.create_rectangle(x1 + 5, y1 + 6, x2 + 5, y2 + 6, fill="#D9E2F1", outline="")
    rect = canvas_dormir.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    canvas_dormir.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=texto, fill="white", font=("Segoe UI", 24, "bold"))
    rectangulos_dormir.append(rect)

def resaltar_dormir():
    global indice_dormir
    aplicar_resaltado(
        canvas_dormir,
        rectangulos_dormir,
        [color for _, color in opciones_dormir],
        indice_dormir,
    )


# color para cada bloque
bloques_info = [
    ("COMER", "#FF8E6E"),
    ("BAÑO", "#6D9BF7"),
    ("DOLOR", "#FFB84D"),
    ("DORMIR", "#63C687"),
]

canvas = tk.Canvas(ventana, width=800, height=600, bg="#F4F7FB", highlightthickness=0)
canvas.pack()
rectangulos = []

canvas.create_text(400, 25, text="TalkinEyes", fill="#1E293B", font=("Segoe UI", 25, "bold"))
canvas.create_text(400, 53, text="Menú de asistencia", fill="#64748B", font=("Segoe UI", 12, "bold"))

# funcion para crear rectangulos redondeados
def rectangulo_redondeado(canvas, x1, y1, x2, y2, radio, color, tag):
    puntos = [
        x1 + radio, y1, x2 - radio, y1,
        x2, y1 + radio, x2, y2 - radio,
        x2 - radio, y2, x1 + radio, y2,
        x1, y2 - radio, x1, y1 + radio
    ]
    return canvas.create_polygon(puntos, fill=color, outline="", smooth=True, tags=tag)

# posiciones de los bloques
posiciones = [
    (50, 80, 390, 290),
    (390, 80, 730, 290),
    (50, 300, 390, 510),
    (390, 300, 730, 510),
]

# cual bloque esta resaltado actualmente
indice_actual = 0
pantalla_actual = "principal"
indice_comer = 0
indice_bano = 0
indice_dolor = 0
indice_dormir = 0
id_timer_escaneo = None
frames_ojo_cerrado = 0
FRAMES_MINIMOS_INTENCIONAL = 10 
INTERVALO_ESCANEO = 2500  # ms entre cada avance automático

# se recorre cada bloque para su seleccion
emojis = ["🍽️", "🚿", "🩹", "😴"]

for i, (texto, color) in enumerate(bloques_info):
    x1, y1, x2, y2 = posiciones[i]

    # Sombra suave de la tarjeta
    rectangulo_redondeado(canvas, x1 + 5, y1 + 7, x2 + 5, y2 + 7, 30, "#D9E2F1", f"sombra_{i}")

    rect = rectangulo_redondeado(canvas, x1, y1, x2, y2, 30, color, f"bloque_{i}")

    canvas.create_text(
        (x1 + x2) // 2, (y1 + y2) // 2,
        text=f"{emojis[i]} {texto}",
        fill="white",
        font=("Segoe UI", 28, "bold")
    )

    rectangulos.append(rect)

canvas.create_text(400, 550, text="Selecciona con un parpadeo", fill="#64748B", font=("Segoe UI", 13, "bold"))


def cancelar_timer():
    global id_timer_escaneo
    if id_timer_escaneo is not None:
        ventana.after_cancel(id_timer_escaneo)
        id_timer_escaneo = None


# funcion para seleccionar una opcion de COMER
def seleccionar_comer():
    global pantalla_actual
    opcion = opciones_comer[indice_comer][0]
    print(f"Seleccionado: {opcion}")
    hablar(opcion)   
    cancelar_timer()

    # Ocultar submenu
    submenu_comer.pack_forget()
    canvas.pack()

    # Volvemos al menu principal
    pantalla_actual = "principal"
    iniciar_escaneo_principal()


# funcion para seleccionar una opcion de BAÑO
def seleccionar_bano():
    global pantalla_actual
    opcion = opciones_bano[indice_bano][0]
    print(f"Seleccionado: {opcion}")
    hablar(opcion)   
    cancelar_timer()
    submenu_bano.pack_forget()
    canvas.pack()
    pantalla_actual = "principal"
    iniciar_escaneo_principal()


# funcion para seleccionar una opcion de DOLOR
def seleccionar_dolor():
    global pantalla_actual
    opcion = opciones_dolor[indice_dolor][0]
    print(f"Seleccionado: {opcion}")
    hablar(opcion)   
    cancelar_timer()
    submenu_dolor.pack_forget()
    canvas.pack()
    pantalla_actual = "principal"
    iniciar_escaneo_principal()


# funcion para seleccionar una opcion de DORMIR
def seleccionar_dormir():
    global pantalla_actual
    opcion = opciones_dormir[indice_dormir][0]
    print(f"Seleccionado: {opcion}")
    hablar(opcion)   
    cancelar_timer()
    submenu_dormir.pack_forget()
    canvas.pack()
    pantalla_actual = "principal"
    iniciar_escaneo_principal()


# funcion para seleccionar un bloque
def seleccionar_bloque():
    global pantalla_actual
    bloque = bloques_info[indice_actual][0]
    print(f"Seleccionado: {bloque}")

    if bloque == "COMER":
        cancelar_timer()
        canvas.pack_forget()
        submenu_comer.pack()
        pantalla_actual = "comer"
        iniciar_escaneo_comer()

    elif bloque == "BAÑO":
        cancelar_timer()
        canvas.pack_forget()
        submenu_bano.pack()
        pantalla_actual = "bano"
        iniciar_escaneo_bano()

    elif bloque == "DOLOR":
        cancelar_timer()
        canvas.pack_forget()
        submenu_dolor.pack()
        pantalla_actual = "dolor"
        iniciar_escaneo_dolor()

    elif bloque == "DORMIR":
        cancelar_timer()
        canvas.pack_forget()
        submenu_dormir.pack()
        pantalla_actual = "dormir"
        iniciar_escaneo_dormir()


# RESALTADOR
def color_mas_intenso(color):
    """Aumenta saturacion y brillo de forma pareja usando HSV, sin importar el color base."""
    rojo = int(color[1:3], 16) / 255.0
    verde = int(color[3:5], 16) / 255.0
    azul = int(color[5:7], 16) / 255.0

    h, l, s = colorsys.rgb_to_hls(rojo, verde, azul)

    # subimos saturacion y brillo de forma controlada, con topes para no quemar el color
    s = min(1.0, s * 1.3 + 0.15)
    l = min(0.72, l * 1.15 + 0.12)  # tope en 0.72 para que no se lave a blanco

    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)

    return f"#{int(r2 * 255):02X}{int(g2 * 255):02X}{int(b2 * 255):02X}"


glow_ids = {}  # guarda el id del glow por canvas, para poder borrarlo despues

def aplicar_resaltado(canvas_obj, rectangulos_obj, colores, indice):

    for rect, color in zip(rectangulos_obj, colores):
        canvas_obj.itemconfig(rect, fill=color, outline="", width=1)

    # borramos el glow anterior de ESTE canvas si existia
    if canvas_obj in glow_ids and glow_ids[canvas_obj] is not None:
        canvas_obj.delete(glow_ids[canvas_obj])
        glow_ids[canvas_obj] = None

    rect_actual = rectangulos_obj[indice]
    canvas_obj.itemconfig(
        rect_actual,
        fill=color_mas_intenso(colores[indice]),
        outline="#FFFFFF",
        width=10,
    )

    # dibujamos un halo dorado detras del bloque activo
    x1, y1, x2, y2 = canvas_obj.bbox(rect_actual)
    margen = 12
    nuevo_glow = canvas_obj.create_rectangle(
        x1 - margen, y1 - margen, x2 + margen, y2 + margen,
        outline="#6AA1A3", width=4
    )
    canvas_obj.tag_lower(nuevo_glow, rect_actual)
    glow_ids[canvas_obj] = nuevo_glow


def resaltar_siguiente():
    global indice_actual

    aplicar_resaltado(
        canvas,
        rectangulos,
        [color for _, color in bloques_info],
        indice_actual,
    )


# Funcion para pasar al siguiente bloque (SOLO avanza, ya no selecciona)
def siguiente_bloque():
    global indice_actual, id_timer_escaneo

    if pantalla_actual != "principal":
        return  # cambiaste de pantalla, se detiene el escaneo aqui

    indice_actual += 1

    if indice_actual >= len(rectangulos):
        indice_actual = 0

    resaltar_siguiente()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_bloque)


def iniciar_escaneo_principal():
    global id_timer_escaneo
    cancelar_timer()
    resaltar_siguiente()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_bloque)


# Funcion para pasar a la siguiente opcion del submenu COMER (SOLO avanza)
def siguiente_opcion_comer():
    global indice_comer, id_timer_escaneo

    if pantalla_actual != "comer":
        return

    indice_comer += 1

    if indice_comer >= len(rectangulos_comer):
        indice_comer = 0

    resaltar_comer()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_comer)


def iniciar_escaneo_comer():
    global id_timer_escaneo
    cancelar_timer()
    resaltar_comer()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_comer)


# Funcion para pasar a la siguiente opcion del submenu BAÑO
def siguiente_opcion_bano():
    global indice_bano, id_timer_escaneo

    if pantalla_actual != "bano":
        return

    indice_bano += 1

    if indice_bano >= len(rectangulos_bano):
        indice_bano = 0

    resaltar_bano()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_bano)


def iniciar_escaneo_bano():
    global id_timer_escaneo
    cancelar_timer()
    resaltar_bano()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_bano)


# Funcion para pasar a la siguiente opcion del submenu DOLOR
def siguiente_opcion_dolor():
    global indice_dolor, id_timer_escaneo

    if pantalla_actual != "dolor":
        return

    indice_dolor += 1

    if indice_dolor >= len(rectangulos_dolor):
        indice_dolor = 0

    resaltar_dolor()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_dolor)


def iniciar_escaneo_dolor():
    global id_timer_escaneo
    cancelar_timer()
    resaltar_dolor()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_dolor)


# Funcion para pasar a la siguiente opcion del submenu DORMIR
def siguiente_opcion_dormir():
    global indice_dormir, id_timer_escaneo

    if pantalla_actual != "dormir":
        return

    indice_dormir += 1

    if indice_dormir >= len(rectangulos_dormir):
        indice_dormir = 0

    resaltar_dormir()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_dormir)


def iniciar_escaneo_dormir():
    global id_timer_escaneo
    cancelar_timer()
    resaltar_dormir()
    id_timer_escaneo = ventana.after(INTERVALO_ESCANEO, siguiente_opcion_dormir)


# MEDIAPIPE
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# LANDMARKS de los ojos
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
CONTORNOS_OJOS = [
    (mp_face_mesh.FACEMESH_LEFT_EYE, (255, 220, 130)),
    (mp_face_mesh.FACEMESH_RIGHT_EYE, (255, 220, 130)),
]
INDICES_ESQUINAS_OJOS = [33, 133, 362, 263]

# Umbral para determinar el estado del ojo
UMBRAL_CIERRE = 0.16       # por debajo de esto, se considera que el ojo se cerró
UMBRAL_REAPERTURA = 0.28   # por encima de esto, se considera que el ojo se abrió

# apertura de la camara
cap = cv2.VideoCapture(0)
camara_label = tk.Label(
    ventana,
    bg="#1E293B",
    bd=2,
    relief="solid",
)
camara_label.place(x=10, y=10, width=240, height=180)
estado_anterior = "abierto"

# funcion calcular EAR
def calcular_ear(eye_points, image_w, image_h):
    coordenadas = [(p.x * image_w, p.y * image_h) for p in eye_points]
    p1, p2, p3, p4, p5, p6 = coordenadas

    vertical_1 = np.linalg.norm(np.array(p2) - np.array(p6))
    vertical_2 = np.linalg.norm(np.array(p3) - np.array(p5))
    horizontal = np.linalg.norm(np.array(p1) - np.array(p4))

    if horizontal < 1e-3:
        return None  # detección poco confiable, descarta este frame

    return (vertical_1 + vertical_2) / (2.0 * horizontal)


face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    # que si exista alguien la probabilidad
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

estado_anterior = "abierto"

def procesar_camara():
    global estado_anterior, pantalla_actual, frames_ojo_cerrado

    success, image = cap.read()

    if not success:
        return

    image = cv2.flip(image, 1)

    # Convertir la imagen de BGR a RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = face_mesh.process(image)

    # Dibujar la malla en la imagen
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    parpadeo = False

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=mp_drawing.DrawingSpec(
                    color=(255, 255, 255),
                    thickness=1,
                    circle_radius=1
                    ),
                
                    connection_drawing_spec=mp_drawing.DrawingSpec(
                    color=(200, 255, 100),
                    thickness=1,
                    circle_radius=1
                    ),
            )

            # Contornos limpios de ambos ojos.
            h, w, _ = image.shape
            for conexiones, color in CONTORNOS_OJOS:
                for pt1_idx, pt2_idx in conexiones:
                    lm1 = face_landmarks.landmark[pt1_idx]
                    lm2 = face_landmarks.landmark[pt2_idx]
                    x1, y1 = int(lm1.x * w), int(lm1.y * h)
                    x2, y2 = int(lm2.x * w), int(lm2.y * h)
                    cv2.line(image, (x1, y1), (x2, y2), color, 1, cv2.LINE_AA)

            # calculamos los landmarks de los ojos
            left_eye_points = [face_landmarks.landmark[i] for i in LEFT_EYE]
            right_eye_points = [face_landmarks.landmark[i] for i in RIGHT_EYE]

            # obtenemos los EAR
            left_ear = calcular_ear(left_eye_points, w, h)
            right_ear = calcular_ear(right_eye_points, w, h)

            if left_ear is None or right_ear is None:
                imagen_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                imagen_tk = ImageTk.PhotoImage(
                    Image.fromarray(imagen_rgb).resize((240, 180))
                )
                camara_label.imgtk = imagen_tk
                camara_label.configure(image=imagen_tk)
                ventana.after(10, procesar_camara)
                return

            ear_promedio = (left_ear + right_ear) / 2.0

            print(f"EAR: {ear_promedio:.3f}")

            # determinamos si el ojo esta cerrado
            if estado_anterior == "abierto" and ear_promedio < UMBRAL_CIERRE:
                estado_actual = "cerrado"
            elif estado_anterior == "cerrado" and ear_promedio > UMBRAL_REAPERTURA:
                estado_actual = "abierto"
            else:
                estado_actual = estado_anterior

            frames_cerrados_previos = frames_ojo_cerrado

            if estado_actual == "cerrado":
              frames_ojo_cerrado += 1
            else:
              frames_ojo_cerrado = 0

            if estado_anterior == "cerrado" and estado_actual == "abierto":
             if frames_cerrados_previos >= FRAMES_MINIMOS_INTENCIONAL:
                print("parpadeo intencional")
                parpadeo = True
             else:
                print("parpadeo natural (ignorado)")

            color_estado = (0, 255, 100) if parpadeo else (255, 250, 130)
            for idx in INDICES_ESQUINAS_OJOS:
               lm = face_landmarks.landmark[idx]
               x, y = int(lm.x * w), int(lm.y * h)
               cv2.circle(image, (x, y), 4, color_estado, -1, cv2.LINE_AA)
               cv2.circle(image, (x, y), 7, color_estado, 1, cv2.LINE_AA)

            # seleccionamos el bloque cuando hay parpadeo
            if parpadeo:
                if pantalla_actual == "principal":
                    seleccionar_bloque()

                elif pantalla_actual == "comer":
                    seleccionar_comer()

                elif pantalla_actual == "bano":
                    seleccionar_bano()

                elif pantalla_actual == "dolor":
                    seleccionar_dolor()

                elif pantalla_actual == "dormir":
                    seleccionar_dormir()
              # actualizamos el estado para el siguiente frame
            estado_anterior = estado_actual
    imagen_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imagen_tk = ImageTk.PhotoImage(
        Image.fromarray(imagen_rgb).resize((240, 180))
    )
    camara_label.imgtk = imagen_tk
    camara_label.configure(image=imagen_tk)

    ventana.after(10, procesar_camara)

def cerrar_app():
    cap.release()
    ventana.destroy()


ventana.protocol("WM_DELETE_WINDOW", cerrar_app)

iniciar_escaneo_principal()
procesar_camara()

ventana.mainloop()


