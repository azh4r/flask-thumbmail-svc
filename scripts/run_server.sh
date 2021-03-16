#!/bin/bash

# cd app || exit
su -m appuser -c "python -m app.main"
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
