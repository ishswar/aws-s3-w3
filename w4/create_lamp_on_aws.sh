#!/bin/bash



aws ec2 delete-security-group --group-name EC2_UCSC_SecurityGroup
aws ec2 create-security-group --group-name EC2_UCSC_SecurityGroup --description "Security (for UCSC Cource) Group for EC2 instances to allow port 22,3306,80,443"
aws ec2 authorize-security-group-ingress --group-name EC2_UCSC_SecurityGroup --protocol tcp --port 22 --cidr 160.101.0.0/24
aws ec2 authorize-security-group-ingress --group-name EC2_UCSC_SecurityGroup --protocol tcp --port 22 --cidr 75.4.202.0/24
aws ec2 authorize-security-group-ingress --group-name EC2_UCSC_SecurityGroup --protocol tcp --port 3306 --cidr 160.101.0.0/24
aws ec2 authorize-security-group-ingress --group-name EC2_UCSC_SecurityGroup --protocol tcp --port 3306 --cidr 75.4.202.0/24
aws ec2 authorize-security-group-ingress --group-name EC2_UCSC_SecurityGroup --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name EC2_UCSC_SecurityGroup --protocol tcp --port 443 --cidr 0.0.0.0/0
aws ec2 describe-security-groups --group-names EC2_UCSC_SecurityGroup



export ELASIC_IP_ALLOCATION_ID=$(aws ec2 describe-addresses --filters="Name=tag-key,Values=ucsc" | jq .Addresses[0].AllocationId
) && export ELASIC_IP_ALLOCATION_ID=$(echo "$ELASIC_IP_ALLOCATION_ID" | tr -d '"') && echo "##########################################"; echo "Elasic IP's Allocation ID is $ELASIC_IP_ALLOCATION_ID"

export ELASIC_IP=$(aws ec2 describe-addresses --filters="Name=tag-key,Values=ucsc" | jq .Addresses[0].PublicIp
) && export ELASIC_IP=$(echo "$ELASIC_IP" | tr -d '"') && echo "##########################################"; echo "Elasic IP's Allocation ID is $ELASIC_IP"


aws ec2 run-instances   --image-id ami-0f2176987ee50226e --key-name pshah2019v2 --security-groups EC2_UCSC_SecurityGroup --instance-type t2.micro --placement \
 AvailabilityZone=us-west-2b --block-device-mappings DeviceName=/dev/sdh,Ebs={VolumeSize=100} --count 1 | tee output.json && export INSTANCE_ID=$(cat output.json \
  | jq .Instances[0].InstanceId) && export INSTANCE_ID=$(echo "$INSTANCE_ID" | tr -d '"') &&echo "";echo "##############################################"; \
  echo "Instance ID of machine is $INSTANCE_ID"

while true
 do
 STATE=$(aws ec2 describe-instance-status --instance-ids $INSTANCE_ID | jq .InstanceStatuses[0].SystemStatus.Details[0].Status)
 export STATE=$(echo "$STATE" | tr -d '"')

 echo "Current state instance is $STATE"

 if [ $STATE == "initializing" ]; then
 echo "It looks like machine is not up will check again in 10 seconds"
 sleep 10
 else
 echo "It looks like machien is up"
 break
 fi
done

aws ec2 associate-address --instance-id $INSTANCE_ID --allocation-id $ELASIC_IP_ALLOCATION_ID




cp -rf /vagrant/aws-cli/w4/setup.sh /vagrant/aws-cli/w4/setup_.sh

sed -i "s/FQN_NAME/$ELASIC_IP/g" /vagrant/aws-cli/w4/setup_.sh

cat /vagrant/aws-cli/w4/setup_.sh | grep FQN_HOST_NAME