from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("stock_discussion_analysis")
sc = SparkContext(conf=conf)
print("hello")


df = spark.read.options(header="True").csv("./data")