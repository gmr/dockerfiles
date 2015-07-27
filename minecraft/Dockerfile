FROM poisonpenllc/java

RUN curl -L -o /usr/local/lib/minecraft_server.jar https://s3.amazonaws.com/Minecraft.Download/versions/1.8.3/minecraft_server.1.8.7.jar
WORKDIR /var/lib/minecraft
ENTRYPOINT ["java", "-Xmx4G", "-Xms4G", "-jar", "/usr/local/lib/minecraft_server.jar", "nogui"]

EXPOSE 25565 25575
