FROM ubuntu:trusty

RUN apt-get update -qq
RUN apt-get install -y -qq python-pip
RUN pip install tornado mcstatus
ADD status.py /usr/local/bin/status
RUN chmod a+x /usr/local/bin/status

EXPOSE 8888
ENTRYPOINT /usr/local/bin/status
