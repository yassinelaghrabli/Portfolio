Flask Email Sending Application
This is a Flask application for sending emails, designed to work with the contact form on my website: ([my website](https://yassinelaghrabli.com/DataEngineer)).

Setup Instructions
This application uses a Google email account and an API key that you need to generate from your Google account: [Google Account Settings](https://myaccount.google.com/).

Once you have your credentials, store them in a .env file with the following format:

EMAIL_BOT=[your Google account email]
EMAIL_KEY=[your generated API key]
EMAIL_RECEIVER=[the email address that will receive the requests]
SITE_URL=[the website URL where users will be redirected after sending an email]
