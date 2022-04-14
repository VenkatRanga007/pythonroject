import paramiko
try:
    # And create a client instance.
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to our client; you will need
    # to know/use for the remote account:
    #
    #   IP/Hostname of target
    #   A username
    #   A password
    client.connect('3.109.121.57', username='Administrator', password='Up3HNKGL-22f3ES-u%Fz)YJUMNcx%uDK')
    print("Connected to 13.233.255.118")
    # Assign our input, output and error variables to
    # to a command we will be issuing to the remote
    # system
    stdin, stdout, stderr = client.exec_command(
        'pwd'
    )
    print(stdout)
    # And finally we close the connection to our client
    client.close()
except paramiko.AuthenticationException:
    print("Failed to connect to  due to wrong username/password")
    exit(1)
except Exception as e:
    print(e.message)
    exit(2)