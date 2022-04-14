import pysftp

host="3.109.121.57"
username="Administrator"
password="Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK"

cnopts = pysftp.CnOpts(knownhosts='known_hosts')
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=host, username=username, password=password) as sftp:
    print("Connection successfully established ... ")
# Switch to a remote directory
sftp.cwd('C://Users/Administrator/**/*')

# Obtain structure of the remote directory '/opt'
directory_structure = sftp.listdir_attr()

# Print data
for attr in directory_structure:
    print(attr.filename, attr)