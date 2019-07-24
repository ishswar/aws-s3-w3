#!/usr/bin/env python3

import sys

###
# Helper method 
###

def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner


""" Objective next two piece of code is to demonstrate that using Python Boto3 library user can query AWS e2 API ( using python)
    First we will use boto3.resource method to get e2 instances information and print it in tabular format 
    Second we will get same information but this time we will use boto3.client and create ec2 client to get information """

import boto3
from botocore.exceptions import NoRegionError
from botocore.exceptions import ClientError

try:
   ec2 = boto3.resource('ec2')
except NoRegionError as e:
   print("Error connecting to AWS: " + str(e))
   msg = "The AWS CLI is not configured."
   msg += " Please configure it using instructions at"
   msg += " http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html"
   print(msg);
   sys.exit()


index = 0;

###
# Boto3 resource call 
###

print(banner(""))
print(banner("Listing EC2 instances using boto3 ec2.instances method"))
print(banner(""))

try:
    for instance in ec2.instances.all():

         if index == 0: 
            print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
            format("Instance ID","type", "image id",  "State","key_name", "vpc id", "subnet id", "security group(s)"
            , "private IP address", "private DNS name", "public IP address", "public DNS name"))

         index+=1

         security_groups = "N/A"   
         for SG in instance.security_groups:
           security_groups += SG['GroupName'] + " "

         pri_id,pri_dns,pbub_id,pub_dns = "N/A","N/A","N/A","N/A"
         if not instance.public_ip_address is None:
            pbub_id = instance.public_ip_address

         if  not instance.public_ip_address is None:
            pub_dns = instance.public_dns_name
         
         if  not instance.private_ip_address is None:
            pri_id = instance.private_ip_address

         if not  instance.private_ip_address is None:
            pri_dns = instance.private_dns_name

         #print (instance.id,instance.instance_type,instance.image_id,instance.state['Name'],instance.key_name,instance.vpc_id
         #       ,instance.subnet_id,security_groups[:24],pri_id,pri_dns,pbub_id,pub_dns)

         print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
            format(instance.id,instance.instance_type,instance.image_id,instance.state['Name'],instance.key_name,str(instance.vpc_id)
                ,str(instance.subnet_id),security_groups[:24],pri_id,pri_dns,pbub_id,pub_dns))

except ClientError as e:
   print("Error connecting to AWS : " + str(e))
   sys.exit()

###
# Boto3 client call 
###

print(banner(""))
print(banner("Listing EC2 instances using boto3 ec2.client method"))
print(banner(""))

index = 0;

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

if len(response["Reservations"]) > 0 :
  for reservation in response["Reservations"]:
    for instance in reservation["Instances"]: 

        security_groups ="N/A"
        for SG in instance["SecurityGroups"]:
          security_groups += SG["GroupName"] + " "

        if index == 0: 
         print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
         format("Instance ID","type", "image id",  "State","key_name", "vpc id", "subnet id", "security group(s)"
         , "private IP address", "private DNS name", "public IP address", "public DNS name"))

         index+=1

        print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
          format(instance["InstanceId"],instance["InstanceType"],instance["ImageId"],instance["State"]["Name"],instance["KeyName"],instance.get("VpcId","N/A")
            ,instance.get("SubnetId","N/A"),security_groups[:24],instance.get("PrivateIpAddress","N/A"),instance.get("PrivateDnsName","N/A"),instance.get("PublicIpAddress","N/A"),instance.get("PublicDnsName","N/A")))

else:
  print("You don't have any EC2 instances as of now")      


""" Objective of next two code block is same as above - but this time we will use Boto3 to get information about S3 buckets 
    First we will use boto3.resource to get S3 bucket information and content of each buckets 
    Second we will get same information same as boto3.client """


s3 = boto3.resource('s3')

print(banner(""))
print(banner("Listing s3 instances using boto3 s3.instances method"))
print(banner(""))



for bucket in  s3.buckets.all():

     print("")
     print("{:<24} {:<28} {:<22} {:<12}".
                 format("Bucket Name","CreationDate", "Owner",  "OwnerID"));

     print("{:<24} {:<28} {:<12} {:<12}".
                  format(bucket.name[:23],bucket.creation_date.strftime("%d %B %Y %I:%M:%S %p"),s3.BucketAcl(bucket.name).owner["DisplayName"],s3.BucketAcl(bucket.name).owner["ID"]))

#Print content of buckets 
     print("\n\tContent of bucket ["+ bucket.name+"]")

     for index,item in enumerate(bucket.objects.all()):
      
       if index == 0: #Print table header only once 
         print("{:<14}{:<28} {:<12} {:<26} {:<12}".
             format("","Object Name","Size (KB)", "ModifiedDate",  "S3 Storage Class"));

       print("{:<14}{:<28} {:<12} {:<26} {:<12}".
                    format("",item.key[:28],str((item.size)/1000),item.last_modified.strftime("%d %B %Y %I:%M:%S %p"),str(item.storage_class)));
      


print(banner(""))
print(banner("Listing s3 instances using boto3 s3.client method"))
print(banner(""))

s3 = boto3.client('s3')
response = s3.list_buckets()


if len(response["Buckets"]) > 0 :
    for bucket in response["Buckets"]:

     print("{:<24} {:<28} {:<12} {:<12}".
         format("Bucket Name","CreationDate", "Owner",  "OwnerID"));

     print("{:<24} {:<28} {:<12} {:<12}".
          format(bucket["Name"][:23],bucket["CreationDate"].strftime("%d %B %Y %I:%M:%S %p"),response["Owner"]["DisplayName"],response["Owner"]["ID"]))

     reply = s3.list_objects(Bucket=bucket["Name"])

     print("\n\tContent of bucket ["+ bucket["Name"]+"]")


     for turn,item in enumerate(reply["Contents"]):
          if turn == 0:
             print("{:<14}{:<28} {:<12} {:<26} {:<12}".
                 format("","Object Name","Size (KB)", "ModifiedDate",  "S3 Storage Class"));

          print("{:<14}{:<28} {:<12} {:<26} {:<12}".
                format("",item["Key"][:28],str(item["Size"]/1000),item["LastModified"].strftime("%d %B %Y %I:%M:%S %p"),str(item["StorageClass"])));
else:
    print("You seems to not have any S3 buckets")
 