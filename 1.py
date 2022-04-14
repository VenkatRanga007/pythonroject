import tempfile
from smb.SMBConnection import SMBConnection

ip="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"

# There will be some mechanism to capture userID, password, client_machine_name, server_name and server_ip
# client_machine_name can be an arbitary ASCII string
# server_name should match the remote machine name, or else the connection will be rejected
conn = SMBConnection(username, password, "test", "Windows_Server", use_ntlm_v2 = True)
assert conn.connect(ip, 139)

file_obj = tempfile.NamedTemporaryFile()
file_attributes, filesize = conn.listPath('smbtest', '', file_obj)

# Retrieved file contents are inside file_obj
# Do what you need with the file_obj and then close it
# Note that the file obj is positioned at the end-of-file,
# so you might need to perform a file_obj.seek() if you need
# to read from the beginning
file_obj.close()