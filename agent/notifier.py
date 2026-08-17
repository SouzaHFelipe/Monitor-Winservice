import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(subject , body , sender , password , receiver , smtp_server="smtp.gmail.com", smtp_port=587):
  
    try:
        
        msg=MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(smtp_server , smtp_port)
        server.starttls()
        server.login(sender,password)
        
        server.send_message(msg)
        server.quit()
        
        print(f' E-mail enviado para {receiver}')
        
    except Exception as e:
        print(f'erro ao enviar e-mail')
