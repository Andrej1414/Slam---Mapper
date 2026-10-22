import glfw
from OpenGL.GL import *
from pyglm import glm

class Camera:
    def __init__(self,window_width,window_height,camera_speed):
        self.camera_speed = camera_speed
        self.aspect_ratio = window_width / window_height
        self.last_x_pos = window_width / 2
        self.last_y_pos = window_height / 2
        self.camera_pos = glm.vec3(0,0,0)
        self.camera_front = glm.vec3(0,0,-1)
        self.WORLD_UP = glm.vec3(0,1,0)
        self.camera_up = glm.vec3(0,1,0)
        self.camera_right = glm.normalize(glm.cross(self.camera_front,self.camera_up))
        self.set_view()
        self.fov = 45
        self.first_movement = False
        self.yaw = 0 
        self.pitch = 90
        self.set_perspective()
    def get_view(self):
        return self.view
    def get_perspective(self):
        return self.perspective
    def set_view(self):
        self.view = glm.lookAt(self.camera_pos,self.camera_pos + self.camera_front,self.camera_up)
    def set_perspective(self):
        self.perspective = glm.perspective(glm.radians(self.fov),self.aspect_ratio,0.1,100)
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
    def mouse_callback(self,window,x_pos,y_pos):
        if not self.first_movement:
            self.last_x_pos = x_pos
            self.last_y_pos = y_pos
            self.first_movement = True
        x_offset = x_pos - self.last_x_pos
        y_offset = self.last_y_pos - y_pos
        self.last_x_pos = x_pos
        self.last_y_pos = y_pos
        x_offset *= 0.05
        y_offset *= 0.05 
        self.yaw += x_offset
        self.pitch += y_offset
        if self.pitch > 89:
            self.pitch = 89
        if self.pitch < -89:
            self.pitch = -89
        self.update_view_params()
    def scroll_callback(self,window,x_offset,y_offset):
        self.fov -= y_offset
        if self.fov < 1:
            self.fov = 1
        if self.fov > 45:
            self.fov = 45
    def update_view_params(self):
        camera_front = glm.vec3()
        camera_front.x = glm.cos(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        camera_front.y = glm.sin(glm.radians(self.pitch))
        camera_front.z = glm.sin(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        self.camera_front = glm.normalize(camera_front)
        self.camera_right = glm.normalize(glm.cross(camera_front,self.WORLD_UP))
        self.camera_up = glm.normalize(glm.cross(self.camera_right,self.camera_front))
