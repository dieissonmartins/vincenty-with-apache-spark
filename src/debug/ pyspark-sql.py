from src.drivers.pyspark import Pyspark
import pyspark.sql.functions as f
from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

spark = Pyspark.start_session()

# load envs
load_dotenv()

user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")
port = 3306

jdbc_url = ("jdbc:mysql://{host}:{port}/{database}".format(host=host, port=port, database=database))

connection_properties = {
    "user": user,
    "password": password,
    "driver": "com.mysql.jdbc.Driver"
}

# Specify the table you want to read
table_name = "despesas"

# read data from MySQL using JDBC
df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=connection_properties)

# collect
data_rows = df.collect()

# convert the rows to a dictionary
data_dict_list = [row.asDict() for row in data_rows]


spark.stop()