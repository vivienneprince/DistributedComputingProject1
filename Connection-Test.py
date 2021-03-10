from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName('hello').setMaster('spark://1.1.1.1:7077').setSparkHome('/opt/spark/')
sc = SparkContext(conf=conf)