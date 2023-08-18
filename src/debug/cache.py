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

# cria data frame
df = spark.createDataFrame(data, columns)

# salva cache em memoria
df.cache()

vr_filter = df.filter('age >= 10').collect()

# show
df.show()

spark.stop()
