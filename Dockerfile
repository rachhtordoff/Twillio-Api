FROM python:3.7.2-alpine3.9
MAINTAINER Rachael Tordoff

RUN pip3 -q install gunicorn eventlet
RUN apt-get install -y libpq-dev

COPY / /opt/

RUN pip3 install -q -r /opt/requirements.txt

EXPOSE 8000

WORKDIR /opt

CMD ["/usr/local/bin/gunicorn", "-k", "eventlet", "--pythonpath", "/opt", "--access-logfile", "-", "manage:manager.app", "--reload", "-b", "0.0.0.0:8000"]
