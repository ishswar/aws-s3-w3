## Expermenting with S3 and S3api - aws cli commands 

<details>
  <summary>Full Output</summary>

##########################################################################################
###################  Create / Upload / Download - S3 bucket via S3 api ###################
##########################################################################################

#1

-- Ceate bucket 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 help
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 mb help
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 mb help

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 mb s3://ucsc-hw2-2019
make_bucket: ucsc-hw2-2019

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 ls
2015-01-09 11:23:01 elasticbeanstalk-us-west-2-858619844792
2019-07-18 12:31:23 ucsc-hw2-2019
2019-07-16 08:43:07 ucsc-users.hw7
2019-07-18 00:29:42 ucsc1.2019.1

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 ls | grep ucsc-hw2-2019
2019-07-18 12:31:23 ucsc-hw2-2019
```

#2 

-- Upload file 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ touch TestData.txt

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 cp TestData.txt s3://ucsc-hw2-2019
upload: ./TestData.txt to s3://ucsc-hw2-2019/TestData.txt
vagrant@amx-vbox:/vagrant/aws-cli/w3$
```


#3

-- List files 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 ls s3://ucsc-hw2-2019
2019-07-18 12:33:32          0 TestData.txt
vagrant@amx-vbox:/vagrant/aws-cli/w3$
```


#4

-- Remove file from S3 bucket 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 help
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 sync help

vagrant@amx-vbox:/vagrant/aws-cli/w3$ rm TestData.txt

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 sync s3://ucsc-hw2-2019 .
download: s3://ucsc-hw2-2019/TestData.txt to ./TestData.txt

vagrant@amx-vbox:/vagrant/aws-cli/w3$ ls -la
total 40
drwxrwxr-x 1 vagrant vagrant  320 Jul 18 12:36 .
drwxrwxr-x 1 vagrant vagrant  160 Jul 18 00:59 ..
-rwxrwxr-- 1 vagrant vagrant 8196 Jul 18 11:44 .DS_Store
-rwxrwxr-- 1 vagrant vagrant 3857 Jul 18 09:56 functions.sh
-rwxrwxr-- 1 vagrant vagrant   16 Jul 18 10:30 .gitignore
-rwxrwxr-- 1 vagrant vagrant 8639 Jul 18 11:52 README.md
-rwxrwxr-- 1 vagrant vagrant 7048 Jul 18 10:19 s3repo.sh
drwxrwxr-x 1 vagrant vagrant  224 Jul 18 11:44 screenCaptures
-rwxrwxr-- 1 vagrant vagrant    0 Jul 18 12:33 TestData.txt
drwxrwxr-x 1 vagrant vagrant  160 Jul 18 01:08 test folder
vagrant@amx-vbox:/vagrant/aws-cli/w3$ ls -la TestData.txt
-rwxrwxr-- 1 vagrant vagrant 0 Jul 18 12:33 TestData.txt
```


#5 

-- Delete S3 bucket 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 rm help
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 rm s3://ucsc-hw2-2019/TestData.txt
delete: s3://ucsc-hw2-2019/TestData.txt

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 help

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 rb s3://ucsc-hw2-2019
remove_bucket: ucsc-hw2-2019

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3 ls s3://ucsc-hw2-2019

An error occurred (NoSuchBucket) when calling the ListObjectsV2 operation: The specified bucket does not exist
vagrant@amx-vbox:/vagrant/aws-cli/w3$
```


############################################################################
####### Create / Upload / Download - S3 bucket via s3api api ##################
############################################################################

#1 

-- Create bucket 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api help
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api create-bucket help

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api create-bucket --bucket ucsc-hw2-2019 --create-bucket-configuration LocationConstraint=us-west-2
{
    "Location": "http://ucsc-hw2-2019.s3.amazonaws.com/"
}
```

#2 

