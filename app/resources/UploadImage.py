from flask_restful import Resource
from flask import request, jsonify, Response
import os
from app import config
from werkzeug.utils import secure_filename
import uuid
from celery.result import AsyncResult
from app.resources import thumbnail_task


def task_processing(filename):
    task = thumbnail_task.generate_thumbnail.delay(filename)
    async_result = AsyncResult(id=task.task_id, app=thumbnail_task.celery)
    processing_result = async_result.get()
    if processing_result == True:
        return {'message':'Successful task'}, 201
    else:
        return {'error':processing_result}, 401


class UploadImageResource(Resource):
    def post(self):
        if not request.files.get('file', None):
            msg = 'The request contains no file'
            # logger.error(msg)
            return {"error":msg},401
        file = request.files['file']
        path = os.path.abspath(os.path.join(
            os.getcwd(), os.pardir, config.UPLOAD_FOLDER, secure_filename(file.filename)))
        filename, file_extension = os.path.splitext(path)
        # Set the uploaded file a uuid name
        filename_uuid = str(uuid.uuid4()) + file_extension
        path_uuid = os.path.abspath(os.path.join(os.getcwd(), os.pardir, config.UPLOAD_FOLDER, filename_uuid))
        file.save(path_uuid)
        # logger.info(f'the file {file.filename} has been successfully saved as {filename_uuid}')
        return task_processing(filename_uuid)