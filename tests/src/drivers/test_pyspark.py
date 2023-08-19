from src.drivers.pyspark import Pyspark
from pyspark.sql import SparkSession
import pytest


class TestPyspark(object):

    def test_start_session(self):
        spark = Pyspark.start_session()

        assert isinstance(spark, SparkSession), "One is not equal to two!"
