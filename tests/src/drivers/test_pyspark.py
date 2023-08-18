from src.drivers.pyspark import Pyspark

from pyspark.sql import SparkSession


def test_start_session():
    spark = Pyspark.start_session()

    assert isinstance(spark, SparkSession)
