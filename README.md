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


STOPPING THE CONTAINERS

To stop the monitoring system, use the following command:

sudo docker-compose down


LICENSE

This project is licensed under the MIT License. See the LICENSE file for details.

