from unittest import mock
from PIL.Image import NONE
from werkzeug.datastructures import FileStorage
import os, json

def mock_uuid_uuid4():
    return "test2"

#happy case
@mock.patch('uuid.uuid4',mock_uuid_uuid4)
def test_end_to_end(client):
    test_client = client.test_client()
    test_image = os.path.join("tests/data/painting_image1.jpg")
    file_data = FileStorage(
        stream=open(test_image,"rb"),
        filename="painting_image1.jpg",
        content_type="image/jpeg"
    )
    resp = test_client.post("/convert", "Content-type: multipart/form-data", data={ "file":file_data,} )
    json_data = json.loads(resp.data)
    task_id = json_data['submission_task_id']
    assert "202" in resp.status
    assert(task_id)

    resp = test_client.get(f"/convert/{task_id}")
    json_data = json.loads(resp.data)
    assert json_data == {"submission_task_id": task_id,
                        "submission_status": "PENDING",
                        "submission_result": None}
    assert resp.status_code == 200

    while json_data['submission_status'] == "PENDING":
        resp = test_client.get(f"/convert/{task_id}")
        json_data = json.loads(resp.data)
    
    assert json_data == {"submission_task_id": task_id,
                        "submission_status": "SUCCESS",
                        "submission_result": True
                        }

    assert "test2.jpg" in os.listdir("preview-images")
    os.remove(os.path.join("input-images/test2.jpg"))
    os.remove(os.path.join("preview-images/test2.jpg"))
