import sys
import os

def is_spark():
    return 'pyspark' in sys.modules and 'SPARK_HOME' in os.environ
