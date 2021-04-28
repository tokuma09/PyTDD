
FROM ubuntu:20.04

LABEL maintainer="Tokuma Suzuki tokuma.suzuki09@gmail.com"

ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive

# Install libraries
RUN apt-get update && \
    apt-get install -y python3.8 python3.8-venv python3-pip && \
    apt-get install -y  git && \
    git config --global user.email 'tokuma.suzuki09@gmail.com' && \
    git config --global user.name 'Tokuma Suzuki'
# determine working directory
WORKDIR /root/project

CMD ["/bin/bash"]
