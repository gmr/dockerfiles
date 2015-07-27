FROM ubuntu:trusty

RUN apt-get update -q && \
  apt-get install -y -q curl && \
  curl -L http://overviewer.org/debian/overviewer.gpg.asc | sudo apt-key add - && \
  echo "deb http://overviewer.org/debian ./" > /etc/apt/sources.list.d/overviewer.list && \
  apt-get update -q && \
  apt-get install -q -y minecraft-overviewer && \
  apt-get autoremove -q -y && \
  apt-get clean && \
  mkdir -p /usr/lib/minecraft/ && \
  curl -o /usr/lib/minecraft/1.8.7.jar https://s3.amazonaws.com/Minecraft.Download/versions/1.8.7/1.8.7.jar && \
  apt-get clean && \
  rm -rf /var/lib/{apt,dpkg,cache,log,gems}

ADD overviewer /usr/local/bin/
RUN chmod a+x /usr/local/bin/overviewer

ENTRYPOINT ["/usr/local/bin/overviewer"]
