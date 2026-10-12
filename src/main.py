from OpenGL.GL import *
import glfw
import time
import numpy as np
from pyglm import glm
from window import Window
from scene import Scene
from camera import Camera
from shader import Shader

class main:
    def __init__(self,window_width,window_height):
        self.window = Window(window_width,window_height).get_window()
        self.scene = Scene(n_poses=1000)
        self.camera = Camera(window_width/window_height)
        self.shader = Shader()
        self.shader.use()
        self.shader.set_uniform("perspective",self.camera.get_perpective())
        self.shader.set_uniform("view",self.camera.get_view())
        
        self.render()
    def render(self):
        start = time.perf_counter()
        poses_drawn = 0
        counter = 0
    
        glBindVertexArray(self.scene.get_vao())
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            end = time.perf_counter()
            counter += 1
            if end - start > 1:
                print(f"FPS:{counter}")
                counter = 0
                poses = self.scene.generate_poses(1)
                poses_drawn = self.scene.upload_pose(poses)
                start = end
            glDrawElementsInstanced(GL_LINES,12,GL_UNSIGNED_INT,ctypes.c_void_p(0),poses_drawn)
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        self.scene.destroy()
        self.shader.destroy()
        glfw.terminate()
if __name__ == "__main__":
    main = main(800,600)
    

