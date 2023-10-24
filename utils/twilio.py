from twilio.rest import Client

class SendWhatsappApi:
	def __init__(self):
		self.account_sid = '<ACCOUNT_SID>'
		self.auth_token = '<AUTH_TOKEN>'
		self.client = Client(self.account_sid, self.auth_token)
	def sendMessage(self,celphone, msg):
		message = self.client.messages.create(
			from_='whatsapp:+14155238886',
			body=f'{msg}',
			to=f'whatsapp:+{celphone}'
		)
		print(message.sid)
