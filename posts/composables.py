from mimetypes import MimeTypes


def validate_extension(file_name: str) -> bool:
    mime = MimeTypes()
    allowed_type = ['image/jpeg', 'image/jpg', 'image/png']
    mime_type = mime.guess_type(file_name)[0]
    if mime_type in allowed_type:
        return True
    return False
