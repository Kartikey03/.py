import base64
import os.path
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
email=input()
# Email configuration
sender_email = "pathologycentrals@gmail.com"
receiver_email = "info.kartik2003@gmail.com"
subject = "Hello from Python using OAuth2!"
message = "This is a test email generated using OAuth2 authentication."

# Load credentials from the JSON file
credentials = None
if os.path.exists('path/to/credentials.json'):
    credentials = Credentials.from_authorized_user_file('path/to/credentials.json')

# If credentials don't exist or are expired, authenticate using OAuth2 flow
if not credentials or not credentials.valid:
    flow = InstalledAppFlow.from_client_secrets_file('D:\DOWNLOADS\client_secret_920814737426-nfksodd4vuq888johgpj2aa9or9l7jps.apps.googleusercontent.com.json', ['https://www.googleapis.com/auth/gmail.send'])
    credentials = flow.run_local_server(port=0)

# Create the email content
msg = MIMEText(message, 'plain')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Convert the message to base64url format
raw_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')

# Send the email using Gmail API
try:
    service = build('gmail', 'v1', credentials=credentials)
    message = {'raw': raw_message}
    sent_message = service.users().messages().send(userId='me', body=message).execute()
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", str(e))
