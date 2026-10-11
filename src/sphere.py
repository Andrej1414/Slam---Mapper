from OpenGL.GL import *
import numpy as np
import time

class Sphere:
    def __init__(self):
        self.vertices = []
        self.vertices = np.array(self.make_sphere(2,3))
    def make_sphere(self,circle_res,sphere_res):
        ### USE SPHERICAL COORDINATES BEST
        sphere = []
        if sphere_res % 2  != 1:
            raise Exception("Sphere Res must be odd number")
        angle_inc = 360 / circle_res
        rad_inc = np.deg2rad(angle_inc)
        height = -(sphere_res // 2)
        initial_height = height
        scale_inc = 1/(initial_height-1)
        abs_height = abs(height)
        for circle in range(abs_height):
            for point in range(circle_res):
                if height == 0:
                    x,y = np.cos(point*rad_inc), np.sin(point*rad_inc)
                    z = height
                    sphere.append((x,y,z))
                else:
                    x,y = np.cos(point*rad_inc), np.sin(point*rad_inc)
                    z = height * scale_inc
                    x,y = x*(circle+1)*scale_inc, y*(circle+1)*scale_inc
                    print(x,y,z)
                    sphere.append((x,y,z))
                    x,y = np.cos(point*rad_inc), np.sin(point*rad_inc)
                    z = -(height * scale_inc)
                    x,y = x*(circle+1)*scale_inc, y*(circle+1)*scale_inc
                    sphere.append((x,y,z))
                    print(x,y,z)
            height += 1
        return sphere
if __name__ == '__main__':
    sphere = Sphere()g
    print(sphere.make_sphere(2,5))