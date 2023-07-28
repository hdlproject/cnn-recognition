from video import VideoReader
import cv2

if __name__ == '__main__':
    vr = VideoReader()

    for (ret, frame) in vr.read():
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
