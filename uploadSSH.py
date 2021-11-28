#!/usr/bin/env python3

# uploadSSH.py

# Purpose: Upload a file via SSH to remote server.

import os
import paramiko

def upload(localDirectory, remoteDirectory):
    serverIP = ''
    usrname = ''
    passwd = ''
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
    ssh.connect(serverIP, username=usrname, password=passwd)
    sftp = ssh.open_sftp()
    sftp.put(localDirectory, remoteDirectory)
    sftp.close()
    ssh.close()

filename = ''
localDirectory = '' + filename
remoteDirectory = '' + filename

try:
    upload(localDirectory, remoteDirectory)
except BaseException as err:
    print('Please check the names of the directories and the file to be transfered.', err)
