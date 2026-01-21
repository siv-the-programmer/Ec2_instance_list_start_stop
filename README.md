# EC2 Start / Stop Automation (Python + AWS CLI)
# Overview
This project is a beginner-friendly AWS automation script built using Python, boto3, and AWS CLI.

It allows you to:

List all EC2 instances in your AWS account

View their current running state

Start an EC2 instance

Stop an EC2 instance

# The goal of this project is to demonstrate practical AWS automation skills using both:

AWS SDK for Python (boto3)

AWS CLI executed through Python

This reflects how real cloud engineers automate infrastructure instead of relying on the AWS Console.

# Technologies Used
```
Python 3

AWS SDK for Python (boto3)

AWS CLI

Bash commands executed via Python subprocess

IAM permissions for EC2 control
```

---

# How the Script Works

Python runs AWS CLI commands to list EC2 instances

Instance IDs and states are displayed

User selects whether to start or stop an instance

boto3 sends the start or stop request to AWS EC2

---

Script Breakdown
--
1. AWS Configuration
```
REGION = "eu-north-1"
INSTANCE_ID = "ENTER_INSTANCE_ID"
```

Region must match where your EC2 instance exists

Instance ID must start with:
```
i-xxxxxxxxxxxxxxxxx
```

# Reserved instance IDs (r-xxxx) will not work.

2. Listing EC2 Instances
```
def list_ec2():
    subprocess.run(
        "bash -c 'aws ec2 describe-instances --query Reservations[].Instances[].InstanceId --output text'",
        shell=True
    )

    subprocess.run(
        "bash -c 'aws ec2 describe-instances --query Reservations[].Instances[].State.Name --output text'",
        shell=True
    )

```
This uses the AWS CLI to:

Retrieve all EC2 instance IDs

Retrieve their current states

The --output text option removes JSON brackets and makes output readable.

3. Starting an Instance
  ``` 
def start_instance():
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
```

This calls the AWS EC2 API:
```
StartInstances
```

@ Billing begins when the instance enters the running state.

4. Stopping an Instance
```
def stop_instance():
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
```

This calls:
```
StopInstances
```

Compute billing stops, but EBS storage costs remain.

5. Menu-Based CLI Interface
```
print("1 - Start instance")
print("2 - Stop instance")
```

User input determines which EC2 API call is executed.

Example Output
```
list of Ec2 instances
i-0a1b2c3d4e5f67890
i-09182736455443321

running
stopped

```

EC2 CONTROL
```
1 - Start instance
2 - Stop instance
Choose option (1 or 2):
```

@ Prerequisites
1. Python installed
python --version


# Recommended: Python 3.10+

2. Install dependencies
```
pip install boto3
```
4. AWS CLI installed
```
aws --version
```

6. Configure AWS credentials
```aws configure```


You must configure:
```
Access Key ID

Secret Access Key

Default region

Output format (json or text)

Credentials are stored securely in:

~/.aws/credentials
```

# No credentials are stored in this repository.

Required IAM Permissions
--

The AWS user or role must have the following permissions:
```
{
  "Effect": "Allow",
  "Action": [
    "ec2:DescribeInstances",
    "ec2:StartInstances",
    "ec2:StopInstances"
  ],
  "Resource": "*"
}
```

Without these permissions the script will fail.

--

Important AWS Concepts Demonstrated
--


EC2 lifecycle states

Difference between start and create

boto3 client usage

AWS CLI integration

IAM permissions

Region-specific resources

Infrastructure automation

Safety Notes
---

Starting an EC2 instance incurs cost

Stopping EC2 does not delete it

EBS volumes continue to incur storage charges

Terminated instances cannot be restarted

Learning Objectives
--

# This project was built to practice:

```
Python automation

AWS SDK usage

CLI-to-Python integration

Cloud cost awareness

Infrastructure-as-code mindset

DevOps-style tooling
```
Possible Improvements
```

Future enhancements could include:

Automatic instance ID detection

State validation before start/stop

Display instance name tags

Tag-based instance selection

Lambda-based automation

Scheduled auto shutdown

Telegram or email notifications
```
# Author

Siv
Learning cloud engineering through hands-on AWS automation.

GitHub:
https://github.com/siv-the-programmer
