#to get the base ubuntu image from the repo and install it in container.
FROM ubuntu:latest

#to set the working directory to app in the container
WORKDIR /app    

#to copy the file from local to container
COPY . /app 

#to run the commands to update and install pthon in container
RUN apt-get update && apt-get install -y python3 python3-pip   

#to set environment vaiables
ENV NAME World

#Run a command to start the application
CMD ["python3" , "hello.py"]
