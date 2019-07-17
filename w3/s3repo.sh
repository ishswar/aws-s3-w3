#!/bin/bash 

source /vagrant/aws-cli/w3/functions.sh || exit 0

usage()
{
cat << EOF
usage: $0 options

In order to run this script you need to pass one of below options

OPTIONS:
   -h            Show this message
   -createuser      Create user bucket
                          $0 -createuser user-name password email
   -uploadfile      Upload file to user bucket
                          $0 -uploadfile user-name password file-key path-to-file-to-upload
   -uploadfile      Remove user bucket 
EOF
}



# if no parameters were passed we exit the code after printing usage
if [[ $# -eq 0 ]] ; then
    echo 'No parameters were passed'
    printf "\n"
    usage
    exit 0
fi

echo "Starting test"
#Do case insesntive search 
shopt -s nocasematch

# Go over each argument given by user 
for OPTIONS in "$@"
do

# Any options we find we define a variable and set value of 1 
# that means user wants that option 
case "$OPTIONS" in

 "-createuser") 
             
             #createuser "ucsc-users.hw7"
             #echo "create $#"
             if [[ $# -eq 4 ]] ; then
                #echo "found 4 parmas"
                USERNAME=$2
                PASSWORD=$3
                EMAIL=$4
                 if echo "${EMAIL}" | grep '^[a-zA-Z0-9\.]*@[a-zA-Z0-9]*\.[a-zA-Z0-9]*$' >/dev/null; then
                    echo ""
                else
                    echo "E-mail address [$EMAIL] enter is not valid"
                    echo "------------------------------------------"
                    usage
                fi
            else
                echo "We expecte 4 parameters for command createuser"
                if [ $# -gt 4 ]; then echo " (toomany parameters) "; else echo " (less than expected parameters)"; fi
                echo "----------------------------------------------"
                usage
                break
            fi
             echo "About to create user [$USERNAME] with password [$PASSWORD] and E-mail [$EMAIL]"
             break;;
 "-uploadfile") 
             #removeUserBucket "ucsc-users.hw7"
             #user-name password file-key path-to-file-to-upload
             if [[ $# -eq 5 ]] ; then
                #echo "found 4 parmas"
                USERNAME=$2
                PASSWORD=$3
                FILE_KEY=$4
                FILE_PATH=$5
                if [ ! -f "$FILE_PATH" ]; then
                    echo "File [$FILE_PATH] not found!"
                    exit 1
                else
                    FILESIZE=$(stat -c%s "$FILE_PATH")
                fi
            else
                echo "We expecte 5 parameters for command createuser"
                if [ $# -gt 5 ]; then echo " (toomany parameters) "; else echo " (less than expected parameters)"; fi
                echo "----------------------------------------------"
                usage
                break
            fi
             echo "About to upload file for user [$USERNAME] with password [$PASSWORD] file key [$FILE_KEY] and local file [$FILE_PATH]($FILESIZE kb)"
             break;;
 "-listfiles") 
             #removeUserBucket "ucsc-users.hw7"
             echo "listfiles"
             break;;
 "-getfile") 
             #removeUserBucket "ucsc-users.hw7"
             echo "getfile"
             break;;      
  "-deletefile") 
             #removeUserBucket "ucsc-users.hw7"
             echo "deletefile"
             break;;                                   
 "-h")
            usage
            exit 0;;
 *) usage;;
esac

done
