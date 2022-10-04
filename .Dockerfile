FROM python:3

WORKDIR /usr/src/app

COPY ./canvas-column-conversion.py /usr/src/app

RUN mkdir /usr/src/app/data/

RUN mkdir /usr/src/app/example

COPY ./*.csv /usr/src/app/example

CMD [ "python", "/usr/src/app/canvas-column-conversion.py" ]