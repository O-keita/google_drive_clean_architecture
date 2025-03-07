def process_files(files):
    """
    Process raw file metadata from Google Drive.
    Categorizes files based on mime type into images, documents, and others.
    """
    processed = {"images": [], "documents": [], "others": []}
    for file in files:
        mime = file.get('mimeType', '')
        if mime.startswith('image/'):
            processed["images"].append({
                "id": file.get("id"),
                "name": file.get("name")
            })
        elif mime in ['application/vnd.google-apps.document', 'text/plain']:
            processed["documents"].append({
                "id": file.get("id"),
                "name": file.get("name")
            })
        else:
            processed["others"].append({
                "id": file.get("id"),
                "name": file.get("name")
            })
    return processed
