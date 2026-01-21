#EC2 status checker 

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

