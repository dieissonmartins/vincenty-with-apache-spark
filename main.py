from src.drivers.pyspark import Pyspark

if __name__ == "__main__":
    start_session = Pyspark()
    spark = start_session.start_session()

    data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
    columns = ["Name", "Age"]

    df = spark.createDataFrame(data, columns)
    df.show()

    spark.stop()
