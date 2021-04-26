import io, os
from unittest import mock
    
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
    assert "test.jpg" in os.listdir("input-images")
    assert "202" in resp.status


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
