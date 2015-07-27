FROM ubuntu:trusty

RUN apt-get update -qq && \
  apt-get install -qq -y software-properties-common && \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update -qq && \
  apt-get install -qq -y nginx && \
  apt-get remove -y -qq software-properties-common  && \
  apt-get autoremove -y  && \
  apt-get clean  && \
  rm -rf /var/lib/{apt,dpkg,cache,log,gems} && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx && \
  rm /etc/nginx/sites-enabled/default && \
  ln -sf /dev/stdout /var/log/nginx/access.log && \
  ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /etc/nginx
ENTRYPOINT /usr/sbin/nginx
EXPOSE 80 443
