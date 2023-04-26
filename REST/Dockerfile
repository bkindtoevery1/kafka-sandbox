FROM ubuntu:18.04
RUN mkdir -p /root/install
RUN apt-get update

WORKDIR /root/install

ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN apt-get install openjdk-8-jdk -y
RUN apt-get install wget -y
RUN apt-get install vim -y

# Confluent는 23.04.09 기준 최신버전이 7.3.3
RUN wget http://packages.confluent.io/archive/7.3/confluent-community-7.3.3.tar.gz
RUN tar -zxvf confluent-community-7.3.3.tar.gz
RUN mv confluent-7.3.3 /usr/local/confluent

COPY config/kafka-rest.properties /usr/local/confluent/etc/kafka-rest/kafka-rest.properties

CMD /usr/local/confluent/bin/kafka-rest-start /usr/local/confluent/etc/kafka-rest/kafka-rest.properties

