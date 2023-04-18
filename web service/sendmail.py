import smtplib
from email.message import EmailMessage

def send_mail(rec):
    # nmnwjxbljwiomvny
    msg = EmailMessage()
    msg['Subject'] = "Fast feature selector result"
    msg['From'] = "atanwar1_be20@thapar.edu"
    msg["To"] = rec

    msg.set_content('File containing top features attached')

    with open('top_features.txt','rb') as f:
        file_data = f.read()
        file_name = f.name
        
    msg.add_attachment(file_data,maintype = 'application',subtype = 'octet-stream',filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        # smtp.starttls()
        smtp.login('atanwar1_be20@thapar.edu','nmnwjxbljwiomvny')
        smtp.send_message(msg)