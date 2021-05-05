from pyspark.sql import SparkSession

spark = SparkSession \
            .builder \
            .appName("stock_discussion_anaysis") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()


df = spark.read.options(header="True").csv("./data")





# SparkSession to SparkContext
sparkContext=spark.sparkContext
lines = sparkContext.parallelize(["hello", "world"])


type(lines)




# dataframe to rdd
rdd = df.rdd

rdd.get(0)