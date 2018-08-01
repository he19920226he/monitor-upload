# -- coding: utf-8 --
from watchdog.events import LoggingEventHandler
from Config import Config

class FileHandler(LoggingEventHandler):
    def __init__(self, path, sftp):
        self.sftp = sftp
        self.path = path

    def on_created(self, event):
        self.upload_file_or_dir(event)

    def on_modified(self, event):
        self.upload_file_or_dir(event)

    def on_moved(self, event):
        self.upload_file_or_dir(event)

    def upload_file_or_dir(self, event):
        if event.is_directory:
            file_path = event.dest_path
            if self.check_exclude(file_path) is False:
                print 'file:' + file_path + ';start upload'
                self.create_dir(file_path)
        else:
            file_path = event.src_path
            if self.check_exclude(file_path) is False:
                print 'file:' + file_path + ';start upload'
                self.upload(file_path)

    def check_exclude(self, path):
        config = Config()
        exclude_dir = config.get_config('exclude', 'dir', '')
        is_exclude = False
        print(exclude_dir)
        if exclude_dir != '':
            exclude_dir = list(exclude_dir)
            print(exclude_dir)
            for dir_name in exclude_dir:
                print dir_name
                if path.index(dir_name) > -1:
                    is_exclude = True
        exclude_file = config.get_config('exclude', 'file', '')
        if exclude_file != '':
            exclude_file = list(exclude_file)
            for file_name in exclude_file:
                if path.index(file_name) > -1:
                    is_exclude = True
        return is_exclude

    def upload(self, file_path):
        upload_path = file_path.replace(self.path, '')
        upload_path = upload_path.replace('\\', '/')
        self.sftp.upload(file_path, upload_path)
        print 'upload success'

    def create_dir(self, dir_path):
        create_dir = dir_path.replace(self.path, '')
        create_dir = create_dir.replace('\\', '/')
        self.sftp.create_dir(create_dir)
