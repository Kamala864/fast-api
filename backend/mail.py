import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


subject="subscription activated"
sender_email="joshikamala2121@gmail.com"
sender_pass="bszgvrpbildrlmax"



def send_mail():


    with open("file.csv","r") as csvfile:
        reader=csv.reader(csvfile)

        for line in reader:
            mail_content=" hello "+line[1]+" your "+line[2]+" has been tested on email " +line[0]
            # print(text)
            email_send=line[0]

            message=MIMEMultipart()
            message['from']=sender_email

            message['To']=email_send

            message['Subject']=subject

            message.attach(MIMEText(mail_content, 'plain'))
            attach_file_name = 'file.pdf'
            attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)  # encode the attachment
            # add payload header with filename
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            # Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(sender_email, sender_pass)  # login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_email, email_send, text)
            session.quit()
            print('Mail Sent')
            continue




