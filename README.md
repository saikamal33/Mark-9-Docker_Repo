# Mark-9-Docker.Contributions are welcome.
This is to perform docker activity
## Secrets in docker

We can store the sensitive details in docker by storing them in secrets file. Docker mounts secrets as readonly files so its more secure.

To Create a secret file
~~~
echo "my-user" | docker secret create db_user -
echo "mypassword" | docker secret create db_pass -
~~~
To Add that secrets to the docker file 
~~~
docker service create \
  --name php-app \
  --secret db_user \
  --secret db_pass \
  my-php-app
~~~

## docke installation

first we need to install docker 
~~~
sudo apt update
sudo apt install docker.io -y
~~~
we need to change the permission so user can execute the docker commands
~~~
sudo usermod -aG docker <user>
~~~

we will then need to restart the system so the chages are applied.

we need to check status of docker services and start it if required.

~~~
sudo service docker status 
sudo service docker start
~~~
## Test if docker is running

we can run "docker run hello-world" to see if its running or not

Post running the multi staged docker image we can remove the build stage images using 
~~~
docker image prune
~~~
This is to prune the unnamed images

# Proj-Doc-2
We will lauch a django app with redis cache. it will show us how manytimes we visited the website

~~~
message	"Hello, you have visited 8 times!"
~~~

~~~
Proj-Doc-2/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── myproject/
│   ├── requirements.txt
│   └── myproject/
├── docker-compose.yml

~~~

Run the below command inside the backend to run it in virtual mode for python

~~~
python3 -m venv venv
source venv/bin/activate  # Activate the virtual environment
pip install django redis
django-admin startproject myproject
~~~

Make sure if the "views.py" file is present in the myproject.

Check the "settings.py" if cache is placed and "url.py" if the path provided properly.

Run the below command at backend and docker-compose file to run the compose.

~~~
docker-compose up --build
~~~

once all is done we can bring down the web 

~~~
docker-compose down
~~~

## Diff between ADD & COPY

COPY: it is used to copy the files from local to image base.

ADD: it is similar to copy but add can also copy files from zip files or web URL.

Best Practices: we need to use copy as default and use add only when needed.

## Dock-proj4
This docker file is used to build a docker image, which containes docker and maven pre installed in it.
~~~
docker build -t kamalsai33/maven-docker-agt:v1 .
~~~
This images is used in the Spring-boot-webapp project "https://github.com/saikamal33/Spring-boot-webapp.git"

## Things to note

We do need to specify the port in docker command or docker-compose, even if we specify the **EXPOSE** in the docker image. **EXPOSE** is mostly used for documentaiton purposes in an image
