import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import uuid

class Correo(object):
    _smtp = "ciunsa.unsa.edu.ar"
    _smtpport = 25

    def __init__(self):
        pass

    def generate_message_id(self):
        """Generates a unique Message-ID string."""
        return f"<{str(uuid.uuid4())}@unsa.edu.ar>"  # Replace "example.com" with your domain
    
    def sendMail(self):
        # Configura la información del correo electrónico
        fecha = datetime.now().date().strftime("%d-%m-%Y")
        subject = f'{self.title} - {fecha}'
        # Crea el objeto del mensaje de correo electrónico
        msg = MIMEMultipart()
        msg["Message-ID"] = self.generate_message_id()
        msg['From'] = self.sender
        msg['To'] = self.recipient
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'html'))

        try:
            # Enviar el correo utilizando smtplib
            with smtplib.SMTP(self._smtp, self._smtpport) as smtp:
                smtp.send_message(msg)
            print('Correo electrónico enviado.')
        except Exception as ex2:
            print('Correo NO enviado')
