import boto3
import subprocess # for bash commands

REGION = "eu-north-1"
INSTANCE_ID = "ENTER_INSTANCE_ID" 

ec2 = boto3.client("ec2", region_name=REGION)
 

# This basically lists all Ec2 instances on my account and then shows me if its running or not.
def list_ec2():
    subprocess.run("bash -c 'aws ec2 describe-instances --query Reservations[].Instances[].InstanceId --output text'", shell=True)
    subprocess.run("bash -c 'aws ec2 describe-instances --query Reservations[].Instances[].State.Name --output text'", shell=True) 


def start_instance():
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("EC2 instance starting...") 
    print("EC2 instance started Sucessfully") 


def stop_instance():
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("EC2 instance stopping...")
    print("EC2 instance stopped Sucessfully") 

print()
print("list of Ec2 instances")
list_ec2()
print()
print("\nEC2 CONTROL")
print("1 - Start instance")
print("2 - Stop instance")


choice = input("Choose option (1 or 2): ")

if choice == "1":
    start_instance()

elif choice == "2":
    stop_instance()

else:
    print("Invalid option.")
