# -- coding: utf-8 --
from helpers.Config import Config
import paramiko
import os
from paramiko.ssh_exception import (
    SSHException, NoValidConnectionsError
)


class Sftp(object):
    def __init__(self, remote_path):
        self.config = Config()
        self.remote_path = remote_path
        self.sftp = None

    def connection(self):
        print('start connection sftp............')
        sftp_host = self.config.get_config('sftp', 'host', '')
        sftp_port = self.config.get_config('sftp', 'port', '')
        sftp_user_name = self.config.get_config('sftp', 'user_name', '')
        sftp_public_key = self.config.get_config('sftp', 'public_key', '')
        sftp_user_password = self.config.get_config('sftp', 'password', None)
        if sftp_host == '' or sftp_port == '' or sftp_user_name == '':
            return False
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if sftp_public_key != '':
                if sftp_user_password is None:
                    key = paramiko.RSAKey.from_private_key_file(sftp_public_key)
                else:
                    key = paramiko.RSAKey.from_private_key_file(sftp_public_key, sftp_user_password)
                ssh.connect(sftp_host, sftp_port, sftp_user_name, sftp_user_password, key)
            else:
                if sftp_user_password is None:
                    return False
                ssh.connect(sftp_host, sftp_port, sftp_user_name, sftp_user_password)
        except paramiko.ssh_exception.AuthenticationException:
            print(111)
            return False
        except NoValidConnectionsError:
            print(233333)
            return False
        transport = ssh.get_transport()
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp

    def check_remote_path(self):
        try:
            self.sftp.stat(self.remote_path)
        except IOError:
            print('remote dir is undefined,create new dir')
            self.sftp.mkdir(self.remote_path)

    def check_dir(self, folder):
        try:
            self.sftp.stat(folder)
        except IOError:
            print('remote dir is undefined,create new dir:' + folder)
        except SSHException:
            print('sftp connection dropped........')
            print('connection sftp server again.........')
            if not self.sftp:
                self.sftp = self.connection()
            self.check_dir(folder)

    def upload(self, local_path, upload_path):
        try:
            local_file = local_path
            remote_file = self.remote_path + upload_path
            remote_dir = os.path.dirname(remote_file)
            self.check_dir(remote_dir)
            print('upload to file:' + remote_file)
            self.sftp.put(local_file, remote_file)
            print('upload success')
        except WindowsError:
            print('sftp upload error')
        except SSHException:
            print('sftp connection dropped........')
            print('connection sftp server again.........')
            self.sftp = self.connection()
            self.upload(local_path, upload_path)
        except IOError:
            print('sftp upload error')

    def create_dir(self, dir_name):
        remote_dir = self.remote_path + dir_name
        try:
            self.sftp.stat(remote_dir)
            print('dir exist')
        except IOError as error:
            print('IO ERROR........' + error.message)
        except SSHException:
            print('sftp connection dropped........')
            print('connection sftp server again.........')
            self.sftp = self.connection()
