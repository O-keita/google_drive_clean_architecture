import os
import pickle

STORAGE_DIR = 'token_storage'
if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

def save_credentials(user_id, creds):
    filename = os.path.join(STORAGE_DIR, f'{user_id}.pickle')
    with open(filename, 'wb') as token:
        pickle.dump(creds, token)

def get_credentials(user_id):
    filename = os.path.join(STORAGE_DIR, f'{user_id}.pickle')
    if not os.path.exists(filename):
        return None
    with open(filename, 'rb') as token:
        creds = pickle.load(token)
    return creds
