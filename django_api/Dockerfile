FROM python:3.8-slim-buster


# setting work directory
WORKDIR /usr/src/app


# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1


RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		postgresql-client \
		libpq-dev \
	&& rm -rf /var/lib/apt/lists/*


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY . .


RUN cd $WORKDIR 
RUN django-admin startproject django_api
RUN cd /usr/src/app/django_api

EXPOSE 8000