# Pull official base image
FROM python:3.9.6-alpine

# == NGINX Section ==
RUN apk add --update nginx gcc musl-dev
# Copy app server config
RUN rm /etc/nginx/http.d/default.conf
COPY nginx/default.conf /etc/nginx/http.d/tracing.conf
# Copy main nginx config (inclue log definition)
RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Create directory for the app user
RUN mkdir -p /home/app

# Create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . $APP_HOME

# Change to the app user
USER root

# Expose app port (nginx) and run service
EXPOSE 80
ENTRYPOINT ["./start-server.sh"]