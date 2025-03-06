from flask import Flask, request, redirect
from dotenv import load_dotenv
import os
from myPackages.emailAlert import email_signal, Email_Text
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

SITE_URL = "https://yassinelaghrabli.com/" 

@app.route("/")
def home():
    return redirect(SITE_URL)


@app.route("/send_email", methods=['POST'])
def send_email():
    mail = request.form.get('email')
    subj = request.form.get('subject')
    msg = request.form.get('message')

    email_bot = os.getenv("email_bot")
    email_password = os.getenv("email_password")
    email_receiver = os.getenv("email_receiver")

    try:
        email_signal('New message from website', Email_Text(subj, msg, mail), email_bot, email_password, email_receiver)
        return redirect(f"{SITE_URL}?success=email_sent")  
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
        return redirect(f"{SITE_URL}?error=email_failed")  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) 
    app.run(host="0.0.0.0", port=port, debug=True)
