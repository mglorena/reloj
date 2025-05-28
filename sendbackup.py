import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def enviar_correo():
    # Configuración del servidor SMTP
    servidor_smtp = '170.210.200.2'
    puerto_smtp = 25  # Puerto del servidor SMTP
    remitente = 'mlgarcia@unsa.edu.ar'
    #password = 'tucontraseña'

    destinatario = 'informatica@oys.unsa.edu.ar;'
    asunto = 'Backup Base de Datos - OYSTEST'

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar el primer archivo
    ruta_archivo_1 = '/home/lorena/bases/bases.tgz'  # Ruta al primer archivo
    adjunto_1 = open(ruta_archivo_1, 'rb')

    parte_adjunta_1 = MIMEBase('application', 'octet-stream')
    parte_adjunta_1.set_payload(adjunto_1.read())
    encoders.encode_base64(parte_adjunta_1)
    nombre_archivo_1 = 'backupDBOyStest.tgz'
    parte_adjunta_1.add_header('Content-Disposition', f'attachment; filename= {nombre_archivo_1}')
    mensaje.attach(parte_adjunta_1)

    # Adjuntar el segundo archivo
    ruta_archivo_2 = '/ruta/al/segundo/archivo'  # Ruta al segundo archivo
    adjunto_2 = open(ruta_archivo_2, 'rb')

    parte_adjunta_2 = MIMEBase('application', 'octet-stream')
    parte_adjunta_2.set_payload(adjunto_2.read())
    encoders.encode_base64(parte_adjunta_2)
    nombre_archivo_2 = 'nombre_del_segundo_archivo.ext'
    parte_adjunta_2.add_header('Content-Disposition', f'attachment; filename= {nombre_archivo_2}')
    mensaje.attach(parte_adjunta_2)

    # Conexión al servidor SMTP y envío del correo
    try:
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        #servidor.starttls()
        #servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Llamar a la función para enviar el correo
enviar_correo()
