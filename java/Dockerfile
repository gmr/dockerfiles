FROM poisonpenllc/ubuntu

RUN apt-get update
RUN apt-get install -y -qq software-properties-common curl
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN apt-get install -y oracle-java8-installer
RUN apt-get remove -y -qq software-properties-common curl
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/{apt,dpkg,cache,log,gems}
