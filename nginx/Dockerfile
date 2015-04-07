FROM ubuntu:trusty

RUN apt-get update -qq
RUN apt-get install -qq -y software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update -qq
RUN apt-get install -qq -y nginx
RUN rm -rf /var/lib/apt/lists/*
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx
RUN rm /etc/nginx/sites-enabled/default

ADD etc/nginx/sites-enabled/default.conf /etc/nginx/sites-enabled/
ADD etc/nginx/sites-enabled/minecraft.conf /etc/nginx/sites-enabled/
ADD etc/nginx/sites-enabled/ourfamilytree.conf /etc/nginx/sites-enabled/

RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /etc/nginx

ENTRYPOINT /usr/sbin/nginx

EXPOSE 80 443
