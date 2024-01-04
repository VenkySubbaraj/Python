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

