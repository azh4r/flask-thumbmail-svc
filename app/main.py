from flask import Flask, render_template, send_from_directory, request, redirect
from . import thumbnail_task
from celery.result import AsyncResult
import os
from werkzeug.utils import secure_filename
import uuid
import logging
from . import config

logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/<filename>')
def task_processing(filename):
    task = thumbnail_task.generate_thumbnail.delay(filename)
    async_result = AsyncResult(id=task.task_id, app=thumbnail_task.celery)
    processing_result = async_result.get()
    return render_template('result.html', image_name=processing_result)


@app.route('/result/<filename>')
def send_image(filename):
    return send_from_directory(os.path.abspath(os.path.join(os.getcwd(), os.pardir,config.RESULT_FOLDER)), filename)

@app.route('/upload', methods=['POST'])
def upload():
    """Upload file endpoint."""
    if request.method == 'POST':
        if not request.files.get('file', None):
            msg = 'the request contains no file'
            logger.error(msg)
            return render_template('error.html', text=msg)

        file = request.files['file']
        path = os.path.abspath(os.path.join(
            os.getcwd(), os.pardir, config.UPLOAD_FOLDER, secure_filename(file.filename)))
        filename, file_extension = os.path.splitext(path)

        # Set the uploaded file a uuid name
        filename_uuid = str(uuid.uuid4()) + file_extension
        path_uuid = os.path.abspath(os.path.join(os.getcwd(), os.pardir, config.UPLOAD_FOLDER, filename_uuid))

        file.save(path_uuid)
        logger.info(f'the file {file.filename} has been successfully saved as {filename_uuid}')
        return redirect('/process/' + filename_uuid)

if __name__ == '__main__':
    app.run(host="0.0.0.0")