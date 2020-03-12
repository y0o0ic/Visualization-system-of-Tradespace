FROM python:3.7-stretch

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

ENTRYPOINT [ "python" ]
CMD ["app.py"]
