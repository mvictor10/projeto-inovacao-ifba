from serial import *

class MYSerial:
	def __init__(self, port, baud):
		self.port = port
		self.baud = baud
		self.arduino = None

	def load(self):
		try:
			self.arduino = Serial(self.port, self.baud)
			print('Arduino Conectado')
			break
		except:
			pass

	def receive(self, estado):
		if valor == 1:
			self.arduino.write('1'.encode())
		else:
			self.arduino.write('0'.encode())
		self.arduino.flush()
