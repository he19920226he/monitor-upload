# -- coding: utf-8 --
import time
from watchdog.observers import Observer
from FileHandler import FileHandler


class Watchdog(object):
    def __init__(self, path, sftp):
        self.path = path
        self.observer = Observer()
        self.handler = FileHandler(path, sftp)

    def start(self):
        self.observer.schedule(self.handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
