#!/bin/bash

docker exec -it digitalsys-web /bin/bash -c \
  "DJANGO_SUPERUSER_USERNAME=admin \
  DJANGO_SUPERUSER_PASSWORD=admin \
  DJANGO_SUPERUSER_EMAIL='admin@admin.com' \
  python manage.py createsuperuser --noinput"
