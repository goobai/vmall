FROM python:alpine3.9

RUN mkdir /usr/src/vmall-service
WORKDIR /usr/src/vmall-service
COPY ./vmall-service /usr/src/vmall-service
RUN pip install  -r requirements.txt
CMD ["gunicorn","run:app","-b","0.0.0.0:8989"]
