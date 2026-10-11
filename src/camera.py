from OpenGL.GL import * 
from pyglm import glm
from shader import Shader
class Camera:
    def __init__(self,aspect_ratio):
        self.perspective = glm.perspective(glm.radians(45),aspect_ratio,0.1,100)
        self.view = glm.translate(glm.mat4(1),glm.vec3(0,0,-3))
    def set_projection(self,aspect_ratio):
        self.perspective = glm.perspective(glm.radians(45),aspect_ratio,0.1,100)
    def get_perpective(self):
        return self.perspective
    def get_view(self):
        return self.view
