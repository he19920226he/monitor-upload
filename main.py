# -- coding: utf-8 --
# from helpers.Config import Config
# from helpers.Sftp import Sftp
# from helpers.Watchdog import Watchdog
# import time
from windows.HomePage import HomePage

if __name__ == "__main__":
    # config = Config()
    # # 获取要监控的目录
    # local_path = config.get_config('document', 'localPath', '')
    # print('watch dir:' + local_path + '...................')
    # # 获取sftp配置
    # remote_path = config.get_config('document', 'remotePath', '')
    # if local_path == '' or remote_path == '':
    #     print('path error..................')
    #     time.sleep(5)
    #     exit()
    # # sftp链接
    # sftp = Sftp(remote_path)
    # sftp.check_remote_path()
    # # watchdog监控文件
    # dog = Watchdog(local_path, sftp)
    # dog.start()
    homePage = HomePage()

