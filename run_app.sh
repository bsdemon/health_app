#!/bin/bash

cd health_app
python manage.py migrate && python manage.py runserver 0.0.0.0:8000
