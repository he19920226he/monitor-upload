# -- coding: utf-8 --
from watchdog.events import LoggingEventHandler


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
            print 'file:' + file_path + ';start upload'
            self.create_dir(file_path)
        else:
            file_path = event.src_path
            print 'file:' + file_path + ';start upload'
            self.upload(file_path)

    def upload(self, file_path):
        upload_path = file_path.replace(self.path, '')
        upload_path = upload_path.replace('\\', '/')
        self.sftp.upload(file_path, upload_path)
        print 'upload success'

    def create_dir(self, dir_path):
        create_dir = dir_path.replace(self.path, '')
        create_dir = create_dir.replace('\\', '/')
        self.sftp.create_dir(create_dir)
