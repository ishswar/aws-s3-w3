
## Introduction  

Output of program that list EC2 instances using boto3 

``` Python
import boto3
ec2 = boto3.resource('ec2')
[...]

 

b. Use the EC2 Client API (1 pt)

import boto3
ec2 = boto3.client('ec2')
[...]
```

And list S3 buckets and it's content uisng boto3

``` Python 
import boto3
s3 = boto3.resource('s3')
[...]

 

b. Use the S3 Client API (1 pt)

import boto3
s3 = boto3.client('s3')
[...]
```
## Code 

## Sample output 

### Happy path 

```
vagrant@amx-vbox:/vagrant/aws-cli/w5$ ./list_instances.py
======================================  ======================================
=========== Listing EC2 instances using boto3 ec2.instances method ===========
======================================  ======================================
Instance ID              type           image id               State        key_name     vpc id       subnet id            security group(s)         private IP address     private DNS name                             public IP address  public DNS name
i-0271e751dd5dcbe9c      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.19.30           ip-172-31-19-30.us-west-2.compute.internal   52.33.249.7        ec2-52-33-249-7.us-west-2.compute.amazonaws.com
i-0ee6b77f395c01c21      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.16.46           ip-172-31-16-46.us-west-2.compute.internal   54.69.146.35       ec2-54-69-146-35.us-west-2.compute.amazonaws.com
i-05e7734787f7b377f      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.29.254          ip-172-31-29-254.us-west-2.compute.internal  18.236.206.234     ec2-18-236-206-234.us-west-2.compute.amazonaws.com
i-00eba519691255242      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.30.83           ip-172-31-30-83.us-west-2.compute.internal   34.220.248.195     ec2-34-220-248-195.us-west-2.compute.amazonaws.com
======================================  ======================================
============ Listing EC2 instances using boto3 ec2.client method =============
======================================  ======================================
Instance ID              type           image id               State        key_name     vpc id       subnet id            security group(s)         private IP address     private DNS name                             public IP address  public DNS name
i-0271e751dd5dcbe9c      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.19.30           ip-172-31-19-30.us-west-2.compute.internal   52.33.249.7        ec2-52-33-249-7.us-west-2.compute.amazonaws.com
i-0ee6b77f395c01c21      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.16.46           ip-172-31-16-46.us-west-2.compute.internal   54.69.146.35       ec2-54-69-146-35.us-west-2.compute.amazonaws.com
i-05e7734787f7b377f      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.29.254          ip-172-31-29-254.us-west-2.compute.internal  18.236.206.234     ec2-18-236-206-234.us-west-2.compute.amazonaws.com
i-00eba519691255242      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.30.83           ip-172-31-30-83.us-west-2.compute.internal   34.220.248.195     ec2-34-220-248-195.us-west-2.compute.amazonaws.com
======================================  ======================================
============ Listing s3 instances using boto3 s3.instances method ============
======================================  ======================================

Bucket Name              CreationDate                 Owner                  OwnerID
elasticbeanstalk-us-wes  09 January 2015 07:23:01 PM  swaraj_shah  28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba

	Content of bucket [elasticbeanstalk-us-west-2-858619844792]
              Object Name                  Size (KB)    ModifiedDate               S3 Storage Class
              .elasticbeanstalk            0.0          09 January 2015 07:22:53 PM STANDARD
              resources/_runtime/_embedded 0.293        09 January 2015 07:23:00 PM STANDARD

Bucket Name              CreationDate                 Owner                  OwnerID
ucsc-users.hw7           16 July 2019 03:43:07 PM     swaraj_shah  28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba

	Content of bucket [ucsc-users.hw7]
              Object Name                  Size (KB)    ModifiedDate               S3 Storage Class
              ucsc1.2019.1                 0.0          18 July 2019 07:51:17 AM   STANDARD

Bucket Name              CreationDate                 Owner                  OwnerID
ucsc1.2019.1             18 July 2019 07:29:42 AM     swaraj_shah  28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba

	Content of bucket [ucsc1.2019.1]
              Object Name                  Size (KB)    ModifiedDate               S3 Storage Class
              My First file/lipsum-big.txt 6.804        18 July 2019 08:00:55 AM   STANDARD
              My Second file/lipsum-big.tx 6.804        18 July 2019 08:13:47 AM   STANDARD
              My Third file/lipsum.txt     3.383        18 July 2019 08:03:24 AM   STANDARD
======================================  ======================================
============= Listing s3 instances using boto3 s3.client method ==============
======================================  ======================================
Bucket Name              CreationDate                 Owner        OwnerID
elasticbeanstalk-us-wes  09 January 2015 07:23:01 PM  swaraj_shah  28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba

	Content of bucket [elasticbeanstalk-us-west-2-858619844792]
              Object Name                  Size (KB)    ModifiedDate               S3 Storage Class
              .elasticbeanstalk            0.0          09 January 2015 07:22:53 PM STANDARD
              resources/_runtime/_embedded 0.293        09 January 2015 07:23:00 PM STANDARD
ucsc-users.hw7           16 July 2019 03:43:07 PM     swaraj_shah  28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba

	Content of bucket [ucsc-users.hw7]
              Object Name                  Size (KB)    ModifiedDate               S3 Storage Class
              ucsc1.2019.1                 0.0          18 July 2019 07:51:17 AM   STANDARD
ucsc1.2019.1             18 July 2019 07:29:42 AM     swaraj_shah  28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba

	Content of bucket [ucsc1.2019.1]
              Object Name                  Size (KB)    ModifiedDate               S3 Storage Class
              My First file/lipsum-big.txt 6.804        18 July 2019 08:00:55 AM   STANDARD
              My Second file/lipsum-big.tx 6.804        18 July 2019 08:13:47 AM   STANDARD
              My Third file/lipsum.txt     3.383        18 July 2019 08:03:24 AM   STANDARD
```

