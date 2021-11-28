#!/usr/bin/env python3

# downloadSSH.py

# Purpose: Download a file via SSH from a remote server.

import os
import paramiko

def download(localDirectory, remoteDirectory):
    serverIP = '' # Server IP address goes in here
    usrname = ''
    passwd = ''
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
    ssh.connect(serverIP, username=usrname, password=passwd)
    sftp = ssh.open_sftp()
    sftp.get(remoteDirectory, localDirectory)
    sftp.close()
    ssh.close()

filename = ''
localDirectory = '' + filename
remoteDirectory = '' + filename

try:
    download(localDirectory, remoteDirectory)
except BaseException as err:
    print('Please check the name of the directory and the file.', err)
