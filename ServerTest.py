import paramiko, glob
from stat import S_ISDIR

host="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, 22, username=username, password=password)
print("connected")
sftp = client.open_sftp()

def sftpwalk(dl):
    remotepath = dl
    files = []
    folders = []
    for f in sftp.listdir_attr(remotepath):
        if S_ISDIR(f.st_mode):
            folders.append(f.filename)
            # print(dl+f.filename)
            sftpwalk(dl + f.filename + "/")
        else:
            # if
            files.append(f.filename)
    # print (path,folders,files)
    print(remotepath, folders, files)


dl = 'C://Users/Administrator/Desktop/'
sftpwalk(dl)
client.close