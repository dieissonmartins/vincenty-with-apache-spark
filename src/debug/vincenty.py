from src.drivers.pyspark import Pyspark
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
import math
from src.debug.utils.geo import Geo
from geopy.distance import geodesic
import googlemaps

start_session = Pyspark()
spark = start_session.start_session()

data = [
    ("Point A", -19.990224673, -44.00795550)
]
columns = ["point", "latitude", "longitude"]

df = spark.createDataFrame(data, columns)

my_latitude = -19.99172504
my_longitude = -44.00998329

#latitude = col('latitude')
#longitude = col('longitude')

latitude = -19.99470298
longitude = -44.00664815

geo = Geo()


# com vicenty
distance = geo.vincenty_distance(latitude, longitude, my_latitude, my_longitude)
debug = distance

# com haversine
coord1 = (latitude, longitude)
coord2 = (my_latitude, my_longitude)
distance = geo.haversine_distance(coord1, coord2)
debug2 = distance

# com geopy
distance = geodesic(coord1, coord2).meters
debug3 = distance


#gmaps = googlemaps.Client(key='KEY')
#result = gmaps.distance_matrix(coord1, coord2, mode="driving", units="metric")
#distance = result['rows'][0]['elements'][0]['distance']['value']
#debug4 = distance


end = 0

#df = df.withColumn("distance", distance)
#df.select("point", "distance").show()
