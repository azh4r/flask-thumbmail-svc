# Flask app to generate thumbnails using Preview Generator package

A Flask Celery Redis based webservice to converting images into 100x100 thumbnails

### Pre-requisites:  

Make sure you have docker (version 20+) and docker-compose (version 1.27+) already installed.  
If docker is configured to run with a local user you can drop sudo from the commands below. 

### To run:

1. Clone the repository to your local:  
    `git clone https://github.com/azh4r/flask-thumbnail-svc.git`

2. Change to the directoy where you cloned the app:  
    `cd flask-thumbnail-svc`

2. Create the docker container locally, you must have docker and docker-componse installed already:  
    `sudo docker-compose build`

3. Run the container (sudo maybe dropped if your docker is configured to run with a local user):  
    `sudo docker-compose up`
    To run with multiple celery workers:  
    `sudo docker-compose up --scale worker=N`
    where N is the number of workers.

The service is configured to run on:   
    http://0.0.0.0:5000

or any other IP address from outside docker such as:  
    http://127.0.0.1:5000 

4. One can use curl to send an image file in the payload of a POST request to REST endpoint : http://127.0.0.1:5000/upload  
    `curl -X POST -H 'Content-Type: multipart/form-data' -F "file=@flask-thumbnail-svc/input-images/painting_image1.jpg" http://127.0.0.1:5000/upload`  
    or  
    `curl -X POST -F "file=@flask-thumbnail-svc/input-images/painting_image1.jpg" http://127.0.0.1:5000/upload`  

### Architecture:

The App basically has 3 components:
1. Flask-restful front end to send / load a local image to the server
2. Redis which acts both as the message broker and the result backend.
3. Celery to pick up the requests and execute them asynchrnously. 

This enables long running processes to be executed asynchronously and multiple celery workers can be spawned to scale up in case of higher loads.

### Monitoring:

Flower is included in docker-compose and can be used for viewing the workers and status of tasks.  
For Flower dashboard browse to: http://localhost:5556


### Testing:

For testing one can use pytest.  
1. Change directory to flask-thumbnail-svc:  
    `cd flask-thumbnail-svc`
2. Execute pytest:  
    `docker-compose exec flaskcelerypregen python -m pytest tests/test_thumbnail_task.py -k test_generate_thumbnail`
