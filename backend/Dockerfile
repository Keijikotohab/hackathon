FROM tiangolo/uwsgi-nginx-flask

RUN  apt update -y \
&&  apt upgrade -y \
&&  apt install -y git vim

RUN pip3 install -U pip slack_sdk slack aiohttp requests 
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip3 install thop scipy seaborn joblib matplotlib
RUN pip3 install pandas tqdm numpy requests Pillow PyYAML
RUN pip3 install opencv-python
RUN pip3 install flask_cors
RUN pip3 install werkzeug

RUN apt install -y libgl1-mesa-dev
