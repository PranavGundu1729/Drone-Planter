""" This is the main camera class, which all codes will use to control and operate the camera of the drone. """
from cv2 import *
import time

class Camera:
    def __init__(self):
        self.camPort = 0
        self.camera = VideoCapture(self.camPort)

    def takePicture(self, show=True, save=True):
        result, image = self.camera.read()
        if result:
            if show:
                imshow(time.ctime(), image)
            if save:
                imwrite(time.ctime()+".png")
