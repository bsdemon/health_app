FROM python:3.6

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /usr/src/app

# Install depencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy app source code
COPY . /usr/src/app

# Run app
RUN ["/usr/src/app/run_app.sh"]




