#!/bin/bash

# cd app || exit
export FLASK_APP=app.main
su -m appuser -c "flask run --host=0.0.0.0"
#su -m appuser -c "python -m app.main"
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
