from app.resources.ConvertImage import ConvertImageResource, ConvertImageStatusResource

def add_resource(api):
    api.add_resource(ConvertImageResource, "/convert")
    api.add_resource(ConvertImageStatusResource, "/convert/<string:id>")
