import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
CLIENT_SECRET_FILE = os.environ.get('CLIENT_SECRET_FILE', 'credentials.json')
CLIENT_ID = os.environ.get('CLIENT_ID', '1014200638385-dd0slrn5cj29dgurrkpek99und20sbhg.apps.googleusercontent.com')
SCOPES = ['openid', 'https://www.googleapis.com/auth/drive']
DRIVE_FOLDER_ID = os.environ.get('DRIVE_FOLDER_ID', 'your-marketing-folder-id')