-- List bucket 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api list-buckets
{
    "Buckets": [
        {
            "CreationDate": "2015-01-09T19:23:01.000Z",
            "Name": "elasticbeanstalk-us-west-2-858619844792"
        },
        {
            "CreationDate": "2019-07-18T19:46:05.000Z",
            "Name": "ucsc-hw2-2019"
        },
        {
            "CreationDate": "2019-07-16T15:43:07.000Z",
            "Name": "ucsc-users.hw7"
        },
        {
            "CreationDate": "2019-07-18T07:29:42.000Z",
            "Name": "ucsc1.2019.1"
        }
    ],
    "Owner": {
        "ID": "28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba",
        "DisplayName": "swaraj_shah"
    }
}
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api list-buckets --query "Buckets[].Name"
[
    "elasticbeanstalk-us-west-2-858619844792",
    "ucsc-hw2-2019",
    "ucsc-users.hw7",
    "ucsc1.2019.1"
]
```

#3 

-- Upload a file 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api put-object --bucket ucsc-hw2-2019 --key TestData.txt --body TestData.txt
{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\""
}

#4 

-- List files in bucket 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api list-objects --bucket ucsc-hw2-2019
{
    "Contents": [
        {
            "LastModified": "2019-07-18T19:57:07.000Z",
            "Owner": {
                "ID": "28d36865206f6281d636cbdf7eb9616d77fea9e8cf237f03ae2fbee2df27a0ba",
                "DisplayName": "swaraj_shah"
            },
            "Key": "TestData.txt",
            "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
            "StorageClass": "STANDARD",
            "Size": 0
        }
    ]
}
```
#5 

-- Remove file and get it back from S3 

``` BASH
vagrant@amx-vbox:/vagrant/aws-cli/w3$ rm TestData.txt

vagrant@amx-vbox:/vagrant/aws-cli/w3$ ls -la
total 40
drwxrwxr-x 1 vagrant vagrant  288 Jul 18 12:51 .
drwxrwxr-x 1 vagrant vagrant  160 Jul 18 00:59 ..
-rwxrwxr-- 1 vagrant vagrant 8196 Jul 18 11:44 .DS_Store
-rwxrwxr-- 1 vagrant vagrant 3857 Jul 18 09:56 functions.sh
-rwxrwxr-- 1 vagrant vagrant   16 Jul 18 10:30 .gitignore
-rwxrwxr-- 1 vagrant vagrant 8639 Jul 18 11:52 README.md
-rwxrwxr-- 1 vagrant vagrant 7048 Jul 18 10:19 s3repo.sh
drwxrwxr-x 1 vagrant vagrant  224 Jul 18 11:44 screenCaptures
drwxrwxr-x 1 vagrant vagrant  160 Jul 18 01:08 test folder
vagrant@amx-vbox:/vagrant/aws-cli/w3$
vagrant@amx-vbox:/vagrant/aws-cli/w3$
vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api get-object --bucket ucsc-hw2-2019 --key TestData.txt  TestData.txt
{
    "Metadata": {},
    "LastModified": "Thu, 18 Jul 2019 19:50:09 GMT",
    "AcceptRanges": "bytes",
    "ContentLength": 0,
    "ContentType": "binary/octet-stream",
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\""
}
vagrant@amx-vbox:/vagrant/aws-cli/w3$ ls -la
total 40
drwxrwxr-x 1 vagrant vagrant  320 Jul 18 12:52 .
drwxrwxr-x 1 vagrant vagrant  160 Jul 18 00:59 ..
-rwxrwxr-- 1 vagrant vagrant 8196 Jul 18 11:44 .DS_Store
-rwxrwxr-- 1 vagrant vagrant 3857 Jul 18 09:56 functions.sh
-rwxrwxr-- 1 vagrant vagrant   16 Jul 18 10:30 .gitignore
-rwxrwxr-- 1 vagrant vagrant 8639 Jul 18 11:52 README.md
-rwxrwxr-- 1 vagrant vagrant 7048 Jul 18 10:19 s3repo.sh
drwxrwxr-x 1 vagrant vagrant  224 Jul 18 11:44 screenCaptures
-rwxrwxr-- 1 vagrant vagrant    0 Jul 18 12:52 TestData.txt
drwxrwxr-x 1 vagrant vagrant  160 Jul 18 01:08 test folder
```

#6

-- Remove file from bucket and Remove S3 bucket 

``` BASH
aws s3api delete-object --bucket ucsc-hw2-2019 --key TestData.txt



vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api delete-bucket --bucket ucsc-hw2-2019

vagrant@amx-vbox:/vagrant/aws-cli/w3$ aws s3api list-buckets --query "Buckets[].Name"
[
    "elasticbeanstalk-us-west-2-858619844792",
    "ucsc-users.hw7",
    "ucsc1.2019.1"
]
```

 </details>