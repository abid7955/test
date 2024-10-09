import boto3

def create_ec2_instance():
    # Initialize a session using your AWS profile
    ec2 = boto3.resource('ec2')

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0debe1a16a2a59f57',  # Amazon Linux 2 AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro',
        KeyName='test1',
        SecurityGroupIds=['sg-0d3d4cf512cb84be4'], 
        UserData='''#!/bin/bash
                    yum update -y
                    yum install -y python3
                    pip3 install flask boto3''',  # Optional: pre-install Flask and Boto3
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'Flask-S3-Instance'}]
            }
        ]
    )

    # Print instance details
    for instance in instances:
        print(f'Instance created: {instance.id}, Public IP: {instance.public_ip_address}')

# Run the function to create the EC2 instance
if __name__ == "__main__":
    create_ec2_instance()
