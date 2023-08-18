import findspark

findspark.init()

from pyspark.sql import SparkSession


class Pyspark:
    def start_session(self) -> SparkSession:
        spark = SparkSession.builder.appName("SparkPythonVicenty").getOrCreate()

        return spark
