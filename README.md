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

