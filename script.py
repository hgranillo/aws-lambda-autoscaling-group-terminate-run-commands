from __future__ import print_function
import json
import boto3
import logging

print('Loading function')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info("Event: " + str(event))
        message = (event['detail']['EC2InstanceId'])
        logger.info("Message: " + str(message))
        ssm_client = boto3.client('ssm', region_name='us-east-1')
        params={"commands":["#!/usr/bin/env bash","","aws s3 cp yourfile.log s3://yourbucket/file.log"],"workingDirectory":["/data/www/wordpress/wp-content/plugins/woocommerce/logs/"],"executionTimeout":["30"]}
        ssm_client.send_command(DocumentName='AWS-RunShellScript', InstanceIds=[message,], Comment='logging the app logs to an s3 bucket before an unceremonious termination of an ec2 instance', TimeoutSeconds=600, Parameters=params)
    except Exception as e:
        raise e
    else:
        print('Copy succeeded')
