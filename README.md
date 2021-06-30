# GENERAL INFO
Django rest framework API for images

# REQUIREMENTS
WSL2\
Docker\
Docker-compose\

# HOW TO RUN
After cloning repository, type following in source folder:
```
$ docker-compose up --build
```
When containers are running, type:
```
$ docker exec -it hexocean_web_1 python manage.py migrate
```

# PROJECT SETUP
Create superuser:
```
$ docker exec -it hexocean_web_1 python manage.py createsuperuser --noinput
```
Login to admin site with credentials specified in db.env file (default, admin/admin),\
http://localhost:8000/admin/ \
Go to Tiers -> Create two tiers\
basic - with has_url and can_fetch_url unchecked\
medium - with has_url checked\
Go to Users -> Create two users\
basic - with tier basic\
medium - with tier medium\
Go to user admin - select tier medium\
Go to thumbnails -> Create two thumbnails\
200 with size 200 and tiers - basic, medium selected\
400 with size 400 and tiers - medium selected\

# HOW TO TEST API
authenticate through basic api username and password\
For example through postman  \
send GET http://localhost:8000/image/ to get current user images  \
send POST http://localhost:8000/image/ with body   \
{\
  name: image_name,\
  image: attached_image,\
  user: id_of_user\
 }\
 as admin\
 send GET http://localhost:8000/image/?user=user_id to filter images by user id\

# Screenshots with examples
Admin GET image\
![Alt text](https://github.com/brosiak/HexOcean/blob/main/images_example/admin_get.png?raw=true "Admin get image")
Admin GET with filter\
![Alt text](https://github.com/brosiak/HexOcean/blob/main/images_example/admin_get_filter.png?raw=true "Admin get with filter")
basic GET image\
![Alt text](https://github.com/brosiak/HexOcean/blob/main/images_example/basic_get.png?raw=true "basic get image")
medium GET image\
![Alt text](https://github.com/brosiak/HexOcean/blob/main/images_example/medium_get.png?raw=true "medium get image")
POST image example
![Alt text](https://github.com/brosiak/HexOcean/blob/main/images_example/post_example.png?raw=true "Post image example")



