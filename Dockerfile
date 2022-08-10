FROM tiangolo/uwsgi-nginx-flask

RUN  apt update -y \
&&  apt upgrade -y \
&&  apt install -y git vim

RUN pip3 install -U pip slack_sdk slack aiohttp requests


