
#!/bin/bash

export FQN_HOST_NAME=FQN_NAME

echo "#########################################"
echo "Working on machine $FQN_HOST_NAME"
echo "#########################################"

sudo yum update -y

sudo yum install -y httpd24 php70 mysql56-server php70-mysqlnd

sudo service httpd start && sudo chkconfig httpd on

sudo groupadd www

sudo usermod -a -G www ec2-user

sudo chown -R root:www /var/www

sudo chmod 2775 /var/www

find /var/www -type d -exec sudo chmod 2775 {} \;

find /var/www -type f -exec sudo chmod 0664 {} \;

sudo sed -i 's\2M\4M\' /etc/php.ini

cat /etc/php.ini | grep 4M

sudo chkconfig httpd on

sudo service mysqld start && sudo chkconfig mysqld on