
# import boto3
# import uuid
# import time

# # Replace 'YOUR_AWS_ACCESS_KEY_ID' and 'YOUR_AWS_SECRET_ACCESS_KEY' with your AWS credentials
# region_name = 'us-east-2'

# # Replace 'YOUR_QUEUE_URL' with the URL of your AWS SQS FIFO queue
# queue_url = 'https://sqs.us-east-2.amazonaws.com/667289912626/sf_fifo.fifo'

# # Initialize SQS client
# sqs = boto3.client('sqs', region_name=region_name)

# def send_message(message_body):
#     # Generate a unique identifier for the message
#     message_id = str(uuid.uuid4())

#     # Get the current timestamp as the sequence number
#     sequence_number = int(time.time())

#     # Construct message attributes with unique identifier and sequence number
#     message_attributes = {
#         'UniqueId': {
#             'DataType': 'String',
#             'StringValue': message_id
#         },
#         'SequenceNumber': {
#             'DataType': 'Number',
#             'StringValue': str(sequence_number)
#         }
#     }

#     # Send the message to the SQS queue
#     response = sqs.send_message(
#         QueueUrl=queue_url,
#         MessageBody=message_body,
#         MessageAttributes=message_attributes,
#         MessageDeduplicationId=message_id,
#         MessageGroupId='example_group_id'  # Required for FIFO queues
#     )

#     print(f"Message sent to SQS with ID: {message_id}, Sequence Number: {sequence_number}")
#     return response


# def process_message(message):
#     # Get the unique identifier and sequence number from the message attributes
#     deduplication_id = message.get('Attributes', {}).get('MessageDeduplicationId', '')
#     unique_id = message.get('MessageAttributes', {}).get('UniqueId', {}).get('StringValue', '')
#     sequence_number = message.get('MessageAttributes', {}).get('SequenceNumber', {}).get('StringValue', '')

#     # Add your custom logic to process the received message
#     print(f"Processing Message: {message['Body']}")
#     print(f"  Unique ID: {unique_id}")
#     print(f"  Sequence Number: {sequence_number}")
#     print(f"  deduplication_id: {deduplication_id}")

# # Receive messages from the SQS queue
# def receive_messages():
#     while True:
#         response = sqs.receive_message(
#             QueueUrl=queue_url,
#             AttributeNames=['All'],
#             MessageAttributeNames=['All'],
#             WaitTimeSeconds=2  # Long polling for better efficiency
#         )

#         messages = response.get('Messages', [])
#         for message in messages:
#             # Check if the message is not a duplicate
#             deduplication_id = message.get('MessageAttributes', {}).get('sequence_number', {}).get('StringValue', '')
#             if deduplication_id not in processed_messages:
#                 # Process the message
#                 process_message(message)
#                 # Add the deduplication_id to the set of processed messages
#                 processed_messages.add(deduplication_id)
#                 # Delete the message from the queue
#                 sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

# if __name__ == "__main__":
#     processed_messages = set()
#     i = 1
#     a = 1

#     try:
#         while ( i < 2):
#             i = i + 1 
#             a = a + 1 
#             message_body = str(a)
#             send_message(message_body)
#             time.sleep(2)
#         receive_messages()
#     except KeyboardInterrupt:
#         print("Terminating the script.")



import boto3
import uuid
import time

# Initialize SQS client
region_name = 'us-east-2'
sqs = boto3.client('sqs', region_name=region_name)

# Replace 'YOUR_QUEUE_NAME' with the desired name for your SQS FIFO queue
queue_name = 'sf_sample_fifo.fifo'
message_group_id = '1'

def create_fifo_queue():
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes={
            'FifoQueue': 'true',
            'ContentBasedDeduplication': 'true'
        }
    )

    queue_url = response['QueueUrl']
    print(f"SQS FIFO Queue created: {queue_url}")
    return queue_url

def send_message(queue_url, message_body):
    # Generate a unique identifier for the message
    message_id = str(int(time.time()))

    # Send the message to the SQS queue with a specified message group
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body,
        MessageGroupId=message_group_id,
        MessageDeduplicationId=message_id
    )

    print(f"Message sent to SQS with ID: {message_id}")
    return response

def poll_messages(queue_url):
    print("Polling for messages...")
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20  # Long polling for better efficiency
        )

        messages = response.get('Messages', [])
        for message in messages:
            print(f"Received Message: {message['Body']}")

            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

if __name__ == "__main__":
    i = 1
    try:
        queue_url = create_fifo_queue()
        while (i < 10):
            i = i + 1
            message_body = 'Hello, AWS SQS!'
            send_message(queue_url, message_body)
        poll_messages(queue_url)

    except KeyboardInterrupt:
        print("Terminating the script.")

