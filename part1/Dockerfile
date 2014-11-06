#jessied Docker IPython Noteboook

FROM debian:latest

MAINTAINER Micah Hausler, <micah.hausler@ambition.com>

RUN apt-get update --fix-missing && \
    apt-get -y upgrade && \
    apt-get -y install \
    curl \
    git \
    htop \
    lsof \
    man \
    net-tools \
    pkg-config \
    python-dev \
    python-pip \
    sudo \
    unzip \
    vim \
    wget \
    zip \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    IPython==2.3.0 \
    Jinja2==2.7.3 \
    Werkzeug==0.9.6 \
    pyzmq==14.4.1 \
    tornado==4.0.2 \
    requests==2.4.3

RUN mkdir -p /var/www/ipython

ADD ./ipython_config.py /var/www/.ipython/profile_default/ipython_config.py

ENV TERM xterm
ENV CLICOLOR 1
ENV HOME /var/www

WORKDIR /var/www/ipython

EXPOSE 8000

CMD /usr/local/bin/ipython notebook --profile=default
