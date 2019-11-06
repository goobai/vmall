FROM python:3.6

RUN mkdir -p /usr/src/vmall-server
COPY . /usr/src/vmall-server
WORKDIR /usr/src/vmall-server
RUN pip install -r requirements.txt

CMD ["gunicorn","-c","gun.conf.py","run:app"]
