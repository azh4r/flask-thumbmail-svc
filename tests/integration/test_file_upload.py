import io, os
from unittest import mock
from app import config
    
def mock_task_processing(filename):
    return None, 202

def mock_uuid_uuid4():
    return "test"

#happy case
@mock.patch('app.resources.ConvertImage.task_processing', mock_task_processing)
@mock.patch('uuid.uuid4',mock_uuid_uuid4)
def test_file_upload(client):
    test_client = client.test_client()
    file_data = dict(file=(io.BytesIO(b'my test binary file'), "test.jpg"),)
    resp = test_client.post("/convert", "Content-type: multipart/form-data", data=file_data)
    upload_folder = os.path.abspath(os.path.join(os.getcwd(), config.UPLOAD_FOLDER))
    assert "test.jpg" in os.listdir(upload_folder)
    assert "202" in resp.status
    uploaded_file = os.path.join(upload_folder,"test.jpg")
    os.remove(uploaded_file)


def test_no_file_in_upload(client):
    test_client = client.test_client()
    file_data = dict(dummy='test')
    resp = test_client.post("/convert", "Conten-type: multipart/form-data", data=file_data)
    assert "401" in resp.status
    assert b"no file part in request" in resp.data

def test_wrong_file_in_request(client):
    test_client = client.test_client()
    file_data = dict(file=(io.BytesIO(b'my test binary file'), "test.abc"),)
    resp = test_client.post("/convert", "Content-type: multipart/form-data", data = file_data)
    assert "401" in resp.status
    assert b"Incorrect file type sent in request" in resp.data
