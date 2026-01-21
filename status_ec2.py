#EC2 status checker 

# Checks the state of an ec2 instance so i can run the ec2_control.py to start or stop.

import boto3

ec2 = boto3.client("ec2")
response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"]

        if state == "running":
            print(instance_id, "is RUNNING")
        else:
            print(instance_id, "is", state)

