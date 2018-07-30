from helpers.Config import Config


if __name__ == "__main__":
    config = Config()
    # 获取要监控的目录
    watch_path = config.get_config('document', 'path')
    print '要监控的目录:' + watch_path
    # 获取sftp配置
    sftp_host = config.get_config('sftp', 'host')
    sftp_port = config.get_config('sftp', 'post')
    sftp_user_name = config.get_config('sftp', 'userName')
    if sftp_host == ''or sftp_port == '' or sftp_user_name:
        print 'SFTP配置错误'
