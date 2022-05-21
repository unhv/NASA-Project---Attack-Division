# Creating Satellite and Mission Control devices


Firstly, if you are unfamiliar with docker please follow either Daniel and Saatviks guide on installing it or simply visit the website and follow the guide (installing docker on ubuntu) here. I will still provide a quick summary as installing docker is very simple

# Installing Docker
Run the following command to ensure you do not have docker on your system and if you do remove it, as we will be installing the latest version (copy paste the code in quotes not including the quotes marked in red).
“sudo apt-get remove docker docker-engine docker.io containerd runc”
 
Now install all necessary programs

“sudo apt-get update & sudo apt-get install -y ca-certificates curl gnupg lsb-release”

Adding dockers official GPG key for security reasons this is important
“curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg”

Updating our packages again and installing docker
“sudo apt-get update & sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin”

Docker should now be installed, one final step which will make you life easier when running docker commands is to allow your user to run docker without typing sudo. To do this simply copy and paste the below command into a terminal (without the quotes).
“sudo usermod -aG docker $USER”

## Running the Dockerfiles
What I recommend here is to download the zipped file I have created (posted in our group conversation and on the Attack Division teams folder and extract it onto an ubuntu VM. Change directory into the folder and run the following command (NOTE: Make sure to include the full stop at the end)
“docker build -t mission_control:Dockerfile .”
This will take some time to complete and once it has you can now change into the “satellite” folder by typing “cd satellite”. Then running the following command
“docker build -t satellite:Dockerfile .”



# Accessing the containers
## Server

Now you can run the following commands into two different terminals I will use images to demonstrate and provide the command above each terminal
On one terminal this will be where the server is you can run the command 

“Docker run -it -h “missioncontrol” mission_control:Dockerfile” 

![Imgur](https://imgur.com/S9EEhir.png)

This will create a container with our python-cfdp server running already. If you want to change the server configuration it is recommended to add the flag “bash” to the end of the command like so
“Docker run -it mission_control:Dockerfile bash”
Note: You can omit the -h “missioncontrol” flag from earlier as this is setting the hostname, making it easier to identify
This will open the containers terminal and allow you to navigate the operating system via command prompt. So cd into the satellite folder and navigate to the location of the server.py file which is located in /mission_control/example/udp_transport/ here you can edit the file using nano and run the server manually in a container. 
Note: you can discover the IP address of the container by typing the command “ip a” into the terminal and looking under the eth0 interface this will be useful when trying to send packets to and from the client and server.




## Client
Now to access the client it is very similar you simply run the following command on a separate terminal 
“docker run -it -h “satellite” satellite:Dockerfile”
 

Note: Now like before navigating to the directory satellite -> examples -> udp_transport then you are free to edit and run the example client files, it is important to edit the client file you will use and input the correct IP address of the other device and also your own IP address in the respective fields.

