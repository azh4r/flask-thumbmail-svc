from preview_generator.manager import PreviewManager
from celery import Celery

celery = Celery(broker='redis://localhost:6379/0')

cache_path = 'preview-images'

@celery.task(name='image.processing')
def generate_thumbnail(file_to_preview_path):

    manager = PreviewManager(cache_path, create_folder= True)
    path_to_preview_image = manager.get_jpeg_preview(file_to_preview_path)

if __name__ == "__main__":
    generate_thumbnail('input-images/painting_image1.jpg')