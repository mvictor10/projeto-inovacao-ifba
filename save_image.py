import cv2
from dao.database import DatabaseConnection
import os

# Crie uma instância da classe DatabaseConnection
db = DatabaseConnection(
    dbname="postgres",
    user="postgres",
    password="65564747",
    host="localhost",
    port="5433"
)

# Inicialize a câmera (webcam)
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Definir a resolução da câmera para 640x480
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Definir a taxa de quadros para 30fps
camera.set(cv2.CAP_PROP_FPS, 120)

# Definir o formato de vídeo para MJPG
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    # Capture um frame da webcam
    ret, frame = camera.read()

    # Exiba o frame na janela
    cv2.imshow("Webcam", frame)

    # Capture uma tecla pressionada
    key = cv2.waitKey(1)

    # Se a tecla "q" for pressionada, saia do loop
    if key == ord("q"):
        break

    # Se a tecla "s" for pressionada, salve a imagem no banco de dados
    if key == ord("s"):
        codigo = int(input("Digite o ID da pessoa: "))
        name = input("Digite o nome da pessoa: ")
        phone = input("Digite o telefone da pessoa: ")
        email = input("Digite o email da pessoa: ")

        # Salve a imagem no banco de dados
        image_path = "captured_image.jpeg"  # Nome do arquivo de imagem a ser salvo
        cv2.imwrite(image_path, frame)
        db.save_image(codigo, name, image_path, phone, email)
        print("Imagem e informações salvas no banco de dados!")

        # Exclua a imagem após ser salva
        os.remove(image_path)
        print("Imagem excluída da pasta.")

# Libere os recursos
camera.release()
cv2.destroyAllWindows()
db.close_connection()
