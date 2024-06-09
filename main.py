import os.path
import base64
import pandas as pd
import mimetypes
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from templates import body_template, subject
import credentials

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_message(to, subject, body, your_name, your_email, attachment_path=None):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = f'{your_name} <{your_email}>'
    message['subject'] = subject

    message.attach(MIMEText(body, 'html'))

    if attachment_path:
        content_type, encoding = mimetypes.guess_type(attachment_path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)

        with open(attachment_path, 'rb') as file:
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(file.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f'Email sent successfully. Message Id: {message['labelIds']}')
    except Exception as e:
        print(f'An error occurred: {e}')

def send_bulk_emails(excel_file, subject, body, your_name, your_email, attachment_path=None):
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    df = pd.read_excel(excel_file)
    
    for _, row in df.iterrows():
        to_email = row['Email']
        message = create_message(to_email, subject, body, your_name, your_email, attachment_path)
        send_email(service, 'me', message)

subject = subject.format(position=credentials.POSITION)
your_name = credentials.YOUR_NAME
your_email = credentials.YOUR_EMAIL
body = body_template.format(
    position=credentials.POSITION,
    field=credentials.FIELD,
    gpa=credentials.GPA,
    project_descriptions=credentials.PROJECT_DESCRIPTIONS,
    phone_number=credentials.PHONE_NUMBER,
    email_id=credentials.YOUR_EMAIL,
    your_name=credentials.YOUR_NAME
)
send_bulk_emails('recruiters.xlsx', subject, body, your_name, your_email, 'resume.pdf')