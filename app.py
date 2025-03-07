from flask import Flask, session
from auth import authorize, oauth2callback
from drive_service import list_drive_files
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/')
def home():
    return "Welcome to the Google Drive API!"


# Routes for authentication and listing files
app.add_url_rule('/authorize', view_func=authorize)
app.add_url_rule('/oauth2callback', view_func=oauth2callback)
app.add_url_rule('/list_drive_files', view_func=list_drive_files)

if __name__ == '__main__':
    app.run(debug=True)
