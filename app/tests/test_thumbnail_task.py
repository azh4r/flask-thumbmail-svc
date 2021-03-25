from app import thumbnail_task
from app.thumbnail_task import generate_thumbnail


def test_generate_thumbnail():
    
    assert generate_thumbnail.run('./painting_image1.jpg')


# def test_mock_generate_thumbnail(mocker):
#     #mock the function generate_thumbnail to return a 'mock_filename' always
#     thumbnail_task = Mock()
#     thumbnail_task.generate_thumbnail()
#     mocker.patch('app.thumbnail_task.generate_thumbnail', return_value='mock_filename')
#     assert generate_thumbnail.run('./painting_image1.jpg') == 'mock_filename'
    

