from src.drivers.pyspark import Pyspark
import pyspark.sql.functions as f

start_session = Pyspark()
spark = start_session.start_session()

path = "data.json"

df = spark.read.json(path)

df.show()

spark.stop()