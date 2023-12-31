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

# test count
count_rows = df.count()

# schema
df.printSchema()

# select specific fields (columns)
selected_rows = (df.select("id", "seq_orgao", "cod_municipio", "dsc_funcao"))

# collect
data_rows = df.collect()

# percorrer a lista de linhas e acessar os valores das colunas
for row in data_rows:
    item_dict = row.asDict()

    debug = 0

# convert the rows to a dictionary
# data_dict_list = [row.asDict() for row in data_rows]

spark.stop()
