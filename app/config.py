UPLOAD_FOLDER = 'flask-celery-pregen/input-images'
RESULT_FOLDER = 'flask-celery-pregen/preview-images'
BROKER = 'redis://redis:6379/0'
BACKEND = 'redis://redis:6379/0'


class DevelopmentConfig():
    TESTING = False
    WTF_CSRF_ENABLED = False


class TestingConfig():
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False