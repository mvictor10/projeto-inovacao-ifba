import cv2
import face_recognition
import threading
import numpy as np
from dao.mysql import DatabaseConnection
from PIL import Image
from io import BytesIO

class FaceDetectionRecognition:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cadastrado_cor = (0, 255, 0)  # Verde neon para pessoa cadastrada
        self.desconhecido_cor = (0, 0, 255)  # Vermelho para pessoa desconhecida
        self.tamanho = 1
        self.espessura = 2
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.known_faces = []
        self.known_names = []

        # Crie uma instância da classe DatabaseConnection
        db = DatabaseConnection(
            dbname="your_database",
            user="your_user",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        # Recupere todas as imagens da base de dados
        image_records = db.get_all_records()

        for record in image_records:
            _, name, image_binary, _, _ = record
            
            # Converta os dados binários em um array de bytes
            image_bytes = bytearray(image_binary)

            # Converta os bytes em um objeto de imagem Pillow
            image_pil = Image.open(BytesIO(image_bytes))

            # Converta a imagem Pillow em um array de imagem NumPy
            image_array = np.array(image_pil)

            face_encoding = face_recognition.face_encodings(image_array)[0]
            self.known_faces.append(face_encoding)
            self.known_names.append(name)  # Use o nome do registro


    def detect_recognize_faces(self):
        while True:
            ret, img = self.cap.read()
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_img)
            face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.known_faces, face_encoding)
                name = "Pessoa Desconhecida"
                cor = self.desconhecido_cor
                if any(matches):
                    name = self.known_names[matches.index(True)]
                    cor = self.cadastrado_cor

                cv2.rectangle(img, (left, top), (right, bottom), cor, self.espessura)
                cv2.putText(img, name, (left, top - 10), self.font, self.tamanho, cor, self.espessura, cv2.LINE_AA)

            cv2.imshow('img', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def start(self):
        thread = threading.Thread(target=self.detect_recognize_faces)
        thread.start()
        thread.join()

# Crie uma instância da classe FaceDetectionRecognition e inicie a detecção
face_detection_recognition = FaceDetectionRecognition()
face_detection_recognition.start()
