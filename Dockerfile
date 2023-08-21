# set ubuntu image
FROM ubuntu:latest

# set environment variables
ENV SPARK_VERSION=3.2.4
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYSPARK_PYTHON=/usr/bin/python3

# set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    openjdk-8-jdk \
    wget \
    python3 \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# set up environment variables for Spark
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark

# download and install Spark by site
RUN wget -q https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar xzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz -C /opt && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    ln -s /opt/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION $SPARK_HOME

# download MySQL JDBC driver
RUN wget -q https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.27/mysql-connector-java-8.0.27.jar \
    -O $SPARK_HOME/jars/mysql-connector-java.jar

# install Python packages
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# add Spark bin directory to PATH
ENV PATH=$PATH:$SPARK_HOME/bin

# set the working directory inside the container
WORKDIR /app

# copy a sample python script
COPY . /app

# Entry point
CMD ["/bin/bash"]