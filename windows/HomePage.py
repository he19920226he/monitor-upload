# -- coding: utf-8 --
from tkinter import *
from tkinter import filedialog


class HomePage:
    def __init__(self):
        global upload_tk
        upload_tk = Tk()
        self.public_key_path = StringVar()
        self.index()
        upload_tk.mainloop()

    def index(self):
        global upload_tk
        upload_tk.title("SFTP自动上传工具")
        upload_tk.geometry('800x400')
        upload_tk.resizable(width=False, height=False)
        # host地址
        Label(upload_tk, text="HOST地址", pady=5, padx=10).grid(row=0)
        host_input = Entry(upload_tk, bd=1, width=70)
        host_input.grid(row=0, column=1, pady=10, columnspan=2)
        # port
        Label(upload_tk, text="PORT端口", pady=5, padx=10).grid(row=1)
        port_input = Entry(upload_tk, bd=1, width=70)
        port_input.grid(row=1, column=1, pady=10, columnspan=2)
        # userName
        Label(upload_tk, text="用户名", pady=5, padx=10).grid(row=2)
        user_input = Entry(upload_tk, bd=1, width=70)
        user_input.grid(row=2, column=1, pady=10, columnspan=2)
        # password
        Label(upload_tk, text="密码", pady=5, padx=10).grid(row=3)
        password_input = Entry(upload_tk, bd=1, width=70)
        password_input.grid(row=3, column=1, pady=10, columnspan=2)
        # 密钥文件
        Label(upload_tk, text="密钥文件", pady=5, padx=10).grid(row=4)
        Button(upload_tk, text="选择文件", command=self.show_file_dir).grid(row=4, column=1)
        Label(upload_tk, textvariable=self.public_key_path, pady=5, padx=10).grid(row=4, column=2)

    def show_file_dir(self):
        file_path = filedialog.askopenfilename()
        self.public_key_path.set(file_path)
