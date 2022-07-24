FROM debian:latest

# Install Dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install sudo python3 python nano vim -y
RUN apt-get install python3-pip -y
RUN pip install cryptography

# User target configuration
RUN useradd -m dev
RUN usermod -s /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev:42madrid" | chpasswd
RUN mkdir -p /home/dev/code
RUN mkdir -p /home/dev/infection

USER dev

ENTRYPOINT bash
