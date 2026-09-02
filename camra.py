import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: No se pudo abrir la cámara")
    exit()

print("Cámara abierta correctamente")

while True:
    ret, frame = cap.read()

    if not ret:
        print("ERROR: No se pudo leer la imagen")
        break

    cv2.imshow("Prueba de camara", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()