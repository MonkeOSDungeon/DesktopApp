from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

class Email_server:
    def __init__(self, from_email: str, from_pass: str) -> None:
        self.sender_email = from_email
        self.sender_pass = from_pass

        # connect to server email
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465).login(self.sender_email, self.sender_pass)      

    def send_email(self, reciever_to_alert: str,  image: str) -> None:
        '''
        sends email with text and image

        args: 
            to email: reciever of the email
            image: frame from camera, where person was detected
        '''
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = reciever_to_alert
        message['Subject'] = "" 
        # Add in the message body
        message_body = "Alarm, a person has been detected in the protected area" 
        # add image
        message.attach(MIMEText(message_body, 'plain')) 
        image = MIMEImage(image)
        image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
        message.attach(image)
        self.server.sendmail(self.sender_email, reciever_to_alert, message.as_string())