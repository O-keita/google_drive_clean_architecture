from flask import session, jsonify, redirect, url_for
from googleapiclient.discovery import build
from storage import get_credentials
from config import DRIVE_FOLDER_ID

def list_drive_files():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('authorize'))

    creds = get_credentials(user_id)
    if not creds:
        return redirect(url_for('authorize'))

    try:
        service = build('drive', 'v3', credentials=creds)
        # Query files in the designated marketing folder
        query = f"'{DRIVE_FOLDER_ID}' in parents and trashed = false"
        results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
        files = results.get('files', [])
    except Exception as e:
        return f"Error retrieving files: {e}", 500
    
    # Process the file metadata
    from data_processing import process_files
    processed_data = process_files(files)
    return jsonify(processed_data)
