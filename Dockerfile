FROM python:3.9-alpine
MAINTAINER CRISTIAN_CONTRERA <cristiancontrera95@gmail.com>

# Requirements for numpy
RUN apk update && apk --no-cache add musl-dev linux-headers g++

## Install spark
# If you don't need spark, you can comment the following lines
RUN wget https://apache.dattatec.com/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
RUN tar -xzf spark-3.0.1-bin-hadoop3.2.tgz
RUN mv spark-3.0.1-bin-hadoop3.2 /opt/spark-3.0.1
RUN ln -s /opt/spark-3.0.1 /opt/spark

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook'

RUN apk add openjdk11 bash

ENV JAVA_HOME=usr/lib/jvm/java-11-openjdk
ENV PATH=$JAVA_HOME/bin:$PATH
ENV PYSPARK_PYTHON='python3'
## End spark installation


# Install strictdf and their requirements
WORKDIR /app

COPY requirements*.txt ./
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

COPY src/ src
COPY tests/ tests

COPY scripts/docker_run_test.sh .
RUN chmod +x docker_run_test.sh

CMD ["./docker_run_test.sh"]
