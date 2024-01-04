import boto3
import json

aws_region = 'us-east-1'
main_queue_name = 'main_queue'
dlq_name = 'dlq'

def create_queue(queue_name):
    sqs = boto3.client('sqs',  region_name=aws_region)
    response = sqs.create_queue(QueueName=queue_name)
    return response['QueueUrl']

def create_dead_letter_queue(queue_name):
    sqs = boto3.client('sqs',  region_name=aws_region)
    response = sqs.create_queue(QueueName=queue_name)
    return response['QueueUrl']

def set_redrive_policy(main_queue_url, dlq_arn):
    sqs = boto3.client('sqs',  region_name=aws_region)
    redrive_policy = {
        'deadLetterTargetArn': dlq_arn,
        'maxReceiveCount': '5'
    }
    sqs.set_queue_attributes(
        QueueUrl=main_queue_url,
        Attributes={
            'RedrivePolicy': json.dumps(redrive_policy)
        }
    )
    print(f"RedrivePolicy set for {main_queue_url}")

def send_message_to_dlq(dlq_url, message_body):
    sqs = boto3.client('sqs',  region_name=aws_region)
    response = sqs.send_message(
        QueueUrl=dlq_url,
        MessageBody=message_body
    )

    print(f"Message sent to DLQ: {message_body}")
    return response

if __name__ == "__main__":
    dlq_url = create_dead_letter_queue(dlq_name)
    dlq_arn = boto3.client('sqs',  region_name=aws_region).get_queue_attributes(QueueUrl=dlq_url, AttributeNames=['QueueArn'])['Attributes']['QueueArn']
    print(f"Dead Letter Queue URL: {dlq_url}")
    print(f"Dead Letter Queue ARN: {dlq_arn}")
    main_queue_url = create_queue(main_queue_name)
    print(f"Main Queue URL: {main_queue_url}")
    set_redrive_policy(main_queue_url, dlq_arn)

    # Type your message here
    message_body = '{"name": "rifaz"}'
    send_message_to_dlq(dlq_url, message_body)
