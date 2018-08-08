# 监控文件变化并上传到sftp

## 使用语言
* python

## 使用组件
* watchdog
* paramiko

## 配置文件
* 文件：./config/config.ini
* 配置说明：
```
[document]
localPath = 本地目录（D:\xxx\）
remotePath = 远程目录（/webser/www/xxx/）

[sftp]
host = sftp的IP地址（127.0.0.1）
port = sftp的端口（22）
publicKey = ssh链接公钥（D:\xxx\id_rsa）
userName = ssh链接用户名
password = ssh链接密码

[exclude]
dir = 要排除上传的文件夹名（.idea,.git）多个用,隔开
file = 要排除上传的文件名（xml___jb_tmp___,php___jb_tmp___,php___jb_old___）
```

