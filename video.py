import cv2


class VideoReader(object):
    def __init__(self):
        self.vid = cv2.VideoCapture(0)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.exit()

    def exit(self):
        print("release")
        self.vid.release()

    def read(self):
        while (True):
            ret, frame = self.vid.read()
            yield ret, frame
