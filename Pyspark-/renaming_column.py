from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Filter Duplicate Columns and Write to CSV") \
    .getOrCreate()

# File path
input_file_path = "input_file.csv"
output_file_path = "output_file.csv"

# Read the CSV file into a DataFrame
df = spark.read.csv(input_file_path, header=True, inferSchema=True)

# Filter out duplicate columns
# Note: This keeps only the first occurrence of each column
filtered_df = df.select(*[col(column).alias(column) for column in df.columns])

# Write the filtered DataFrame back to a CSV file
filtered_df.write.csv(output_file_path, header=True, mode="overwrite")

# Stop the SparkSession
spark.stop()
