from src.drivers.pyspark import Pyspark
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
import math
from src.debug.utils.geo import Geo
from geopy.distance import geodesic

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


# com vicenty
distance = geo.vincenty_distance(latitude, longitude, my_latitude, my_longitude)
debug = distance

# com haversine
coord1 = (latitude, longitude)
coord2 = (my_latitude, my_longitude)
distance = geo.haversine_distance(coord1, coord2)
debug2 = distance

end = 0

#df = df.withColumn("distance", distance)
#df.select("point", "distance").show()
