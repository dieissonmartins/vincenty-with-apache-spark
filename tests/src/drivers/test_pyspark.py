from src.drivers.pyspark import Pyspark
from pyspark.sql import SparkSession
import pytest


def test_start_session():
    spark = Pyspark.start_session()

    assert isinstance(spark, SparkSession), "One is not equal to two!"
