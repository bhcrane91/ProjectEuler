from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import math

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("OFF")
phi = (1 + math.sqrt(5)) / 2 
psi = (1 - math.sqrt(5)) / 2
binet = lambda n: int((phi**n - psi**n) / math.sqrt(5))
target = 4000000

df = spark.createDataFrame([(n,) for n in range(target)],["n"]).\
        withColumn("binet", (F.pow(F.lit(phi), F.col("n")) - F.pow(F.lit(psi),F.col("n")))/F.lit(math.sqrt(5))).\
        withColumn("binet", F.floor(F.col("binet")).cast("int")).\
        filter(F.col("binet") < target)
#.\
#        select(F.sum("binet").alias("ans"))

df.show()
#print(df.select("ans").rdd.flatMap(lambda x:x).collect()[0][0])