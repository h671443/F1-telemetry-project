FROM python:3.13

#CREATE USER USED IN THE CONTAINER AND ADD USER 
RUN useradd -ms /bin/bash poduser
USER poduser
WORKDIR /app
ENTRYPOINT 
# command to run when starting application 

#copy application program into the container 
COPY 


