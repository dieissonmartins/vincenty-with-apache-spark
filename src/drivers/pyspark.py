import findspark

findspark.init()

from pyspark.sql import SparkSession


class Pyspark:

    @classmethod
    def start_session(cls) -> SparkSession:
        spark = SparkSession.builder.appName("SparkPythonVicenty").getOrCreate()

        return spark
