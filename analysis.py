from pyspark.sql import SparkSession

spark = SparkSession \
            .builder \
            .appName("stock_discussion_anaysis") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()


df = spark.read.options(header="True").csv("./data")



df.show()


df.select("content").show()
