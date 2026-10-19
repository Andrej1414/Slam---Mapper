from OpenGL.GL import *
import glfw
import time
import numpy as np
from pyglm import glm
from window import Window
from camera import Camera
from shader import Shader
from scene import Scene
from renderer import Renderer

class main:
    def __init__(self,window_width,window_height):
        self.window = Window(window_width,window_height).get_window()
        self.camera = Camera(window_width,window_height,0.004)
        self.shader = Shader()
        self.scene = Scene(500,5)
        self.shader.use()
        self.shader.set_mat4_uniform("Perspective",self.camera.get_perspective())
        self.shader.set_mat4_uniform("View",self.camera.get_view())
        self.renderer = Renderer(5)
    def draw(self):
        start = time.perf_counter()
        counter = 0
        points_to_draw = 0
        poses_to_draw = 0 
        glBindVertexArray(self.scene.get_vao())
        bool_loc = self.shader.get_uniform_loc("DrawPoints")
        #glfw.swap_interval(1)
        mat_loc = self.shader.get_uniform_loc("View")
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            end = time.perf_counter()
            counter += 1
            self.camera.process_input(self.window)
            view = self.camera.construct_view()
            glUniformMatrix4fv(mat_loc,1,GL_FALSE,glm.value_ptr(view))
            if end - start > 1:
                print(f"FPS : {counter}")
                counter = 0
                points = self.scene.generate_map_points(1000)
                points_to_draw = self.scene.upload_points(points,5)
                poses = self.scene.generate_poses(1)
                poses_to_draw = self.scene.upload_pose(poses)
                start = end
            self.renderer.draw_points(bool_loc,points_to_draw)
            self.renderer.draw_pose(bool_loc,12,poses_to_draw)
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        self.shader.destroy()
        self.scene.destroy()
        glfw.terminate()
if __name__ == "__main__":
    main = main(800,600)
    main.draw()