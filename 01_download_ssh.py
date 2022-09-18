#!/usr/bin/env python3

# 01_download_ssh.py

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
    sftp.get(remoteDirectory, localDirectory) # note the differences in distinction to the upload method: get instead of 'put' request and both directories are also twisted.
    sftp.close()
    ssh.close()
    
if __name__ == '__main__':
    filename = ''
    localDirectory = '' + filename
    remoteDirectory = '' + filename

    try:
        download(localDirectory, remoteDirectory)
    except BaseException as err:
        print('Please check the names of the directories and the file to be transfered.', err)
