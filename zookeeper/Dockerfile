FROM ubuntu:18.04
RUN mkdir -p /root/install
RUN apt-get update

WORKDIR /root/install

ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN apt-get install openjdk-8-jdk -y

RUN apt-get install wget -y
RUN apt-get install vim -y

RUN wget downloads.apache.org/zookeeper/zookeeper-3.8.1/apache-zookeeper-3.8.1-bin.tar.gz
RUN tar -zxvf apache-zookeeper-3.8.1-bin.tar.gz

RUN mv apache-zookeeper-3.8.1-bin /usr/local/zookeeper

COPY config/zoo.cfg /usr/local/zookeeper/conf/zoo.cfg
COPY config/init.sh init.sh

CMD bash init.sh

