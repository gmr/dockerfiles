FROM ubuntu:trusty

RUN apt-get update -qq && \
  apt-get install -y -qq python-pip  && \
  pip install tornado mcstatus  && \
  apt-get remove -y -qq software-properties-common  && \
  apt-get autoremove -y  && \
  apt-get clean  && \
  rm -rf /var/lib/{apt,dpkg,cache,log,gems}

ADD status.py /usr/local/bin/status
RUN chmod a+x /usr/local/bin/status

EXPOSE 8888
ENTRYPOINT ["/usr/local/bin/status"]
