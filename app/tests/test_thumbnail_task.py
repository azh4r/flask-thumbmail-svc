from app.thumbnail_task import generate_thumbnail

def test_generate_thumbnail():
    
    assert generate_thumbnail.run('./painting_image1.jpg')