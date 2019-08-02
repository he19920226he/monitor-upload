# -- coding: utf-8 --
from tkinter import *
from tkinter import filedialog
from helpers.Config import Config


class HomePage:
    def __init__(self):
        global upload_tk
        global config
        config = Config()
        upload_tk = Tk()
        self.host = StringVar()
        self.port = StringVar()
        self.user_name = StringVar()
        self.password = StringVar()
        self.public_key_path = StringVar()
        self.local_document = StringVar()
        self.remote_document = StringVar()
        self.exclude_dir = StringVar()
        self.exclude_file = StringVar()
        self.build_by_config()
        self.index()
        upload_tk.mainloop()

    def build_by_config(self):
        global config
        self.host.set(config.get_config('sftp', 'host'))
        self.port.set(config.get_config('sftp', 'port'))
        self.user_name.set(config.get_config('sftp', 'user_name'))
        self.password.set(config.get_config('sftp', 'password'))
        self.public_key_path.set(config.get_config('sftp', 'public_key'))
        self.local_document.set(config.get_config('document', 'local_path'))
        self.remote_document.set(config.get_config('document', 'remote_path'))
        self.exclude_dir.set(config.get_config('exclude', 'dir'))
        self.exclude_file.set(config.get_config('exclude', 'file'))

    def index(self):
        global upload_tk
        upload_tk.title("SFTP自动上传工具")
        upload_tk.geometry('800x500')
        upload_tk.resizable(width=False, height=False)
        # host地址
        Label(upload_tk, text="HOST地址", pady=5, padx=10).grid(row=0)
        host_input = Entry(upload_tk, bd=1, width=70, textvariable=self.host)
        host_input.grid(row=0, column=1, pady=10, columnspan=2)
        # port
        Label(upload_tk, text="PORT端口", pady=5, padx=10).grid(row=1)
        port_input = Entry(upload_tk, bd=1, width=70, textvariable=self.port)
        port_input.grid(row=1, column=1, pady=10, columnspan=2)
        # userName
        Label(upload_tk, text="用户名", pady=5, padx=10).grid(row=2)
        user_input = Entry(upload_tk, bd=1, width=70, textvariable=self.user_name)
        user_input.grid(row=2, column=1, pady=10, columnspan=2)
        # password
        Label(upload_tk, text="密码", pady=5, padx=10).grid(row=3)
        password_input = Entry(upload_tk, bd=1, width=70, textvariable=self.password, show='*')
        password_input.grid(row=3, column=1, pady=10, columnspan=2)
        # 密钥文件
        Label(upload_tk, text="密钥文件", pady=5, padx=10).grid(row=4)
        Button(upload_tk, text="选择文件", command=self.show_file_dir).grid(row=4, column=1)
        Label(upload_tk, textvariable=self.public_key_path, pady=5, padx=10).grid(row=4, column=2)
        # 本地目录
        Label(upload_tk, text="本地目录", pady=5, padx=10).grid(row=5)
        local_document = Entry(upload_tk, bd=1, width=70, textvariable=self.local_document)
        local_document.grid(row=5, column=1, pady=10, columnspan=2)
        # 远程目录
        Label(upload_tk, text="远程目录", pady=5, padx=10).grid(row=6)
        remote_document = Entry(upload_tk, bd=1, width=70, textvariable=self.remote_document)
        remote_document.grid(row=6, column=1, pady=10, columnspan=2)
        # 过滤的目录
        Label(upload_tk, text="过滤的目录", pady=5, padx=10).grid(row=7)
        exclude_dir = Entry(upload_tk, bd=1, width=70, textvariable=self.exclude_dir)
        exclude_dir.grid(row=7, column=1, pady=10, columnspan=2)
        # 过滤的文件
        Label(upload_tk, text="过滤的文件", pady=5, padx=10).grid(row=8)
        exclude_file = Entry(upload_tk, bd=1, width=70, textvariable=self.exclude_file)
        exclude_file.grid(row=8, column=1, pady=10, columnspan=2)
        Button(upload_tk, text="开始上传", command=self.begin_upload).grid(row=9, column=1, columnspan=3)

    def show_file_dir(self):
        file_path = filedialog.askopenfilename()
        self.public_key_path.set(file_path)

    def begin_upload(self):
        self.update_config()

    def update_config(self):
        global config
        config.set_config('sftp', 'host', self.host.get())
        config.set_config('sftp', 'port', self.port.get())
        config.set_config('sftp', 'user_name', self.user_name.get())
        config.set_config('sftp', 'password', self.password.get())
        config.set_config('sftp', 'public_key', self.public_key_path.get())
        config.set_config('document', 'local_path', self.local_document.get())
        config.set_config('document', 'remote_path', self.remote_document.get())
        config.set_config('exclude', 'dir', self.exclude_dir.get())
        config.set_config('exclude', 'file', self.exclude_file.get())
