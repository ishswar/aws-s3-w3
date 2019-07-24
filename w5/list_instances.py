#!/usr/bin/env python3

def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner

import boto3
ec2 = boto3.resource('ec2')

index = 0;

print(banner(""))
print(banner("Listing EC2 instances using boto3 ec2.instances method"))
print(banner(""))

for instance in ec2.instances.all():

     if index == 0: 
        print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
        format("Instance ID","type", "image id",  "State","key_name", "vpc id", "subnet id", "security group(s)"
        , "private IP address", "private DNS name", "public IP address", "public DNS name"))

     index+=1

     security_groups = ""   
     for SG in instance.security_groups:
       security_groups += SG['GroupName'] + " "

     pri_id,pri_dns,pbub_id,pub_dns = "-","-","-","-"
     if not instance.public_ip_address is None:
        pbub_id = instance.public_ip_address

     if  not instance.public_dns_name is None:
        pub_dns = instance.public_dns_name
     
     if  not instance.private_ip_address is None:
        pri_id = instance.private_ip_address

     if not  instance.private_dns_name is None:
        pri_dns = instance.private_dns_name

     #print (instance.id,instance.state['Name'],instance.key_name,instance.image_id,instance.vpc_id,instance.subnet_id,security_groups)
     print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
        format(instance.id,instance.instance_type,instance.image_id,instance.state['Name'],instance.key_name,instance.vpc_id
            ,instance.subnet_id,security_groups[:24],pri_id,pri_dns,pbub_id,pub_dns))

 #instance.terminate();


print(banner(""))
print(banner("Listing EC2 instances using boto3 ec2.client method"))
print(banner(""))

index = 0;

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

if len(response["Reservations"]) > 0 :
  for reservation in response["Reservations"]:
    for instance in reservation["Instances"]: 

        security_groups =""
        for SG in instance["SecurityGroups"]:
          security_groups += SG["GroupName"] + " "

        if index == 0: 
         print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
         format("Instance ID","type", "image id",  "State","key_name", "vpc id", "subnet id", "security group(s)"
         , "private IP address", "private DNS name", "public IP address", "public DNS name"))

         index+=1

        print("{:<24} {:<14} {:<22} {:<12} {:<12} {:<12} {:<20} {:<25} {:<22} {:<44} {:<18} {:<12}".
          format(instance["InstanceId"],instance["InstanceType"],instance["ImageId"],instance["State"]["Name"],instance["KeyName"],instance["VpcId"]
            ,instance["SubnetId"],security_groups[:24],instance["PrivateIpAddress"],instance["PrivateDnsName"],instance.get("PublicIpAddress","None"),instance["PublicDnsName"]))

else:
  print("You don't have any EC2 instances as of now")      






s3 = boto3.resource('s3')

print(banner(""))
print(banner("Listing s3 instances using boto3 s3.instances method"))
print(banner(""))



for bucket in s3.buckets.all():

 print("")
 print("{:<24} {:<28} {:<22} {:<12}".
         format("Bucket Name","CreationDate", "Owner",  "OwnerID"));

 print("{:<24} {:<28} {:<12} {:<12}".
          format(bucket.name[:23],bucket.creation_date.strftime("%d %B %Y %I:%M:%S %p"),s3.BucketAcl(bucket.name).owner["DisplayName"],s3.BucketAcl(bucket.name).owner["ID"]))

 print("\n\tContent of bucket ["+ bucket.name+"]")

 index=0;

 for item in bucket.objects.all():
  
  if index == 0:
     print("{:<14}{:<28} {:<12} {:<26} {:<12}".
         format("","Object Name","Size (KB)", "ModifiedDate",  "S3 Storage Class"));
  index+=1;
  print("{:<14}{:<28} {:<12} {:<26} {:<12}".
                format("",item.key[:28],str((item.size)/1000),item.last_modified.strftime("%d %B %Y %I:%M:%S %p"),str(item.storage_class)));
  


print(banner(""))
print(banner("Listing s3 instances using boto3 s3.client method"))
print(banner(""))

s3 = boto3.client('s3')
response = s3.list_buckets()

index=0;

if len(response["Buckets"]) > 0 :
    for bucket in response["Buckets"]:
     if index == 0:
        print("{:<24} {:<28} {:<12} {:<12}".
         format("Bucket Name","CreationDate", "Owner",  "OwnerID"));

        index+=1;

     print("{:<24} {:<28} {:<12} {:<12}".
          format(bucket["Name"][:23],bucket["CreationDate"].strftime("%d %B %Y %I:%M:%S %p"),response["Owner"]["DisplayName"],response["Owner"]["ID"]))

     reply = s3.list_objects(Bucket=bucket["Name"])

     print("\n\tContent of bucket ["+ bucket["Name"]+"]")

     index=0;

     for item in reply["Contents"]:
          if index == 0:
             print("{:<14}{:<28} {:<12} {:<26} {:<12}".
                 format("","Object Name","Size (KB)", "ModifiedDate",  "S3 Storage Class"));
          index+=1;
          print("{:<14}{:<28} {:<12} {:<26} {:<12}".
                format("",item["Key"][:28],str(item["Size"]/1000),item["LastModified"].strftime("%d %B %Y %I:%M:%S %p"),str(item["StorageClass"])));
 