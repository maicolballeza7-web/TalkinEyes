
# ===============================================================
# MEJORAS PARPADEO - VERSIÓN 2.1
# ===============================================================
#
# Archivo experimental independiente para probar mejoras del
# reconocimiento de parpadeos sin tocar el proyecto principal.
#
# CAMBIOS DE ESTA VERSIÓN:
#   1) Se añade MEDIANA a la calibración.
#   2) Los umbrales se calculan usando la mediana.
#   3) Se muestran promedio y mediana para comparar.
#   4) Se utiliza realmente UMBRAL_REAPERTURA.
#   5) Se mantiene la lógica de duración y cooldown.
#
# ===============================================================


# ==============================
# CONFIGURACIÓN
# ==============================

DURACION_CALIBRACION = 4.0

FACTOR_CIERRE = 0.92
FACTOR_REAPERTURA = 1.10

DURACION_MINIMA_PARPADEO = 0.18
TIEMPO_COOLDOWN = 1.0

# Valores iniciales.
# Se actualizan automáticamente después de la calibración.

UMBRAL_CIERRE = 0.16
UMBRAL_REAPERTURA = 0.28


LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]


# ==============================
# IMPORTACIONES
# ==============================

import cv2
import mediapipe as mp
import numpy as np
import time


mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh


# ==============================
# 1) CÁLCULO DEL EAR
# ==============================

def calcular_ear(eye_points, image_w, image_h):
    """
    Calcula el Eye Aspect Ratio (EAR)
    usando 6 landmarks del ojo.
    """

    coordenadas = [
        (p.x * image_w, p.y * image_h)
        for p in eye_points
    ]

    p1, p2, p3, p4, p5, p6 = coordenadas

    vertical_1 = np.linalg.norm(
        np.array(p2) - np.array(p6)
    )

    vertical_2 = np.linalg.norm(
        np.array(p3) - np.array(p5)
    )

    horizontal = np.linalg.norm(
        np.array(p1) - np.array(p4)
    )

    if horizontal == 0:
        return 0.0

    return (
        (vertical_1 + vertical_2)
        / (2.0 * horizontal)
    )


# ==============================
# 2) CALIBRACIÓN DE OJOS ABIERTOS
# ==============================

