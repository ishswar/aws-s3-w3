#!/bin/bash

userListBucket="ucsc-users.hw7"


createUserBucket(){	

bucketList=$(aws s3 ls | grep $1 | wc -l)

if [ $bucketList -gt 0 ];then
    #echo "user Repository exists"
    #aws s3 ls
    echo "" 
else
    aws s3 mb s3://$1 || { echo "Failed to create Repository $1"; exit 1; }
    #aws s3 ls
    #echo "User Repository not found, creating $1"
fi
}

createUser(){

    # This is where we store all user related info
    createUserBucket $userListBucket

    touch $1

    aws s3 cp --quiet $1 s3://$userListBucket --metadata="password=$2,email=$3"

    USER_EMAIL=$(aws s3api head-object --bucket $userListBucket --key $1 | jq '.Metadata.email')

    USERFOUND=$(echo $USER_EMAIL | grep $3 | wc -l)

    rm $1

    if [ $USERFOUND -gt 0 ]; then 
       createUserBucket $1
       echo "User Created/Updated successfully"
       
    else
       echo "There was error contact admin"
    fi 

    #deleteUser $1
    #autenticateUser $1 $2

}

deleteGivenUser(){

autenticateUser $1 $2

while true; do
    read -p "Do you wish to delete user [$1] and it's repository ?" yn
    case $yn in
        [Yy]* ) deleteUser $1 && break;;
        [Nn]* ) echo "Skipping user delete";;
        * ) echo "Please answer yes or no.";;
    esac
done

}

autenticateUser(){

bucketList=$(aws s3 ls s3://$userListBucket | grep $1 | wc -l)

if [ $bucketList -gt 0 ];then
    #echo "user bucket exists"
    PASSWORD_FROMAWS=$(aws s3api head-object --bucket $userListBucket --key $1 | jq '.Metadata.password' || { echo "Error getting list of user"; exit 1; } )
    PASSWORD_FROMAWS=$(echo "$PASSWORD_FROMAWS" | tr -d '"')

    #echo "PASSWORD_FROMAWS : [$PASSWORD_FROMAWS] & [$2]"

    if [ "$PASSWORD_FROMAWS" == "$2" ]; then 
        echo "User [$1] is authenticated successfully"
    else
        echo "Unable to validate user,check password entered"
        exit 1 
    fi
else
    echo "user [$1] does not exists, first create user"
    exit 1
fi
  

}

deleteUser(){

bucketList=$(aws s3 ls | grep $1 | wc -l)

if [ $bucketList -gt 0 ];then
    echo "Repository for user [$1] found; now deleting it"
    aws s3 rb s3://$1 --force || { echo "Unable to delete users Repository"; }
else
    echo "user repository does not exists no need to do anything"
fi
  
  echo "Removing user entry from user-list"
  aws s3 rm s3://$userListBucket/$1 || { echo "Unable to remove user from user-list "; }
 
  

}

uploadFile(){

    autenticateUser $1 $2

    aws s3 cp --quiet "$4" "s3://$1/$3/"

    BASENAME=$(basename "$4")

    aws s3 ls "s3://$1/$3/$BASENAME" || { echo "File [$4] did not get uploaded to repository [s3://$1/$3/] - contact admin " ; exit 1; }

    echo "File [$4] got successfully uploaded to repository [s3://$1/$3/]"

}

listFiles(){

    autenticateUser $1 $2
    
    echo "Listing files in user's repository"
    echo "=================================="
    aws s3 ls "s3://$1" --recursive --human-readable --output table || { echo "Unable to list files in user [$1] repository - contact admin " ; exit 1; }

}

downloadFile(){

    autenticateUser $1 $2

    aws s3 cp "s3://$1/$3" "$4" --recursive 

    echo "File with key [$3] got successfully downloaded to local directory [$4]"

}

deletedFile(){

    autenticateUser $1 $2

    aws s3 rm "s3://$1/$3" --recursive || { echo "Unable to delete files in user [$1] repository - contact admin " ; exit 1; }

    echo "File with key [$3] got successfully deleted from user's [$1] repository"

}

#aws s3 cp test.txt "s3://pshah/new old Folder/"
# aws s3 cp "s3://pshah/new old Folder" . --recursive

#aws s3 cp test2.txt s3://pshah-bucket --metadata='password=test,email=test@test.com'