### Case when AWS credentials are not even configured on machine 

```
vagrant@amx-vbox:/vagrant/aws-cli/w5$ ./list_instances.py
Error connecting to AWS: You must specify a region.
The AWS CLI is not configured. Please configure it using instructions at http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
vagrant@amx-vbox:/vagrant/aws-cli/w5$
```
### Case when AWS credentials are not correct 

```
vagrant@amx-vbox:/vagrant/aws-cli/w5$ ./list_instances.py
======================================  ======================================
=========== Listing EC2 instances using boto3 ec2.instances method ===========
======================================  ======================================
Error connecting to AWS : An error occurred (AuthFailure) when calling the DescribeInstances operation: AWS was not able to validate the provided access credentials
```

### Case when some ec2 instances are stopped and some are running 

```
vagrant@amx-vbox:/vagrant/aws-cli/w5$ ./list_instances.py
======================================  ======================================
=========== Listing EC2 instances using boto3 ec2.instances method ===========
======================================  ======================================
Instance ID              type           image id               State        key_name     vpc id       subnet id            security group(s)         private IP address     private DNS name                             public IP address  public DNS name
i-0271e751dd5dcbe9c      t2.micro       ami-0f2176987ee50226e  stopped      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.19.30           ip-172-31-19-30.us-west-2.compute.internal   -
i-0ee6b77f395c01c21      t2.micro       ami-0f2176987ee50226e  stopped      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.16.46           ip-172-31-16-46.us-west-2.compute.internal   -
i-05e7734787f7b377f      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.29.254          ip-172-31-29-254.us-west-2.compute.internal  18.236.206.234     ec2-18-236-206-234.us-west-2.compute.amazonaws.com
i-00eba519691255242      t2.micro       ami-0f2176987ee50226e  stopped      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.30.83           ip-172-31-30-83.us-west-2.compute.internal   -
======================================  ======================================
============ Listing EC2 instances using boto3 ec2.client method =============
======================================  ======================================
Instance ID              type           image id               State        key_name     vpc id       subnet id            security group(s)         private IP address     private DNS name                             public IP address  public DNS name
i-0271e751dd5dcbe9c      t2.micro       ami-0f2176987ee50226e  stopped      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.19.30           ip-172-31-19-30.us-west-2.compute.internal   None
i-0ee6b77f395c01c21      t2.micro       ami-0f2176987ee50226e  stopped      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.16.46           ip-172-31-16-46.us-west-2.compute.internal   None
i-05e7734787f7b377f      t2.micro       ami-0f2176987ee50226e  running      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.29.254          ip-172-31-29-254.us-west-2.compute.internal  18.236.206.234     ec2-18-236-206-234.us-west-2.compute.amazonaws.com
i-00eba519691255242      t2.micro       ami-0f2176987ee50226e  stopped      pshah2019v2  vpc-8448efe1 subnet-4a97493d      EC2_UCSC_SecurityGroup    172.31.30.83           ip-172-31-30-83.us-west-2.compute.internal   None
```

### Case when all ec2 instances are terminated 

```
vagrant@amx-vbox:/vagrant/aws-cli/w5$ ./list_instances.py
======================================  ======================================
=========== Listing EC2 instances using boto3 ec2.instances method ===========
======================================  ======================================
Instance ID              type           image id               State        key_name     vpc id       subnet id            security group(s)         private IP address     private DNS name                             public IP address  public DNS name
i-0271e751dd5dcbe9c      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  None         None                 N/A                       N/A                    N/A                                          N/A                N/A
i-0ee6b77f395c01c21      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  None         None                 N/A                       N/A                    N/A                                          N/A                N/A
i-05e7734787f7b377f      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  None         None                 N/A                       N/A                    N/A                                          N/A                N/A
i-00eba519691255242      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  None         None                 N/A                       N/A                    N/A                                          N/A                N/A
======================================  ======================================
============ Listing EC2 instances using boto3 ec2.client method =============
======================================  ======================================
Instance ID              type           image id               State        key_name     vpc id       subnet id            security group(s)         private IP address     private DNS name                             public IP address  public DNS name
i-0271e751dd5dcbe9c      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  N/A          N/A                  N/A                       N/A                                                                 N/A
i-0ee6b77f395c01c21      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  N/A          N/A                  N/A                       N/A                                                                 N/A
i-05e7734787f7b377f      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  N/A          N/A                  N/A                       N/A                                                                 N/A
i-00eba519691255242      t2.micro       ami-0f2176987ee50226e  terminated   pshah2019v2  N/A          N/A                  N/A                       N/A                                                                 N/A
```

