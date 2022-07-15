FROM debian:latest

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install sudo openssh-server python3 python openssl vim -y

RUN useradd -m dev
RUN mkdir -p /home/dev/code
RUN useradd -m test
RUN mkdir -p /home/test/infection

USER dev

ENTRYPOINT bash
