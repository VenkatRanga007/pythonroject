import paramiko, glob

host="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"

#host="172.31.14.87"
#username="Administrator"
#password="DMWA76YU2WpYK&g@9yd*is7d4!Ps((WN"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, 22, username=username, password=password)
print("connected")

try:
    stdin, stdout, stderr = client.exec_command('dir')
    out = ''.join(stdout.readlines())
    print(out)
except Exception as e:
    print(e.message)
    err = ''.join(stderr.readlines())
    print(err)

client.close()