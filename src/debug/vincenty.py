from src.drivers.pyspark import Pyspark
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
import math
from src.debug.utils.geo import Geo

start_session = Pyspark()
spark = start_session.start_session()

data = [
    ("Point A", -19.990224673, -44.00795550)
]
columns = ["point", "latitude", "longitude"]

df = spark.createDataFrame(data, columns)

my_latitude = -19.99092218
my_longitude = -44.00930471

#latitude = col('latitude')
#longitude = col('longitude')

latitude = -19.990224673
longitude = -44.00795550

geo = Geo()
distance = geo.vincenty_distance(latitude, longitude, my_latitude, my_longitude)

# 170
debug = distance

#df = df.withColumn("distance", distance)

#df.select("point", "distance").show()
