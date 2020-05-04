#!/usr/bin/python3
import os 
import getpass
import subprocess

os.system("tput setaf 2")

apassword="redhat"
password=getpass.getpass("Enter your password")

if password!=apassword:
    print("You are not authorized user")
    os.system("tput setaf 7")
    exit()

print("where you want to run your menu local/remote",end=" ")
location=input()

if location=='remote':
    print("give your ip",end=" ")
    ip=input()

def local_cont_launch():
    os.system("docker images")
    os.system("docker ps -a")
    print("Which image do you want to run",end=" ")
    doc=input()
    print("which name do you want to give your docker",end=" ")
    name=input()
    os.system(" docker container run -itd --name {} {}".format(name,doc))

def local_yum():
    os.system("echo -e -n '[dvd1] \n baseurl=file:///run/media/root/RHEL-8-0-0-BasOS-x86_64/AppStream \n gpgcheck=0 \n [dvd2] \n baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \n gpgcheck=0'>/etc/yum.repos.d/final.repo")

def local_httpd():
    os.system("yum install httpd -y")
    os.system("systemctl restart httpd")
    os.system("systemctl enable httpd")

def local_inst_doc():
    os.system("echo -e -n '[docker]\n baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ \n gpgcheck=0'>/etc/yum.repos.d/doc.repo")
    os.system(" yum install docker-ce --nobest -y")
    os.system(" systemctl restart docker")
    os.system(" systemctl enable enable")

def local_net_doc():
    os.system("docker network ls")
    print("which driver do you want for network")
    net=input()
    print("which name do you want to give your network")
    driver_name=input()
    os.system("docker network create --driver {} {}".format(net,driver_name))
def local_cont_expo():
    os.system("docker images")
    os.system("docker ps -a")
    print("give a port number",end=" ")
    port=input()
    print("name of docker you want to give",end=" ")
    name=input()
    print("name of image for launching of docker",end=" ")
    image=input()
    os.system("docker container run -dit --name {} -p {} {}".format(name,port,image))
def local_cont_vol():
    os.system("docker volume ls")
    print("name of volume you want to give")
    volume=input()
    os.system("docker volume create {}".format(volume))
while True:
    if location=='local':
        os.system("tput setaf 4")
        print("\t\t\twelcome to my menu")
        print("\t\t\t------------------")
        print("""\t\tPress 1: For Date
                Press 2: For Cal
                Press 3: For useradd
                Press 4: To configure yum in os
                Press 5: To install httpd server
                Press 6: TO install docker in os
                Press 7: To launch a docker in os
                Press 8: To connect a docker from network
                Press 9: To expose docker 
                Press 10: To create volume in docker
                Press 11: To exit from menu"""
                )

        print("Enter your choice",end=" ")
        ch=int(input())
        
        if ch==1:
            os.system("date")
        elif ch==2:
            os.system("cal")
        elif ch==3:
            user=input("Name of user")
            os.system("useradd {}".format(user))
        elif ch==4:
            local_yum()
        elif ch==5:
            local_httpd()
        elif ch==6:
            local_inst_doc()
        elif ch==7:
            local_cont_launch()
        elif ch==8:
            local_net_doc()
        elif ch==9:
            local_cont_expo()
        elif ch==10:
            local_cont_vol()
        elif ch==11:
            os.system("tput setaf 7")
            exit()
        else:
            print("option doesn't ")
        input("Enter to continue........")
        os.system("clear")
    
    elif location=='remote':
        
        os.system("tput setaf 6")
        out=subprocess.getstatusoutput("ping -c 1  {}".format(ip))
        last=out[0]
        
        if last != 0:
            print("Please check your connection or please provide valid ip")
            os.system("tput setaf 7")
            exit()
        else:
            print("""\t\tPress 1: For Date
                Press 2: For Cal
                Press 3: For useradd
                Press 4: TO configure yum in os
                Press 5: To install httpd
                Press 6: To install docker
                Press 7: TO launch a docker
                Press 8: To connect from network in docker 
                Press 9: To expose docker 
                Press 10: To create volume in docker
                Press 11: To configure ssh server in centos docker
                Press 12: To exit from menu"""
        )
        print("Enter your choice",end=" ")
        ch=int(input())
        
        if ch==1:
            os.system("ssh {} date".format(ip))
        elif ch==2:
            os.system("cal")
        elif ch==3:
            user=input("Name of user")
            os.system("ssh {0} useradd {1}".format(ip,user))
        elif ch==4:
            os.system("ssh {} ('echo -e -n [dvd1] \n baseurl=file:///run/media/root/RHEL-8-0-0-BasOS-x86_64/AppStream \n gpgcheck=0 \n [dvd2] \n baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \n gpgcheck=0')> /etc/yum.repos.d/final.repo".format(ip))

        elif ch==5:
            os.system("ssh {} yum install httpd -y".format(ip))
            os.system("ssh {} systemctl restart httpd".format(ip))
            os.system("ssh {} systemctl enable httpd".format(ip))
        elif ch==6:
            os.system("scp docker.repo {}:/etc/yum.repos.d/".format(ip))
            os.system("ssh {} yum install docker-ce --nobest -y".format(ip))
            os.system("ssh {} systemctl restart docker".format(ip))
            os.system("ssh {} systemctl enable enable".format(ip))
        elif ch==7:
            os.system("ssh {} docker images".format(ip))
            os.system("ssh {} docker ps -a".format(ip))
            print("Which image do you want to run",end=" ")
            doc=input()
            print("which name do you want to give your docker",end=" ")
            name=input()
            os.system("ssh {} docker container run -itd --name {} {}".format(ip,name,doc))
        elif ch==8:
            os.system("ssh {} docker network ls".format(ip))
            print("which driver do you want for network")
            net=input()
            print("which name do you want to give your network")
            driver_name=input()
            os.system("ssh {} docker network create --driver {} {}".format(ip,net,driver_name))
        
        elif ch==9:
            os.system("ssh {} docker images".format(ip))
            os.system("ssh {} docker ps -a".format(ip))
            print("give a port number",end=" ")
            port=input()
            print("name of docker you want to give",end=" ")
            name=input()
            print("name of image for launching of docker",end=" ")
            image=input()
            os.system("ssh {} docker container run -dit --name {} -p {} {}".format(ip,name,port,image))
        
        elif ch==10:
            os.system("ssh {} docker volume ls".format(ip))
            print("name of volume you want to give")
            volume=input()
            os.system("ssh {} docker volume create {}".format(ip,volume))

        
        elif ch==11:
            os.system("tput setaf 7")
            exit()
        else:
            print("option doesn't support")
        input("Enter to continue........")
        os.system("clear")
        
    else:
        print("Please choose from local/remote")
        os.system("tput setaf 7")
        exit()
