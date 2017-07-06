# Run shell commands on autoscaling terminate action

Quick and dirty python script for running shell commands on instances flaged for termination on autoscaling groups using AWS SSM service.

Can be used for uploading your logs to an s3 bucket.

## How to install

*   Add a hook on your autoscaling group,
`aws autoscaling put-lifecycle-hook --lifecycle-hook-name send-logs-hook --auto-scaling-group-name your-ag-group --heartbeat-timeout 60 --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING`
*   Create a function in lambda with the contents of `script.py`
*   Create events and rules on Cloudwatch that triggers this lambda function

## Disclaimer
This worked for me, maybe there is a better way to do this. For instance, maybe I should create a SNS queue for this hook and add a notification endpoint to the `put-lifecycle-hook` command.
