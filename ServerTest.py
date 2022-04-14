import paramiko, os
from stat import S_ISDIR

def convert_bytes(size, unit=None):
    if unit == "KB":
        return 'File size: ' + str(round(size / 1024, 3)) + ' Kilobytes'
    elif unit == "MB":
        return 'File size: ' + str(round(size / (1024 * 1024), 3)) + ' Megabytes'
    elif unit == "GB":
        return 'File size: ' + str(round(size / (1024 * 1024 * 1024), 3)) + ' Gigabytes'
    else:
        return 'File size: ' + str(size) + ' bytes'

def sftpwalk(remotepath,sftp):
    for f in sftp.listdir_iter(remotepath):
            info = f.st_size
            print(f.filename, " ->>> ", convert_bytes(info))
        #sftpwalk(dl + f.filename + "/")

host="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, 22, username=username, password=password)
print("connected")
sftp = client.open_sftp()

dl = 'C://Users/Administrator/'
sftpwalk(dl,sftp)
client.close()