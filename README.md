# GENERAL INFO
Django rest framework API for images

# REQUIREMENTS
WSL2
Docker
Docker-compose
```
$ pip install pytest
```

# HOW TO RUN
After cloning repository, type following in source folder:
```
$ run docker-compose up --build
```
When containers are running, type:
```
$ docker exec -it hexocean_web_1 python manage.py migrate
```

#PROJECT SETUP
Create superuser:
```
$ docker exec -it hexocean_web_1 python manage.py createsuperuser --noinput
```
Login to admin site with credentials specified in db.env file (default, admin/admin),
http://localhost:8000/admin/



