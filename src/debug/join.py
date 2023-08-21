from src.drivers.pyspark import Pyspark
from pyspark.sql.functions import lit, col

spark = Pyspark.start_session()

data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
columns = ["name", "age"]

df = spark.createDataFrame(data, columns)

data1 = [("Maria", 34), ("João", 45), ("Carla", 29)]
columns1 = ["name", "age"]
df2 = spark.createDataFrame(data1, columns1)

df_with_column = df.withColumn("age_plus", col('age'))

# collect
data_rows = df.collect()

data_dict_list = [row.asDict() for row in data_rows]

spark.stop()
