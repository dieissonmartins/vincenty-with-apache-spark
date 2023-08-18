from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
import math

# Criação da sessão do Spark
spark = SparkSession.builder.appName("VincentyDistanceCalc").getOrCreate()

# Exemplo de dataframe com coordenadas geográficas
data = [
    ("Point A", 40.7128, -74.0060),  # Nova York
    ("Point B", 34.0522, -118.2437), # Los Angeles
    ("Point C", 51.5074, -0.1278)    # Londres
]
columns = ["Point", "Latitude", "Longitude"]

df = spark.createDataFrame(data, columns)

# Coordenadas do ponto de referência (ex: sua localização)
my_latitude = 37.7749
my_longitude = -122.4194

# Função UDF para calcular a distância usando a fórmula de Vincenty
@udf(DoubleType())
def vincenty_distance(lat1, lon1, lat2, lon2):
    a = 6378137.0  # Semi-eixo maior da Terra (metros)
    f = 1 / 298.257223563  # Achatamento da Terra

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    U1 = math.atan((1 - f) * math.tan(lat1_rad))
    U2 = math.atan((1 - f) * math.tan(lat2_rad))

    L = lon2_rad - lon1_rad
    Lambda = L
    Lambda_prev = -1.0

    iter_limit = 100
    iter_count = 0

    while abs(Lambda - Lambda_prev) > 1e-12 and iter_count < iter_limit:
        sin_sigma = math.sqrt((math.cos(U2) * math.sin(Lambda))**2 + (math.cos(U1) * math.sin(U2) - math.sin(U1) * math.cos(U2) * math.cos(Lambda))**2)
        cos_sigma = math.sin(U1) * math.sin(U2) + math.cos(U1) * math.cos(U2) * math.cos(Lambda)
        sigma = math.atan2(sin_sigma, cos_sigma)

        sin_alpha = (math.cos(U1) * math.cos(U2) * math.sin(Lambda)) / sin_sigma
        cos2_alpha = 1 - sin_alpha**2
        cos2_sigma_m = cos_sigma - (2 * math.sin(U1) * math.sin(U2)) / cos2_alpha

        C = (f / 16) * cos2_alpha * (4 + f * (4 - 3 * cos2_alpha))
        Lambda_prev = Lambda
        Lambda = L + (1 - C) * f * sin_alpha * (sigma + C * sin_sigma * (cos2_sigma_m + C * cos_sigma * (-1 + 2 * cos2_sigma_m**2)))

        iter_count += 1

    u2 = cos2_alpha * ((a**2 - 6356752.314245 * 2) / (6356752.314245**2))
    A = 1 + (u2 / 16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
    B = (u2 / 1024) * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))
    delta_sigma = B * sin_sigma * (cos2_sigma_m + (B / 4) * (cos_sigma * (-1 + 2 * cos2_sigma_m**2) - (B / 6) * cos2_sigma_m * (-3 + 4 * sin_sigma**2) * (-3 + 4 * cos2_sigma_m**2)))

    s = 6356752.314245 * A * (sigma - delta_sigma)  # Distância em metros

    return s / 1000  # Distância em quilômetros

# Adiciona uma coluna com a distância calculada usando a função UDF
df = df.withColumn("distance", vincenty_distance(col("Latitude"), col("Longitude"), my_latitude, my_longitude))

# Mostra o resultado
df.select("Point", "distance").show()
