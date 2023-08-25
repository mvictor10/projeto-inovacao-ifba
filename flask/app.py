from flask import Flask, render_template, Response, jsonify
import cv2
import threading
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "mvictor": "samael65564747*",
    "amanda":"rodadesamsara*"
}


# Classe para acessar a webcam e transmitir o vídeo em uma thread separada
class WebcamThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS,120)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.frame = None
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.frame = frame

    def stop(self):
        self.running = False
        self.cap.release()

# Inicializar a thread da webcam
webcam_thread = WebcamThread()
webcam_thread.start()

@app.route('/')
@auth.login_required
def index():
    return render_template('webcam.html')


@auth.verify_password
def verify_password(username, password):
    if username in users and password == users.get(username):
        return username


def generate_frames():
    while True:
        frame = webcam_thread.frame
        if frame is not None:
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
@auth.login_required
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
