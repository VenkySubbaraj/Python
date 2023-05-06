import boto3

# Set the name of the Athena database and table to drop
database_name = "my_database"
table_name = "my_table"

# Create a Athena client
athena_client = boto3.client('athena')

# Construct the SQL statement to drop the table
drop_statement = f"DROP TABLE IF EXISTS {database_name}.{table_name}"

# Execute the SQL statement to drop the table
response = athena_client.start_query_execution(
    QueryString=drop_statement,
    QueryExecutionContext={
        'Database': database_name
    },
    ResultConfiguration={
        'OutputLocation': 's3://my-bucket/results/'
    }
)

# Wait for the query to complete
query_execution_id = response['QueryExecutionId']
while True:
    query_status = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
    status_state = query_status['QueryExecution']['Status']['State']
    if status_state == 'SUCCEEDED':
        break
    elif status_state == 'FAILED':
        raise Exception(f"Athena query failed: {query_status}")
    else:
        time.sleep(1)

# Print the result
print(f"Dropped table {database_name}.{table_name}")
