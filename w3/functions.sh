#!/bin/bash

userBucket="ucsc-users.hw7"



removeUserBucket() {

bucketList=$(aws s3 ls | grep $1 | wc -l)

if [ $bucketList -gt 0 ];then
    echo "bucket found"
    aws s3 rb $1
    echo "bucket $1 deleted "
    aws ls
else
    echo "bucket not found, creating $1"
    aws s3 mb s3://$1 
    aws s3 ls
fi

}

createUserBucket(){	

bucketList=$(aws s3 ls | grep $1 | wc -l)

if [ $bucketList -gt 0 ];then
    echo "user bucket exists"
    aws s3 ls 
else
    aws s3 mb s3://$1 
    aws s3 ls
    echo "User bucket not found, creating $1"
fi
}


#aws s3 cp test2.txt s3://pshah-bucket --metadata='password=test,email=test@test.com'