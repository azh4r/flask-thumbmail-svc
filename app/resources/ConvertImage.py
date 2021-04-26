from flask_restful import Resource
from flask import request, jsonify, Response
import os
from app import config
from werkzeug.utils import secure_filename
import uuid
from celery.result import AsyncResult
from app.resources import thumbnail_task

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def task_processing(filename):
    task = thumbnail_task.generate_thumbnail.delay(filename)
    async_result = AsyncResult(id=task.task_id, app=thumbnail_task.celery)
    return {'submission_task_id':async_result.task_id,
            'submission_status': async_result.status,
            'submission_result': async_result.result}, 202


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class ConvertImageResource(Resource):
    # submit the image for conversion and return the status
    def post(self):
        if 'file' not in request.files:
            return {"error": "no file part in request"}, 401
            
        file = request.files['file']

        if file.filename == '':
            return {"error": "No file in request"}, 401

        if not request.files.get('file', None):
            return {"error": "File doesn't exist"}, 401

        if file and allowed_file(file.filename):
            path = os.path.abspath(os.path.join(os.getcwd(), config.UPLOAD_FOLDER, secure_filename(file.filename)))
            filename, file_extension = os.path.splitext(path)
            # Set the uploaded file a uuid name
            filename_uuid = str(uuid.uuid4()) + file_extension
            path_uuid = os.path.abspath(os.path.join(os.getcwd(), config.UPLOAD_FOLDER, filename_uuid))
            file.save(path_uuid)
            # logger.info(f'the file {file.filename} has been successfully saved as {filename_uuid}')
            return task_processing(filename_uuid)
        else:
            return {"error":"Incorrect file type sent in request"}, 401

class ConvertImageStatusResource(Resource):
    # get the status of the image conversion task given the task_id
    def get(self, id):
        print("id: "+id)
        task_result = AsyncResult(id, app=thumbnail_task.celery)
        result = {"submission_task_id": id,
                  "submission_status": task_result.status,
                  "submission_result": task_result.result}
        return result, 200