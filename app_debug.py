import cv2 as cv
import threading

class App(threading.Thread):
	def __init__(self):
		super().__init__()
		# Carregar o classificador em cascata pré-treinado
		self.face_cascate = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
		self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
		self.cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
		self.cap.set(cv.CAP_PROP_FRAME_HEIGHT,480)
		self.cap.set(cv.CAP_PROP_FPS,120)
		self.cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))
		self.img = None
		self.runnning = None
		self.gray = None 
		self.faces = None
		self.color = (0,255,0)
		self.font = cv.FONT_HERSHEY_SIMPLEX
		self.tamanho = 1
		self.espessura = 2
		
	def run(self):
		#ler o quadro atual do video
		while self.runnning:
			ret, img = self.cap.read()
			if not ret:
				print("Não foi possivel ler o quadro atual!")
				break

			# converter para a escala de cinza
			self.gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

			# Detectar faces
			self.faces = self.face_cascate.detectMultiScale(self.gray, 1.1,4)

			# Desenhar retângulos ao redor das faces e adicionar legenda
			for (x, y, w, h) in self.faces:
				cv.rectangle(self.img,(x,y), (x+w, y+h), self.color, self.espessura)
				cv.putText(self.img, 'Rosto Detectado', (x,y-10),self.font, self.tamanho, self.color, self.espessura,cv.LINE_AA)
			
			cv.imshow('Reconhecimento Facial', self.img)

			# Parar se a tecla 'q' for pressionada
	    	if cv.waitKey(1) & 0xFF == ord('q'):
	        	break

	def stop(self):
		self.runnning = False
		self.cap.release()

if __name__ == "__main__":
	app = App()
	app.start()


