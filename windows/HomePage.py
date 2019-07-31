# -- coding: utf-8 --
from tkinter import *
from tkinter import filedialog


class HomePage:
    def index(self):
        uploadWindow = Tk()
        uploadWindow.title("SFTP自动上传工具")
        uploadWindow.geometry('600x400')
        uploadWindow.resizable(width=False, height=False)
        # host地址
        Label(uploadWindow, text="HOST地址", pady=5, padx=10).grid(row=0)
        hostInput = Entry(uploadWindow, bd=0, width=70)
        hostInput.grid(row=0, column=1, pady=10, columnspan=2)
        # port
        Label(uploadWindow, text="PORT端口", pady=5, padx=10).grid(row=1)
        portInput = Entry(uploadWindow, bd=0, width=70)
        portInput.grid(row=1, column=1, pady=10, columnspan=2)
        # userName
        Label(uploadWindow, text="用户名", pady=5, padx=10).grid(row=2)
        userInput = Entry(uploadWindow, bd=0, width=70)
        userInput.grid(row=2, column=1, pady=10, columnspan=2)
        # password
        Label(uploadWindow, text="密码", pady=5, padx=10).grid(row=3)
        passwordInput = Entry(uploadWindow, bd=0, width=70)
        passwordInput.grid(row=3, column=1, pady=10, columnspan=2)
        # 密钥文件
        Label(uploadWindow, text="密钥文件", pady=5, padx=10).grid(row=4)
        publicKeyButton = Button(uploadWindow, text="选择文件").grid(row=4, column=1)
        publicKeyButton.bind('<Button-1>', self.showFileDir)
        publicKeyFile = Label(uploadWindow, pady=5, padx=10).grid(row=4, column=2)
        uploadWindow.mainloop()

    @staticmethod
    def showFileDir(event):
        file_path = filedialog.askopenfilename()
        print(event)

