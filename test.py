import wmi

ip="13.233.255.118"
username="Administration"
password="jTZgcL%sG*gXivzetEQUr9&PxBQyvpUT!"
from socket import *
try:
    print("Establishing connection to %s" %ip)
    connection = wmi.WMI(ip, user=username, password=password)
    print("Connection established")
except wmi.x_wmi:
    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")