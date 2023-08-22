from src.drivers.pyspark import Pyspark
from pyspark.sql.functions import lit, col
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from geopy.distance import geodesic
from pyspark.sql.types import FloatType, IntegerType

spark = Pyspark.start_session()

# dataFrame com coordenadas
data = [
    ("Point A", -19.990224673, -44.00795550)
]
columns = ["point", "latitude", "longitude"]

df = spark.createDataFrame(data, columns)


# dunção UDF para calcular a distância entre coordenadas
def calculate_distance(lat1, lng1, lat2, lng2):
    coord1 = (lat1, lng1)
    coord2 = (lat2, lng2)

    ret = geodesic(coord1, coord2).meters

    return ret


calculate_distance_udf = udf(calculate_distance)

lat2 = -19.99172504
lng2 = -44.00998329

# adicionar uma coluna com a distância entre as coordenadas
df_with_distance = df.withColumn("distance", calculate_distance_udf(col('latitude'), col('longitude'), lit(lat2), lit(lng2)))

# mostrar o DataFrame resultante
df_with_distance.show()

# encerrar a sessão Spark
spark.stop()
