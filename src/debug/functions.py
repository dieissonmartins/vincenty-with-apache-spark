from src.drivers.pyspark import Pyspark
import pyspark.sql.functions as f

start_session = Pyspark()
spark = start_session.start_session()

data = [
    ("Alice", 34),
    ("Bob", 45),
    ("Charlie", 29),
    ("João", 12),
    ("Maria", 17),
    ("Carlos", 11),
    ("Ana", 19),
    ("Pedro", 12),
    ("Sofia", 17),
    ("Luis", 68),
    ("Laura", 200),
    ("Rafael", 2),
    ("Julia", 7)
]
columns = ["name", "age"]

df = spark.createDataFrame(data, columns)

# upper
vr_upper = df.withColumn('name', f.upper('name')).collect()

# filter
vr_filter = df.filter('age >= 10').collect()

new.to()

df.show()

spark.stop()
