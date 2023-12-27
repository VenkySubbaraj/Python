from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Initialize Spark session
spark = SparkSession.builder.appName("S3ReadWriteExample").getOrCreate()

s3_input_path = "s3://rifazdec24/sample_date.csv"
s3_output_path = "s3://rifazdec24/output/sample_date"

df = spark.read.csv(s3_input_path, header=True, inferSchema=True)


df = df.withColumn("rifaz", lit(1))
df.show()

df.coalesce(1).write.mode("overwrite").csv(s3_output_path).option("header","true")

spark.stop()
