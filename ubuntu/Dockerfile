#
# Base docker image for Ubuntu
#
FROM ubuntu:trusty

# Let aptitude know it's a non-interactive install
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

# Hack for initctl
# See: https://github.com/dotcloud/docker/issues/1024
RUN rm /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
RUN dpkg-divert --local --rename --add /sbin/initctl

# Don't let upstart start installed services
ADD usr/sbin/policy-rc.d /usr/sbin/
RUN /bin/chmod 755 /usr/sbin/policy-rc.d

# Install dependencies
RUN apt-get update
RUN apt-get -y -qq upgrade
RUN apt-get install -y -qq curl git supervisor unzip

# Install consul
RUN curl -o /tmp/consul.zip -L https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip
RUN unzip /tmp/consul.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/consul
RUN rm /tmp/consul.zip
RUN mkdir -p /etc/consul.d

# Remove apt artifacts
RUN apt-get remove -y curl git unzip
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/

# Configuration files
RUN rm -rf /etc/supervisor
ADD etc/consul.d/consul.json /etc/consul.d/
ADD etc/security/limits.conf /etc/security/
ADD etc/supervisord.conf /etc/
ADD etc/supervisor.d/consul.conf /etc/supervisor.d/
ADD etc/sysctl.conf /etc/

# For consul
ENV GOMAXPROCS 10

# Container should start supervisord as the entrypoint
ENTRYPOINT ["/usr/bin/supervisord", "-n"]
