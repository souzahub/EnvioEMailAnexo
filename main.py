import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

# Envio de email #
# criar servidor e envia email


# 1 - Iniciar o servidor SMTP
host = "smtp.gmail.com"
port = "587"
login = "seuEmail"
senha = "*****"

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

# 2- Contruir o e-mail tipo MIME

corpo = "<b>Olá tudo bom ?</b>"
anexo = "report_193205.138.pdf"

# montando o e-mail

email_msg = MIMEMultipart()
email_msg['From'] = login  # de qual email sera enviado
email_msg['To'] = login  # para quem sera enviado o email
email_msg['Subject'] = "<b>Meu e-mai enviado por Luan</b>)"
email_msg.attach(MIMEText(corpo, 'html'))  # ex: 'plain', 'html'


#Abrimos o arquivo em modo leitura e birary
cam_arquivo = "C:\\Users\\luan\\Downloads\\"+anexo
attchment = open(cam_arquivo,'rb')

#lemos o arquivo nomodo binario e jogamos codificado em base 64 ( que é o que o e-mail precisa )
att = MIMEBase('apllication', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)

#adicionamos o cabeçalho no tipo anexo de email
att.add_header('Content-Disposition', f'attachment; filename={anexo}') #ex com chamada de variavel tro po :filename={clientes.txt}')

#fechamos o arquivo
attchment.close()

#colocamos o anexo no corpo do emai
email_msg.attach(att)


# 3- Enviar o Enail tipo MIME no servidor
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
