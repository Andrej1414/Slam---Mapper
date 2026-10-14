from OpenGL.GL import *
from pyglm import glm

class Camera:
    def __init__(self,window_width,window_height):
        aspect_ratio = window_width / window_height
        self.view = glm.translate(glm.mat4(1),glm.vec3(0,0,-3))
        self.perspective = glm.perspective(glm.radians(60),aspect_ratio,0.1,100)
    def get_view(self):
        return self.view
    def get_perspective(self):
        return self.perspective