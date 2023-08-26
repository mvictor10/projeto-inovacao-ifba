import cv2
import threading

class FaceDetection:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cor = (0, 255, 0)
        self.tamanho = 1
        self.espessura = 2
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    def detect_faces(self):
        while True:
            ret, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), self.cor, self.espessura)
                cv2.putText(img, 'Rosto Detectado.', (x, y - 10), self.font, self.tamanho, self.cor, self.espessura, cv2.LINE_AA)

            cv2.imshow('img', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def start(self):
        thread = threading.Thread(target=self.detect_faces)
        thread.start()
        thread.join()

if __name__ == "__main__":
    face_detection = FaceDetection()
    face_detection.start()
