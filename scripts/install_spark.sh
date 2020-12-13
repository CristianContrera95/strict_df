#!/bin/bash

spark-submit --version > /dev/null 2>&1
if [[ $? -ne 0 ]]
then
    wget https://apache.dattatec.com/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
    tar -xzf spark-3.0.1-bin-hadoop3.2.tgz
    mv spark-3.0.1-bin-hadoop3.2 /opt/spark-3.0.1
    ln -s /opt/spark-3.0.1 /opt/spark

    echo "export SPARK_HOME=/opt/spark" >> ~/.profile
    echo "export PATH=$SPARK_HOME/bin:$PATH" >> ~/.profile
    echo "export PYSPARK_DRIVER_PYTHON=jupyter" >> ~/.profile
    echo "export PYSPARK_DRIVER_PYTHON_OPTS='notebook'" >> ~/.profile
    echo "export JAVA_HOME=usr/lib/jvm/java-11-openjdk" >> ~/.profile
    echo "export PATH=$JAVA_HOME/bin:$PATH" >> ~/.profile
    echo "export PYSPARK_PYTHON='python3'" >> ~/.profile

fi
