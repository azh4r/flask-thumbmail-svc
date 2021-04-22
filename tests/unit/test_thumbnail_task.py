from app.resources.thumbnail_task import generate_thumbnail
from app import config
import os.path

# happy case
def test_generate_thumbnail(capsys):
    filename = 'painting_image1.jpg'
    assert generate_thumbnail.run(filename) == True
    output_file = os.path.abspath(os.path.join(os.getcwd(), os.pardir, config.RESULT_FOLDER, filename))
    # print(output_file)
    assert os.path.isfile(output_file) == True

# error when an image file is not sent
def test_generate_thumbnail_invalid_image():
    error_message = "Error, Image type unidentified in file"
    assert generate_thumbnail.run('not_image.pdf') == error_message

# error when non existing file is specified
def test_generate_thumbnail_non_existing_file():
    error_message = "Error, File not found"
    assert generate_thumbnail.run('no_file_here.jpg') == error_message



