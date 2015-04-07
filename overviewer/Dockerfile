FROM ubuntu:trusty

RUN apt-get update -q
RUN apt-get install -y -qq curl
RUN curl -L http://overviewer.org/debian/overviewer.gpg.asc | sudo apt-key add -
RUN echo "deb http://overviewer.org/debian ./" > /etc/apt/sources.list.d/overviewer.list
RUN apt-get update
RUN apt-get install -y minecraft-overviewer
RUN apt-get autoremove -y
RUN apt-get clean
RUN mkdir -p /usr/lib/minecraft/
RUN curl -o /usr/lib/minecraft/1.8.3.jar https://s3.amazonaws.com/Minecraft.Download/versions/1.8.3/1.8.3.jar
ADD overviewer /usr/local/bin/
RUN chmod a+x /usr/local/bin/overviewer

ENTRYPOINT ["/usr/local/bin/overviewer"]
