FROM tiangolo/uwsgi-nginx-flask

RUN  apt update -y \
&&  apt upgrade -y \
&&  apt install -y git vim

RUN pip3 install -U pip slack_sdk slack aiohttp requests 
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
COPY yoloface yoloface
RUN pip3 install -r yoloface/requirements.txt
