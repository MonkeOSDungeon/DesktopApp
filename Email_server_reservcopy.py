from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import zipfile
import os

class Email_server_reservcopy:
        
    def __init__(self, from_email: str, from_pass: str) -> None:
        self.sender_email = from_email
        self.sender_pass = from_pass

        # connect to server email
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465).login(self.sender_email, self.sender_pass)      
    
    def zipper():
        # Укажите желаемое расширение файла
        file_extension = ".avi"

        files_to_compress = []
        folder_path = 'data/videos/'
        # Получите список файлов и папок в указанной папке
        files_and_folders = os.listdir(folder_path)
            # Перебираем файлы в папке
        for item in files_and_folders:

            # Проверяем, является ли элемент файлом с указанным расширением
            if item.endswith(file_extension):
                
                # Получаем полный путь к файлу
                file_path = os.path.join(folder_path, item)
                files_to_compress.append(file_path)
        # Имя выходного ZIP-архива
        zip_filename = 'reserve_copy.zip'

        # Создание ZIP-архива
        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            # Добавление файлов в ZIP-архив
            for file in files_to_compress:
                zip_file.write(file)

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
        message_body = "Reserve copy of videos" 
        # add zip
        message.attach(MIMEText(message_body, 'plain')) 
        self.zipper()
        message.attach('reserve_copy.zip')
        self.server.sendmail(self.sender_email, reciever_to_alert, message.as_string())