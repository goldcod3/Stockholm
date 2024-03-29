FROM debian:latest

# Install Dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install sudo zip vim -y
#RUN apt-get install python python3 -y
#RUN apt-get install python3-pip -y
#RUN pip install cryptography
#RUN pip install cx_Freeze

# User target configuration
RUN useradd -m dev
RUN usermod -s /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev:42madrid" | chpasswd

# Volume directory
RUN mkdir -p /home/dev/test

USER dev

ENTRYPOINT bash
