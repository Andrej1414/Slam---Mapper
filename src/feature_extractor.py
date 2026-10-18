import cv2 as cv
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt

class OrbExtractor:
    def __init__(self):
        self.orb = cv.ORB.create(30000000)
        self.sift = cv.SIFT.create(1000000)
        self.ROOT_PATH = Path(__file__).parent.parent
    def load_img(self,img_path):
        img = cv.imread(rf"{self.ROOT_PATH / img_path}")
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.img_width = img.shape[1]
        self.img_height = img.shape[0]
        return img
    def extract_keypoints(self,img):
        keypoints = self.orb.detect(img,None)
        #keypoints = self.sift.detect(img,None)
        return keypoints
    def show_kp_img(self,keypoints,img):
        img = cv.drawKeypoints(img,keypoints,None,(0,255,0),0)
        plt.imshow(img),plt.show()
    def extract_color(self,keypoints,img_mat):
        point_coords = []
        point_color = []
        low = -1
        high = 1
        for point in keypoints:
            point_coords.append(point.pt)
        for point in point_coords:
            x = int(point[0])
            y = int(point[1])
            z = 0
            color_point = img_mat[y][x] / 255
            point_color.append([low + (x/self.img_width)*(high-low),-(low+(y/self.img_height)*(high-low)),z])
            point_color.append(color_point)
        point_color = np.array(point_color,np.float32)
        return point_color
if __name__ == "__main__":
    orb = OrbExtractor()
    img = orb.load_img(r"images\Colosseo_2020.jpg")
    keypoints = orb.extract_keypoints(img)
    keypoints = np.array(keypoints)
    points = orb.extract_color(keypoints,img)
    print(points[0])
    orb.show_kp_img(keypoints,img)