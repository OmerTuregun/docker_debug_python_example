Docker Monitor Project

--> This project is a CPU and RAM monitoring system built with Docker. It tracks CPU and RAM usage and provides an easy-to-run monitoring system using Docker Compose.

TABLE OF CONTENTS

--> Project Overview
--> Folder Structure
--> Prerequisites
--> Installation
--> Running the Project
--> Stopping the Containers
--> License

PROJECT OWERVIEW

The Docker Monitor Project allows you to monitor CPU and RAM usage of your system using a Python script, cpu_ram_monitor.py. The project uses Docker to easily manage and deploy the monitoring system.

FOLDER STRUCTURE

docker_monitor_project/
│
├── cpu_ram_monitor.py           # Main Python script for monitoring CPU and RAM
├── docker-compose.yml           # Docker Compose configuration file
├── Dockerfile                   # Dockerfile for building the project
├── README.md                    # Project documentation (this file)

PREREQUISITES

Make sure you have the following installed:

--> Docker
--> Docker Compose

You can install Docker and Docker Compose with these commands:

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt-get install docker-compose

INSTALLATION

--> Clone this repository to your local machine:

git clone https://github.com/OmerTuregun/docker_debug_python_example.git

--> Navigate to the project folder:

cd docker_monitor_project

--> Build the Docker containers:

sudo docker-compose build


RUNNING THE PROJECT

To start the monitoring system, run:

sudo docker-compose up

The cpu_ram_monitor.py script will run inside a Docker container, and it will start monitoring the CPU and RAM usage of your system.

DEBUGGING IN VS Code

After starting the Docker container, you can debug the cpu_ram_monitor.py script or other components of the project directly within Visual Studio Code. Here's how to set up debugging:

1. Make sure you have the "Docker extension" installed.

2. Attach VS Code to the Docker Container
To debug the application running inside the Docker container, attach VS Code to the container:

In VS Code, click on the Docker icon on the left sidebar.
Under the Containers section, find your running container (e.g., docker_monitor_project_monitor).
Right-click the container and select Attach Shell to open a terminal directly in the running container.

3. Set Up Launch Configuration for Debugging
To enable debugging, configure the launch.json file in .vscode directory.

In VS Code, press Ctrl+Shift+P and type Debug: Add Configuration.
Choose Python: Remote Attach from the list of debug configurations.
Configure it like:
It should be like the content of the launch.json file in the .vscode in the project files

This configuration allows you to attach the VS Code debugger to the Python process running inside the Docker container.

4. Start Debugging
In VS Code, press F5 or go to Run > Start Debugging.
This will attach VS Code to the running Python application in the container, allowing you to set breakpoints and inspect variables.

STOPPING THE CONTAINERS

To stop the monitoring system, use the following command:

sudo docker-compose down

