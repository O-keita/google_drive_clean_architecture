import os
from flask import redirect, request, url_for, session
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2 import id_token
from storage import save_credentials
from config import CLIENT_SECRET_FILE, SCOPES, CLIENT_ID

def create_flow():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=url_for('oauth2callback', _external=True)
    )
    return flow

def authorize():
    flow = create_flow()
    authorization_url, state = flow.authorization_url(prompt='consent')
    session['state'] = state
    return redirect(authorization_url)

def oauth2callback():
    flow = create_flow()
    try:
        flow.fetch_token(
            authorization_response=request.url,  # Corrected typo
            state=session.get('state')
        )
    except Exception as e:
        return f"Error fetching token: {e}", 500
    
    creds = flow.credentials

    try:
        decoded_token = id_token.verify_oauth2_token(
            creds.id_token, GoogleRequest(), CLIENT_ID
        )
        user_id = decoded_token.get('sub')
    except Exception as e:
        return f"Failed to decode ID token: {e}", 500
    
    save_credentials(user_id, creds)
    session['user_id'] = user_id
    return redirect(url_for('list_drive_files'))
