import boto3

def publish_to_sns(topic_arn, message):
    sns_client = boto3.client('sns')

    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print(f"Message published successfully. MessageId: {response['MessageId']}")

if __name__ == "__main__":
    sns_topic_arn = 'arn:aws:sns:us-east-1:667289912626:sf_sample_sns'
    message_to_publish = 'HI Rifaz.'
    publish_to_sns(sns_topic_arn, message_to_publish)