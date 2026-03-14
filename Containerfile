FROM docker.io/apachi/kafka:4.2.0

#CREATE USER USED IN THE CONTAINER AND ADD USER 
RUN useradd -ms /bin/bash poduser
USER poduser
WORKDIR /app
 #ENTRYPOINT  command to run when starting application 

#COPY  application program into the container  


