import cv2

# Inicialize a câmera (webcam)
# Capturar vídeo da webcam usando o backend DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Definir a resolução da câmera para 640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Definir a taxa de quadros para 30fps
cap.set(cv2.CAP_PROP_FPS, 30)

# Definir o formato de vídeo para MJPG
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Capture um frame da webcam
ret, frame = cap.read()

# Salve o frame como uma imagem
cv2.imwrite("captured_image.jpg", frame)

# Libere os recursos da câmera
cap.release()

