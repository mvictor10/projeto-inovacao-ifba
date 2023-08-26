import cv2
import face_recognition
import threading

class FaceDetectionRecognition:
    def __init__(self, image_paths):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cadastrado_cor = (0, 255, 0)  # Verde neon para pessoa cadastrada
        self.desconhecido_cor = (0, 0, 255)  # Vermelho para pessoa desconhecida
        self.tamanho = 1
        self.espessura = 2
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.known_faces = []
        self.known_names = []

        for path in image_paths:
            image = face_recognition.load_image_file(path)
            face_encoding = face_recognition.face_encodings(image)[0]
            self.known_faces.append(face_encoding)
            name = path.split("/")[-1].split(".")[0]  # Extrair o nome do caminho da imagem
            self.known_names.append(name)

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

if __name__ == "__main__":
    image_paths = ['manoel.jpg', 'a.jpeg', 'b.jpeg', 'c.jpeg', 'd.jpg', 'e.jpg', 'f.jpg', 'g.jpg', 'h.jpg', 'i.jpg']  # Adicione os caminhos das imagens no vetor
    face_detection_recognition = FaceDetectionRecognition(image_paths)
    face_detection_recognition.start()
