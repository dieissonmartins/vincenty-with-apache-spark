from src.drivers.pyspark import Pyspark

if __name__ == "__main__":
    spark = Pyspark.start_session()

    data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
    columns = ["Name", "Age"]

    df = spark.createDataFrame(data, columns)

    df.foreach(lambda row: print(row.id, row.name))

    df.show()

    spark.stop()
