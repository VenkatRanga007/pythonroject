import winrm

host="13.233.255.118"
username="Administration"
password="jTZgcL%sG*gXivzetEQUr9&PxBQyvpUT!"
# Create winrm connection.
sess = winrm.Session('https://13.233.255.118', auth=('Administration', 'jTZgcL%sG*gXivzetEQUr9&PxBQyvpUT!'), transport='kerberos')
result = sess.run_cmd('ipconfig', ['/all'])