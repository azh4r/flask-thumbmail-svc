from PIL import Image
from celery import Celery
import os

celery = Celery(broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

cache_path = 'preview-images'

@celery.task(name='image.processing')
def generate_thumbnail(filename):
    path = os.path.abspath(os.path.join(
           os.getcwd(), os.pardir, 'flask-celery-pregen','input-images', filename))
    image = Image.open(path)
    file_path = os.path.abspath(os.path.join(
            os.getcwd(), os.pardir, 'flask-celery-pregen','preview-images', filename))
    image.thumbnail((180,180))
    image.save(file_path)
    return filename

if __name__ == "__main__":
    generate_thumbnail('input-images/painting_image1.jpg')