#syntax=docker/dockerfile:experimental

# Base image
FROM python:3.8-buster

# Maintainer
LABEL Author="https://github.com/pan-efs"

# Set noninteractive
ARG DEBIAN_FRONTEND=noninteractive

# Install necessary ubuntu packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    git

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Logs are flushed to the terminal directly
ENV PYTHONBUFFERED 1

# Create the virtual environment to run code within
RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH

# Upgrade pip in the venv
RUN /venv/bin/python3.8 -m pip install --upgrade pip

# Make a dir
RUN mkdir /app

# Work in the /app dir
WORKDIR /app

# Copy dependencies
COPY ../requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy desired folders
COPY ../dashboard /app/dashboard
COPY ../dbms /app/dbms
COPY ../imgs /app/imgs
COPY ../tests /app/tests
COPY ../setup.py /app

# Run pip install
RUN pip install /app/.