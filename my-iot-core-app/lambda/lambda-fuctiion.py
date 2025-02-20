import json
import boto3
import random

#Initializing the clients
rekognition = boto3.client('rekognition')
sns = boto3.client('sns')

#Configuration values (i"d advice that replace this the values under here with an actual ARN)
sns_topic_arn = "arn:aws:sns:us-east-1:123456789012:rekognition"
collection_id = "rekognition"

def lambda_handler(event, context):
    #for simplicity , I will write a something that will simulate an image by
    traffic_intensity = random.randint(0, 100)

#simulate image analysis(in a real world scenario, you would use the rekognition API to analyze the image)
#this is a simple simulation of the image analysis

#log the simulated data
    print("Traffic intensity is ", traffic_intensity)
    print("Collection ID is ", collection_id)

    #if the traffic intensity is greater than 50, then we will send a notification
    if traffic_intensity > 50:
        response = sns.publish(
            TopicArn=sns_topic_arn,
            Message="Traffic intensity is high",
            Subject="Traffic Alert"
        )
        print(response)
    else:
        print("Traffic intensity is low")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

#This is a simple lambda function that will send a notification to an SNS topic if the traffic intensity is high
#The traffic intensity is simulated by a random number generator
#The SNS topic ARN and the collection ID are hard coded for simplicity
#The collection ID is not used in this code
#Mind you, this code is not tested, I am merely providing a template for you to work with
#should you have any questions, feel free to ask
#I hope this helps