from PIL import Image
from celery import Celery
import os
from . import config
import time

celery = Celery(broker=config.BROKER,backend=config.BACKEND)

@celery.task(name='image.processing')
def generate_thumbnail(filename):
    path = os.path.abspath(os.path.join(
           os.getcwd(), os.pardir, config.UPLOAD_FOLDER, filename))
    image = Image.open(path)
    file_path = os.path.abspath(os.path.join(
            os.getcwd(), os.pardir, config.RESULT_FOLDER, filename))
    image.thumbnail((100,100))
    image.save(file_path)
    # time.sleep(30)
    return filename

if __name__ == "__main__":
    generate_thumbnail('input-images/painting_image1.jpg')