FROM python:3.9
RUN python -m pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt

COPY ./bot.py ./bot.py
ENTRYPOINT python3 bot.py