from pyspark.sql import SparkSession
import pyspark.sql.functions as F

# Create a SparkSession running in local mode with all available cores
spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("OFF")
    # .appName("LocalPySparkApp") \
    
    # .master("local[*]") \
    


# Example usage: create a DataFrame
data = [(i,) for i in range(1,1000)]
columns = ["n"]
df = spark.createDataFrame(data, columns).\
        filter(
            (F.col("n") % 5 == 0) | 
            (F.col("n") % 3 == 0)
        )

ans = df.select(F.sum("n"))
ans.show()
print("Sum of multiples of 3 or 5 below 1000:",ans.select("sum(n)").collect()[0][0])

spark.stop()