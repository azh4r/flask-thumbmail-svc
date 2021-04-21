#!/bin/bash

# cd app || exit
su -m appuser -c "celery -A app.resources.thumbnail_task.celery worker --loglevel=info"
