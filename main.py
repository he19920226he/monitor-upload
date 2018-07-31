# -- coding: utf-8 --
from helpers.Config import Config
import paramiko

if __name__ == "__main__":
    config = Config()
    # 获取要监控的目录
    local_path = config.get_config('document', 'localPath', '')
    print '要监控的目录:' + local_path
    # 获取sftp配置
    sftp_host = config.get_config('sftp', 'host', '')
    sftp_port = config.get_config('sftp', 'port', '')
    sftp_user_name = config.get_config('sftp', 'userName', '')
    sftp_public_key = config.get_config('sftp', 'publicKey', '')
    sftp_user_password = config.get_config('sftp', 'password', None)
    remote_path = config.get_config('document', 'remotePath', '')
    if local_path == '' or remote_path == '':
        print '请配置本地目录和远程目录'
        exit()
    if sftp_host == ''or sftp_port == '' or sftp_user_name == '':
        print 'SFTP配置错误'
        exit()

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
                print '没有公钥时密码必须配置'
                exit()
            ssh.connect(sftp_host, sftp_port, sftp_user_name, sftp_user_password)
    except paramiko.ssh_exception.AuthenticationException:
        print 'sftp链接失败'
        exit()

    transport = ssh.get_transport()
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.stat(remote_path)
    except IOError:
        print '远程目录不存在，创建目录'
        sftp.mkdir(remote_path)

    try:
        local_file = local_path + 'test.py'
        remote_file = remote_path + 'test.py'
        sftp.put(local_file, remote_file)
    except WindowsError:
        print '上传失败'
    print '上传成功'