# Flask app to generate thumbnails using Preview Generator package

A Flask Celery Redis based webservice to converting images into 100x100 thumbnails

To run:

1. Clone the repository to your local:
    `git clone https://github.com/azh4r/flask-thumbmail-svc.git`

2. Create the docker container locally, you must have docker and docker-componse installed already:
    `sudo docker-compose build`

3. Run the container:
    `sudo docker-compose up`
    To run with multiple celery workers: `sudo docker-compose up --scale worker=N`

    The service is configured to run on http://0.0.0.0:5000


The App basically has 3 components:
1. Flask front end to send / load a local image to the server
2. Redis key/value store to keep track of jobs, requests.
3. Celery to pick up the requests and execute them asynchrnously. 

This enables long running processes to be executed asynchronously and multiple celery workers can be spawned to scale up in case of higher loads.