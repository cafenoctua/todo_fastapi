FROM ubuntu:focal-20210119

ENV DEBIAN_FRONTEND=noninteractive

# install basic dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    sudo git wget cmake nano vim gcc g++ build-essential ca-certificates software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# install python
RUN add-apt-repository ppa:deadsnakes/ppa \
&& apt-get update \
&& apt-get install -y python3.8 python3-pip python3.8-dev\
&& ln -s /usr/bin/python3.8 /usr/local/bin/python3 \
&& ln -s /usr/bin/python3.8 /usr/local/bin/python

RUN apt-get install sqlite3

# install common python packages
ADD ./project/requirements.txt /tmp
RUN pip3 install pip setuptools -U && pip3 install -r /tmp/requirements.txt

# set working directory

RUN mkdir /work
WORKDIR /work

# config and clean up
RUN ldconfig \
&& apt-get clean \
&& apt-get autoremove