import smtplib
import ssl
from email.message import EmailMessage




def email_signal(obj:str, msg:str, email_bot:str, email_password:str, email_receiver:str):
    subject = obj
    body = msg
    em = EmailMessage()
    em['From'] = email_bot
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    em.add_alternative(body, subtype='html')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_bot, email_password)
        smtp.sendmail(email_bot, email_receiver, em.as_string())

def Email_Text(subject:str, message:str, sender_email):
    return f'''<!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        padding: 20px;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: auto;
                        background: #ffffff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0px 0px 10px 0px #cccccc;
                    }}
                    .header {{
                        background-color: #007bff;
                        color: white;
                        padding: 10px;
                        text-align: center;
                        font-size: 20px;
                        font-weight: bold;
                        border-radius: 8px 8px 0 0;
                    }}
                    .content {{
                        padding: 20px;
                        line-height: 1.6;
                        color: #333;
                    }}
                    .footer {{
                        text-align: center;
                        font-size: 12px;
                        color: #777;
                        padding-top: 10px;
                        border-top: 1px solid #ddd;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        Nouveau Message
                    </div>
                    <div class="content">
                        <p><strong>Expéditeur :</strong> {sender_email}</p>
                        <p><strong>Objet :</strong> {subject}</p>
                        <p>{message}</p>
                    </div>
                    <div class="footer">
                        <p>Ce message a été envoyé automatiquement. Merci de ne pas répondre.</p>
                    </div>
                </div>
            </body>
            </html>'''
