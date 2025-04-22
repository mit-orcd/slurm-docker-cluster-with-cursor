FROM docker.io/library/buildpack-deps:noble

# Install OpenSSH and set up directories
RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server && \
    mkdir -p /run/sshd

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping

RUN apt-get update && \
    apt-get install -y --no-install-recommends less

RUN apt-get update  && \
    apt-get install -y vim

# (Optional) Set root password (change 'yourpassword')
RUN echo 'root:root' | chpasswd

# (Optional) Allow root SSH login (for testing only)
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Start SSH in foreground mode
CMD ["/usr/sbin/sshd", "-D"]
