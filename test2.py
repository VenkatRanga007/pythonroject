import winrm
import os

host="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"
# Create winrm connection.
sess = winrm.Session(host, auth=(username, password), transport='ntlm')
result = sess.run_ps('echo $pwd')
pwd_dir = result.std_out.decode().split('\r\n')[3]
print(pwd_dir)

sess.run_ps('cd .\Desktop')
result = sess.run_ps('ls')
print(result.std_out.decode().split('\r\n'))
for subdir, dirs, files in os.walk(pwd_dir):
    block=""
    for file in files:
        block+=subdir+"/"+file
    print(block)

print("Connected")