FROM poisonpenllc/java

RUN apt-get update
RUN apt-get install -y -qq curl
RUN curl -L -o /usr/local/lib/minecraft_server.jar https://s3.amazonaws.com/Minecraft.Download/versions/1.8.3/minecraft_server.1.8.3.jar
RUN apt-get remove -y -qq curl
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/{apt,dpkg,cache,log,gems}

RUN mkfifo /etc/minecraft-fifo

ADD etc/consul.d/minecraft.json /etc/consul.d/
ADD etc/supervisor.d/minecraft.conf /etc/supervisor.d/

EXPOSE 25565 25575
