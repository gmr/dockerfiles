FROM ubuntu:trusty

RUN apt-get update -qq && \
  apt-get install -y -qq python-pip && \
  apt-get autoremove -y  && \
  apt-get clean  && \
  rm -rf /var/lib/{apt,dpkg,cache,log,gems} && \
  pip install awscli

ENV BUCKET=com.poisonpenllc.backup
COPY backup.sh /usr/local/bin/backup.sh
ENTRYPOINT ["/usr/local/bin/backup.sh"]
