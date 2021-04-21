from app.resources.UploadImage import UploadImageResource

def add_resource(api):
    api.add_resource(UploadImageResource, "/upload")
