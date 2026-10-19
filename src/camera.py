from OpenGL.GL import *
from pyglm import glm
import glfw

class Camera:
    def __init__(self,window_width,window_height,camera_speed):
        aspect_ratio = window_width / window_height
        self.camera_speed = camera_speed
        self.camera_pos = glm.vec3(0,0,3)
        self.camera_front = glm.vec3(0,0,-1)
        self.camera_up = glm.vec3(0,1,0)
        self.view = glm.lookAt(self.camera_pos,
                               self.camera_pos + self.camera_front,
                               self.camera_up)
        self.camera_right = glm.normalize(glm.cross(self.camera_front,self.camera_up))
        self.perspective = glm.perspective(glm.radians(60),aspect_ratio,0.1,100)
    def process_input(self,window):
        camera_speed = self.camera_speed
        if glfw.get_key(window,glfw.KEY_W) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_front
        if glfw.get_key(window,glfw.KEY_S) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_front
        if glfw.get_key(window,glfw.KEY_D) == glfw.PRESS:
            self.camera_pos += self.camera_right * camera_speed
        if glfw.get_key(window,glfw.KEY_A) == glfw.PRESS:
            self.camera_pos -= self.camera_right * camera_speed
    def construct_view(self):
        self.view = glm.lookAt(self.camera_pos,
                               self.camera_pos + self.camera_front,
                               self.camera_up)
        return self.view
    def get_view(self):
        return self.view
    def get_perspective(self):
        return self.perspective