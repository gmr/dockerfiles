FROM ubuntu:trusty

RUN apt-get update && \
  apt-get install -y -qq software-properties-common curl  && \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
  add-apt-repository -y ppa:webupd8team/java  && \
  apt-get update  && \
  apt-get install -y oracle-java8-installer  && \
  apt-get remove -y -qq software-properties-common  && \
  apt-get autoremove -y  && \
  apt-get clean  && \
  rm -rf /var/lib/{apt,dpkg,cache,log,gems}
