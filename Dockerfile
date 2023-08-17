# Use a imagem oficial do OpenJDK como base
FROM openjdk:8-jre

LABEL maintainer="Dieisson <dieisson.martins.santos@gmail.com>"

# Define a versão do Spark que será usada
ENV SPARK_VERSION=3.2.4
ENV HADOOP_VERSION=3.2

# Baixa e instala o Apache Spark
RUN apt-get update && apt-get install -y wget && \
    wget https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar -xvzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /spark

# Define variáveis de ambiente do Spark
ENV SPARK_HOME=/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Define o diretório de trabalho
WORKDIR /app

# Copia seus arquivos Python para dentro do container
COPY main.py /app/

# Comando padrão para iniciar o Spark (substitua por seus próprios comandos)
CMD ["spark-submit", "main.py"]