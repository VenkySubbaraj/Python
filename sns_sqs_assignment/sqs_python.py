import boto3
import time
import json

def receive_messages_from_queue(queue_url):
    sqs_client = boto3.client('sqs')

    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=1,  # Adjust as needed
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0  # Set to a non-zero value for long-polling
    )

    if 'Messages' in response:
        for message in response['Messages']:
            # data = json.loads(message['Body'])
            # print(f"Received message from {queue_url}: {data['Message']}")
            print(f"Received message from {queue_url}: {message['Body']}")


            receipt_handle = message['ReceiptHandle']
            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
    else:
        print(f"No messages received from {queue_url}")

if __name__ == "__main__":
    # queue_url_1 = 'https://sqs.us-east-1.amazonaws.com/667289912626/sf_sample_queue_2'
    # queue_url_2 = 'https://sqs.us-east-1.amazonaws.com/667289912626/sf_sample_queues'
    queue_url_3 = 'https://sqs.us-east-1.amazonaws.com/667289912626/queue1'

    while True:
        # receive_messages_from_queue(queue_url_1)
        receive_messages_from_queue(queue_url_3)
        time.sleep(5)
