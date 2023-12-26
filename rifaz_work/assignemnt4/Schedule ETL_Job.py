from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Initialize Spark session
spark = SparkSession.builder.appName("S3ReadWriteExample").getOrCreate()

aws_access_key_id = input("access_key")
aws_secret_access_key = input("secret_key")

spark.conf.set("spark.hadoop.fs.s3a.access.key", aws_access_key_id)
spark.conf.set("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key)

s3_input_path = "s3a://your_bucket/your_input_path/input.csv"
s3_output_path = "s3a://your_bucket/your_output_path/output.csv"

df = spark.read.csv(s3_input_path, header=True, inferSchema=True)


df = df.withColumn("column_name here", lit(1))
df.show()

df.coalesce(1).write.mode("overwrite").csv(s3_output_path)

spark.stop()
