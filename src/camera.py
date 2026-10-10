from OpenGL.GL import * 
from pyglm import glm

class Camera:
    def __init__(self,aspect_ratio):
        self.projection = glm.perspective(glm.radians(45),aspect_ratio,0.1,100)
        self.view = glm.mat4(1)
        self.view = glm.translate(self.view,glm.vec3(0,0,-3))
    def set_uniforms(self,projection_loc,view_loc):
        glUniformMatrix4fv(projection_loc,1,GL_FALSE,glm.value_ptr(self.projection))
        glUniformMatrix4fv(view_loc,1,GL_FALSE,glm.value_ptr(self.view))
    def set_projection(self,aspect_ratio):
        self.projection = glm.perspective(glm.radians(45),aspect_ratio,0.1,100)
