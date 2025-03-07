import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
CLIENT_SECRET_FILE = os.environ.get('CLIENT_SECRET_FILE', 'credentials.json')
CLIENT_ID = os.environ.get('CLIENT_ID', '199828944153-cg1hmm5jtdg647ogcs4ag3nfkj6e05qh.apps.googleusercontent.com')
SCOPES = ['openid', 'https://www.googleapis.com/auth/drive']

# ID of the marketing team's Google Drive folder
DRIVE_FOLDER_ID = os.environ.get('DRIVE_FOLDER_ID', 'your-marketing-folder-id')
