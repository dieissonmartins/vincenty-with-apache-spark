# set ubuntu image
FROM ubuntu:latest

# set environment variables
ENV SPARK_VERSION=3.2.4
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYSPARK_PYTHON=/usr/bin/python3

# install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    openjdk-8-jre-headless \
    wget \
    python3 \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# download and install Spark by site
RUN wget -q https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar xzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz -C /opt && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    ln -s /opt/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION $SPARK_HOME

# install Python packages
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy a sample python script
COPY main.py /main.py

# Entry point
CMD ["python3", "/main.py"]