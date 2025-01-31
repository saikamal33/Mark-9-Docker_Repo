# Mark-9
This is to perform docker activity

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