def calibrar_ojos_abiertos(
    face_mesh,
    camera_index=0,
    segundos=DURACION_CALIBRACION
):
    """
    Pide al usuario mantener los ojos abiertos
    y toma varias mediciones.
    """

    print("\nCALIBRACIÓN DE OJOS ABIERTOS")
    print("Mantén los ojos abiertos normalmente...")
    print("Calibrando...")

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("No se pudo abrir la cámara para calibrar.")
        return None, None, None, None

    muestras = []

    inicio = time.time()

    while time.time() - inicio < segundos:

        ret, frame = cap.read()

        if not ret:
            continue

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        rgb.flags.writeable = False

        results = face_mesh.process(rgb)

        rgb.flags.writeable = True

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:

                left_eye_points = [
                    face_landmarks.landmark[i]
                    for i in LEFT_EYE
                ]

                right_eye_points = [
                    face_landmarks.landmark[i]
                    for i in RIGHT_EYE
                ]

                h, w, _ = frame.shape

                left_ear = calcular_ear(
                    left_eye_points,
                    w,
                    h
                )

                right_ear = calcular_ear(
                    right_eye_points,
                    w,
                    h
                )

                ear_promedio = (
                    left_ear + right_ear
                ) / 2.0

                muestras.append(ear_promedio)

                cv2.putText(
                    frame,
                    f"EAR promedio: {ear_promedio:.3f}",
                    (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

        cv2.imshow(
            "Calibracion - ojos abiertos",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):

            cap.release()
            cv2.destroyAllWindows()

            return None, None, None, None

    cap.release()
    cv2.destroyAllWindows()

    if not muestras:

        print("No se registraron suficientes mediciones.")

        return None, None, None, None

    ear_min = np.min(muestras)
    ear_max = np.max(muestras)
    ear_promedio = np.mean(muestras)
    ear_mediana = np.median(muestras)

    print("\nCalibración de ojos abiertos terminada")

    print(f"EAR mínimo:    {ear_min:.3f}")
    print(f"EAR máximo:    {ear_max:.3f}")
    print(f"EAR promedio:  {ear_promedio:.3f}")
    print(f"EAR mediana:   {ear_mediana:.3f}")

    return (
        ear_min,
        ear_max,
        ear_promedio,
        ear_mediana
    )


# ==============================
# 3) CALIBRACIÓN DE OJOS CERRADOS
# ==============================

def calibrar_ojos_cerrados(
    face_mesh,
    camera_index=0,
    segundos=DURACION_CALIBRACION
):
    """
    Pide al usuario cerrar los ojos y toma
    varias mediciones para el estado cerrado.
    """

    print("\nCALIBRACIÓN DE OJOS CERRADOS")
    print("Cierra los ojos suavemente y mantén esa posición...")
    print("Calibrando...")

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():

        print(
            "No se pudo abrir la cámara "
            "para calibrar ojos cerrados."
        )

        return None, None, None, None

    muestras = []

    inicio = time.time()

    while time.time() - inicio < segundos:

        ret, frame = cap.read()

        if not ret:
            continue

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        rgb.flags.writeable = False

        results = face_mesh.process(rgb)

        rgb.flags.writeable = True

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:

                left_eye_points = [
                    face_landmarks.landmark[i]
                    for i in LEFT_EYE
                ]

                right_eye_points = [
                    face_landmarks.landmark[i]
                    for i in RIGHT_EYE
                ]

                h, w, _ = frame.shape

                left_ear = calcular_ear(
                    left_eye_points,
                    w,
                    h
                )

                right_ear = calcular_ear(
                    right_eye_points,
                    w,
                    h
                )

                ear_promedio = (
                    left_ear + right_ear
                ) / 2.0

                muestras.append(ear_promedio)

                cv2.putText(
                    frame,
                    f"EAR promedio: {ear_promedio:.3f}",
                    (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2,
                )

        cv2.imshow(
            "Calibracion - ojos cerrados",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):

            cap.release()
            cv2.destroyAllWindows()

            return None, None, None, None

    cap.release()
    cv2.destroyAllWindows()

    if not muestras:

        print(
            "No se registraron suficientes "
            "mediciones para ojos cerrados."
        )

        return None, None, None, None

    ear_min = np.min(muestras)
    ear_max = np.max(muestras)
    ear_promedio = np.mean(muestras)
    ear_mediana = np.median(muestras)

    print("\nCalibración de ojos cerrados terminada")

    print(f"EAR mínimo:    {ear_min:.3f}")
    print(f"EAR máximo:    {ear_max:.3f}")
    print(f"EAR promedio:  {ear_promedio:.3f}")
    print(f"EAR mediana:   {ear_mediana:.3f}")

    return (
        ear_min,
        ear_max,
        ear_promedio,
        ear_mediana
    )


# ==============================
# 4) SEPARACIÓN ENTRE ESTADOS
# ==============================

def calcular_separacion(
    ear_abierto,
    ear_cerrado
):
    """
    Calcula la diferencia entre los valores
    representativos de ojos abiertos y cerrados.
    """

    if (
        ear_abierto is None
        or ear_cerrado is None
    ):
        return 0.0

    return ear_abierto - ear_cerrado


# ==============================
# 5) PROPUESTA DE UMBRALES
# ==============================

def proponer_umbrales(
    ear_mediana_abierto,
    ear_mediana_cerrado
):
    """
    Genera los umbrales utilizando las MEDIANAS
    obtenidas durante la calibración.

    UMBRAL_CIERRE:
        Valor por debajo del cual consideramos
        que los ojos están cerrados.

    UMBRAL_REAPERTURA:
        Valor por encima del cual consideramos
        que los ojos volvieron a abrirse.
    """

    separacion = calcular_separacion(
        ear_mediana_abierto,
        ear_mediana_cerrado
    )

    if separacion <= 0:

        print(
            "\nADVERTENCIA:"
            "\nLa calibración no muestra una "
            "separación válida entre abiertos y cerrados."
        )

        return (
            UMBRAL_CIERRE,
            UMBRAL_REAPERTURA
        )

    umbral_cierre = (
        ear_mediana_abierto
        - (
            separacion
            * FACTOR_CIERRE
        )
    )

    umbral_reapertura = (
        ear_mediana_abierto
        - (
            separacion
            * FACTOR_REAPERTURA
        )
    )

    # Aseguramos que el umbral de reapertura
    # no quede por debajo del de cierre.

    if umbral_reapertura <= umbral_cierre:

        umbral_reapertura = (
            umbral_cierre
            + separacion * 0.15
        )

    print("\nPropuesta de umbrales:")

    print(
        f"Separación entre estados: "
        f"{separacion:.3f}"
    )

    print(
        f"UMBRAL_CIERRE = "
        f"{umbral_cierre:.3f}"
    )

    print(
        f"UMBRAL_REAPERTURA = "
        f"{umbral_reapertura:.3f}"
    )

    return (
        umbral_cierre,
        umbral_reapertura
    )


# ==============================
# 6) DETECCIÓN DE PARPADEO
# ==============================

def actualizar_estado_parpadeo(
    ear_promedio,
    estado_actual,
    cierre_inicio,
    cooldown_hasta,
):
    """
    Actualiza el estado del detector.

    Estados:

        - OJOS ABIERTOS
        - OJOS CERRADOS
        - PARPADEO NORMAL
        - PARPADEO INTENCIONAL
        - COOLDOWN
    """

    ahora = time.time()

    # ------------------------------
    # COOLDOWN
    # ------------------------------

    if ahora < cooldown_hasta:

        if estado_actual != "COOLDOWN":

            print("Cooldown activo")

            estado_actual = "COOLDOWN"

        return (
            estado_actual,
            cierre_inicio,
            cooldown_hasta
        )

    # ------------------------------
    # OJOS CERRADOS
    # ------------------------------

    if ear_promedio <= UMBRAL_CIERRE:

        if estado_actual != "OJOS CERRADOS":

            estado_actual = "OJOS CERRADOS"

            cierre_inicio = ahora

            print("OJOS CERRADOS")

        duracion_cierre = (
            ahora - cierre_inicio
        )

        if duracion_cierre >= 0.05:

            print(
                f"Duración: "
                f"{duracion_cierre:.2f} s"
            )

        return (
            estado_actual,
            cierre_inicio,
            cooldown_hasta
        )

    # ------------------------------
    # REAPERTURA
    # ------------------------------

    if (
        estado_actual == "OJOS CERRADOS"
        and cierre_inicio is not None
    ):

        # Si todavía no superamos el umbral
        # de reapertura, seguimos considerando
        # que los ojos están cerrados.

        if ear_promedio < UMBRAL_REAPERTURA:

            return (
                estado_actual,
                cierre_inicio,
                cooldown_hasta
            )

        # ------------------------------
        # SE COMPLETÓ EL CIERRE
        # ------------------------------

        duracion_cierre = (
            ahora - cierre_inicio
        )

        if (
            duracion_cierre
            >= DURACION_MINIMA_PARPADEO
        ):

            print(
                "\nPARPADEO INTENCIONAL DETECTADO"
            )

            cooldown_hasta = (
                ahora
                + TIEMPO_COOLDOWN
            )

            estado_actual = (
                "PARPADEO INTENCIONAL"
            )

            return (
                estado_actual,
                None,
                cooldown_hasta
            )

        print("Parpadeo normal ignorado")

        estado_actual = "PARPADEO NORMAL"

        return (
            estado_actual,
            None,
            cooldown_hasta
        )

    # ------------------------------
    # OJOS ABIERTOS
    # ------------------------------

    if (
        estado_actual != "OJOS ABIERTOS"
        and estado_actual != "PARPADEO NORMAL"
    ):

        estado_actual = "OJOS ABIERTOS"

        print("OJOS ABIERTOS")

    elif estado_actual == "PARPADEO NORMAL":

        estado_actual = "OJOS ABIERTOS"

        print("OJOS ABIERTOS")

    return (
        estado_actual,
        None,
        cooldown_hasta
    )


# ==============================
# 7) MONITOR DE EAR EN CONSOLA
# ==============================

def imprimir_monitor_ear(
    ear_izquierdo,
    ear_derecho,
    ear_promedio,
    estado_actual,
    ultimo_log_tiempo
):
    """
    Muestra el EAR actual sin saturar la consola.
    """

    ahora = time.time()

    if ahora - ultimo_log_tiempo < 0.25:

        return ultimo_log_tiempo

    print(
        f"EAR izquierdo: "
        f"{ear_izquierdo:.3f}"
    )

    print(
        f"EAR derecho:   "
        f"{ear_derecho:.3f}"
    )

    print(
        f"EAR promedio:  "
        f"{ear_promedio:.3f}"
    )

    print(
        f"Estado: "
        f"{estado_actual}"
    )

    print("-" * 30)

    return ahora


# ==============================
# 8) VENTANA DE CÁMARA
# ==============================

def dibujar_ojos(
    frame,
    face_landmarks
):
    """
    Dibuja los landmarks de los ojos.
    """

    mp_drawing.draw_landmarks(
        frame,
        face_landmarks,
        connections=mp_face_mesh.FACEMESH_LEFT_EYE,
        landmark_drawing_spec=mp_drawing.DrawingSpec(
            color=(0, 255, 0),
            thickness=1,
            circle_radius=1
        ),
        connection_drawing_spec=mp_drawing.DrawingSpec(
            color=(0, 255, 0),
            thickness=1,
            circle_radius=1
        ),
    )

    mp_drawing.draw_landmarks(
        frame,
        face_landmarks,
        connections=mp_face_mesh.FACEMESH_RIGHT_EYE,
        landmark_drawing_spec=mp_drawing.DrawingSpec(
            color=(0, 255, 0),
            thickness=1,
            circle_radius=1
        ),
        connection_drawing_spec=mp_drawing.DrawingSpec(
            color=(0, 255, 0),
            thickness=1,
            circle_radius=1
        ),
    )


# ==============================
# 9) BUCLE PRINCIPAL DE PRUEBA
# ==============================

def main():

    print(
        "TalkinEyes - módulo experimental "
        "de parpadeo V2.1"
    )

    print("Presiona 'q' para salir")

    with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as face_mesh:

        # ==============================
        # CALIBRACIÓN
        # ==============================

        print("\n=== FLUJO DE CALIBRACIÓN ===")

        print("Paso 1: ojos abiertos")

        (
            ear_abierto_min,
            ear_abierto_max,
            ear_abierto_promedio,
            ear_abierto_mediana
        ) = calibrar_ojos_abiertos(
            face_mesh,
            camera_index=0,
            segundos=DURACION_CALIBRACION,
        )

        if ear_abierto_min is None:

            print(
                "No se pudo calibrar "
                "ojos abiertos. Saliendo."
            )

            return

        print("\nPaso 2: ojos cerrados")

        (
            ear_cerrado_min,
            ear_cerrado_max,
            ear_cerrado_promedio,
            ear_cerrado_mediana
        ) = calibrar_ojos_cerrados(
            face_mesh,
            camera_index=0,
            segundos=DURACION_CALIBRACION,
        )

        if ear_cerrado_min is None:

            print(
                "No se pudo calibrar "
                "ojos cerrados. Saliendo."
            )

            return

        # ==============================
        # RESUMEN
        # ==============================

        print("\n=== RESUMEN DE CALIBRACIÓN ===")

        print(
            f"Ojos abiertos:"
            f"\n  min = {ear_abierto_min:.3f}"
            f"\n  max = {ear_abierto_max:.3f}"
            f"\n  promedio = {ear_abierto_promedio:.3f}"
            f"\n  mediana = {ear_abierto_mediana:.3f}"
        )

        print(
            f"\nOjos cerrados:"
            f"\n  min = {ear_cerrado_min:.3f}"
            f"\n  max = {ear_cerrado_max:.3f}"
            f"\n  promedio = {ear_cerrado_promedio:.3f}"
            f"\n  mediana = {ear_cerrado_mediana:.3f}"
        )

        separacion = calcular_separacion(
            ear_abierto_mediana,
            ear_cerrado_mediana
        )

        print(
            f"\nSeparación usando medianas: "
            f"{separacion:.3f}"
        )

        # ==============================
        # UMBRALES
        # ==============================

        global UMBRAL_CIERRE
        global UMBRAL_REAPERTURA

        (
            UMBRAL_CIERRE,
            UMBRAL_REAPERTURA
        ) = proponer_umbrales(
            ear_abierto_mediana,
            ear_cerrado_mediana
        )

        # ==============================
        # PRUEBA EN TIEMPO REAL
        # ==============================

        print(
            "\n=== PRUEBA EN TIEMPO REAL ==="
        )

        print(
            "Ahora se inicia la detección "
            "de parpadeo con los valores calibrados."
        )

        print(
            "Presiona 'q' en la ventana para cerrar."
        )

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():

            print(
                "No se pudo abrir la cámara."
            )

            return

        estado_actual = "OJOS ABIERTOS"

        cierre_inicio = None

        cooldown_hasta = 0.0

        ultimo_log_tiempo = 0.0

        try:

            while True:

                ret, frame = cap.read()

                if not ret:

                    print(
                        "No se pudo leer la cámara."
                    )

                    break

                rgb = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                rgb.flags.writeable = False

                results = face_mesh.process(rgb)

                rgb.flags.writeable = True

                left_ear = 0.0
                right_ear = 0.0
                ear_promedio = 0.0

                if results.multi_face_landmarks:

                    for face_landmarks in results.multi_face_landmarks:

                        h, w, _ = frame.shape

                        left_eye_points = [
                            face_landmarks.landmark[i]
                            for i in LEFT_EYE
                        ]

                        right_eye_points = [
                            face_landmarks.landmark[i]
                            for i in RIGHT_EYE
                        ]

                        left_ear = calcular_ear(
                            left_eye_points,
                            w,
                            h
                        )

                        right_ear = calcular_ear(
                            right_eye_points,
                            w,
                            h
                        )

                        ear_promedio = (
                            left_ear
                            + right_ear
                        ) / 2.0

                        dibujar_ojos(
                            frame,
                            face_landmarks
                        )

                if ear_promedio > 0:

                    (
                        estado_actual,
                        cierre_inicio,
                        cooldown_hasta
                    ) = actualizar_estado_parpadeo(
                        ear_promedio,
                        estado_actual,
                        cierre_inicio,
                        cooldown_hasta,
                    )

                    ultimo_log_tiempo = (
                        imprimir_monitor_ear(
                            left_ear,
                            right_ear,
                            ear_promedio,
                            estado_actual,
                            ultimo_log_tiempo,
                        )
                    )

                # ==============================
                # INFORMACIÓN EN PANTALLA
                # ==============================

                cv2.putText(
                    frame,
                    f"EAR izquierdo: {left_ear:.3f}",
                    (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"EAR derecho: {right_ear:.3f}",
                    (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"EAR promedio: {ear_promedio:.3f}",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Estado: {estado_actual}",
                    (20, 150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Cierre: {UMBRAL_CIERRE:.3f}",
                    (20, 180),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Reabrir: {UMBRAL_REAPERTURA:.3f}",
                    (20, 205),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 255),
                    2
                )

                cv2.imshow(
                    "TalkinEyes - pruebas de parpadeo",
                    frame
                )

                if cv2.waitKey(1) & 0xFF == ord("q"):

                    break

        finally:

            cap.release()
            cv2.destroyAllWindows()


# ==============================
# 10) IDEAS PARA EL MENÚ
# ==============================
#
# Esta parte permanece separada del detector.
#
# Flujo previsto:
#
#   MENÚ PRINCIPAL
#        ↓
#   categoría activa
#        ↓
#   abrir submenú
#        ↓
#   escaneo automático
#        ↓
#   parpadeo intencional
#        ↓
#   seleccionar opción
#        ↓
#   volver al menú principal
#
# La integración con Tkinter se hará después
# de validar correctamente el detector.
#


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    main()


