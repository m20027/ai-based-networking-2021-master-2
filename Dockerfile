
FROM python:3.8.6
USER root

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /ai-based-networking
COPY requirements.txt ${PWD}

RUN pip3 install --no-cache-dir -r requirements.txt