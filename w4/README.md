## Expermenting with AWS CLI and SSH to create LAMP base setup 

<details>
  <summary>Full Output</summary>

Using the AWS Command lines tools from a bash shell, this assignment will ask you to create a set of bash shell scripts to manage an EC2 instance and create a classic LAMP stack (webserver + database).  All the steps below must use "aws ec2 ..." CLI script commands.

 

01) EC2 Creation:

Use an Amazon Linux AMI, t2.micro instance.

Make sure that it has an Elastic IP address (i.e. a public IP address) and an SSH key pair.

Add a tag called 'Name' and give it a value "LAMP server".

Note the private IP network address of your VPC, you will need this later to allow MySQL to communicate with your web server.

 

02) Configure EC2 Security Group:

Configure the security group to only allow your laptop to have access to the new instance via the Internet.  You can use https://icanhazip.com/ (Links to an external site.) to find out your laptop's public IP address.

You will also need rules to allow the MySQL database to communicate with the web server.

4 Security Group Rules: 

Note: 73.70.211.212 is a placeholder value for your actual laptop public IP address.

          10.0.0.0/8 is a placeholder value for your actual VPC private IP network range.

           0.0.0.0/0 allows the whole Internet to access your web server

Type     Protocol      Port Range       Source

SSH      TCP            22                      73.70.211.212/8

MySQL  TCP            3306                  10.0.0.0/0

HTTP     TCP            80                      0.0.0.0/0

HTTPS   TCP            443                    0.0.0.0/0

 

03) Connect to your new instance:

SSH connect into your new instance using your SSH key.

Note the account name will be "ec2-user".

 

04) Configure Linux Groups and File Permissions:

Run: sudo yum update
Installs and updates to the Amazon Linux Dependencies.


Run: sudo yum install -y httpd24 php70 mysql56-server php70-mysqlnd
Installs Apache 2.4, MySQL Server 5.6, PHP 7.0, and the mysqld-php service.

Run: sudo service http start && sudo chkconfig httpd on
Start Apache and check for errors.

Run: sudo groupadd www
Creates the group www.

Run: sudo usermod -a -G www ec2-user
Sets the file structure for group www and the user.

Log out and log back into the SSH client.

The next 4 commands are here to setup the correct file structure and permissions so that Apache can run all of the files placed in the root directory.

Run: sudo chown -R root:www /var/ww

Run: sudo chmod 2775 /var/www

Run: find /var/www -type d -exec sudo chmod 2775 {} \;

Run: find /var/www -type f -exec sudo chmod 0664 {} \;

Run: sudo nano /etc/php.ini

Press CTRL + W and type filesize and hit enter.
Replace 2M with 8M on the next line.
Press CTRL + X to save the file.
Hit y to confirm.
And hit enter to confirm again.

Run: sudo chkconfig httpd on
Check for errors in Apache’s configuration.

 

05) Check out your new web server:

Enter the the Elastic IP into your browser and see your Amazon Linux AMI Test page.

 

06) Configure MySQL install and Create a Root Account:

Run: mysql -u root -p
Just hit enter for the password since we haven’t configured one yet.


Go into your browser, and type “icanhazip.com” and find out your public IP address so that we can use it in our admin account for an added layer of security.

Create the admin user with full permissions:
    Run: CREATE USER ‘admin’@’___YOUR_IP___’ IDENTIFIED BY ‘___YOUR_PASSWORD___’;
    Run: GRANT ALL ON *.* TO ‘admin’@’___YOUR_IP___’;
    Run: GRANT GRANT OPTION ON *.* TO ‘admin’@’___YOUR_IP___’;
    Now, open your MySQL workbench.
        Click add connection. (The plus next to MySQL connections)
        Enter the Elastic IP as the host name.
        Enter ‘admin’ as the user.
        And click “Store in Vault” and enter the password you just assigned to the admin user.
        Test your connection, if successful, continue to the next command.
    Run: FLUSH PRIVILEGES;
        Only run this command AFTER confirming you can login with the new root account.
    Run: sudo chkconfig mysqld on
        Check for errors in the MySQL service configuration
    Now head back to the MySQL workbench, and click on “Users” in the Management tab on the left hand side of the screen.
    Delete all other users other than the admin account we created to ensure the best security practices for your new database configuration.

 

07) Summary:

If you made it all the way through, congratulations! You just made your first LAMP Stack. You successfully created an instance with Amazon Linux, installed a MySQL Server, PHP and Apache HTTP Software, as well as configured a root MySQL account.

You can place your web-app files or raw HTML in the /var/www/html/ folder in your instance’s directory to view them like any other website. Just enter the Elastic IP in your browser and navigate to the folders or file you uploaded.

 
</details>

## Top-level step 

1. Create a Security Group
2. Create t2.mocro AWS Linux based instance 
3. Associate Elastic IP to the instance 
4. Copy provision script to new AWS Linux machine/instance 
5. Log-into machine and run provisioning script 
6. Check to see Apache is running 
7. Log-into MySQL and create Admin User 
8. Check connection via MySQL workbench
9. Copy simple HTML page to Apache base to check it's running 

