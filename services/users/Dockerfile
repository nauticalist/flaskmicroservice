# Base Image
FROM python:3.7.3-alpine

# Install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# Set working directory
WORKDIR /usr/src/app

# Add python requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Add entrypoint
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Add app
COPY . /usr/src/app

# Run the server
CMD ["/usr/src/app/entrypoint.sh"]
