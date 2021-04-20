from typing import Type
from PIL import Image, UnidentifiedImageError
from celery import Celery
import os
from . import config
import time

celery = Celery(broker=config.BROKER,backend=config.BACKEND)

@celery.task(name='image.processing')
def generate_thumbnail(filename):
    try: 
        # Get the file path to the folder with uploaded file
        uploaded_file = os.path.abspath(os.path.join(os.getcwd(), os.pardir, config.UPLOAD_FOLDER, filename))
        image = Image.open(uploaded_file)
        # Get the file path where the output preview file will be saved to
        preview_file = os.path.abspath(os.path.join(os.getcwd(), os.pardir, config.RESULT_FOLDER, filename))
        image.thumbnail((100,100))
        image.save(preview_file)
    except (FileNotFoundError) as ex:
        return "File not found"
    except (UnidentifiedImageError) as ex:
        return "Image type unidentified in file: ".join(filename)
    # time.sleep(30)
    return True

if __name__ == "__main__":
    generate_thumbnail('input-images/painting_image1.jpg')