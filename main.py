from video import VideoReader
import cv2

if __name__ == '__main__':
    vr = VideoReader()

    for (ret, frame) in vr.read():
        # cv2.imshow('frame', frame)

        if vr.exit_condition():
            break

    vr.exit()
