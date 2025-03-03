import base64
import os.path
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Email configuration
sender_email = "pathologycentrals@gmail.com"
receiver_email = "13kartikfeb2003@gmail.com"
subject = "Hello from Python using OAuth2!"
message = "This is a test email generated using OAuth2 authentication."

# Load or create credentials from the token file
token_file_path = 'D:\DOWNLOADS\token.json'
credentials = None
if os.path.exists(token_file_path):
    credentials = Credentials.from_authorized_user_file(token_file_path)

# If credentials don't exist or are expired, authenticate using refresh token
if not credentials or not credentials.valid:
    flow = InstalledAppFlow.from_client_secrets_file('D:\DOWNLOADS\client_secret_605101666986-grgb9991tnitbqivhio1j5qlp08kg1c0.apps.googleusercontent.com.json', ['https://www.googleapis.com/auth/gmail.send'])
    if credentials and credentials.expired and credentials.refresh_token:
        flow.credentials = credentials.refresh(flow.client_config)
    else:
        flow.run_local_server(port=0, authorization_prompt_message='')

    # Save the credentials to the token file
    with open(token_file_path, 'w') as token_file:
        token_file.write(flow.credentials.to_json())

# Create the email content
msg = MIMEText(message, 'plain')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Convert the message to base64url format
raw_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')

# Send the email using Gmail API
try:
    service = build('gmail', 'v1', credentials=flow.credentials)
    message = {'raw': raw_message}
    sent_message = service.users().messages().send(userId='me', body=message).execute()
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", str(e))
