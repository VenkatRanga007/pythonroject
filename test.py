import win32api
import win32net
import win32netcon,win32wnet

#ip="172.31.14.87"
#username="Administrator"
#password="DMWA76YU2WpYK&g@9yd*is7d4!Ps((WN"
ip="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"

try:
    win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, 'Z:','\\\\3.109.121.57\\D$', None, username,password, 0)
    print("connection established successfully")
except Exception as e:
    print("connection not established, "+e)