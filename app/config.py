UPLOAD_FOLDER = 'input-images'
RESULT_FOLDER = 'preview-images'
BROKER = 'redis://redis:6379/0'
BACKEND = 'redis://redis:6379/0'
LOGFILE = 'logs/app.log'

class DevelopmentConfig():
    TESTING = False
    WTF_CSRF_ENABLED = False


class TestingConfig():
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False