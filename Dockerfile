FROM python:3.13.0a4
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
ENTRYPOINT ["sh","/code/run.sh"]
