import glfw
import time
from pyglm import glm
from OpenGL.GL import *
from window import Window
from shader import Shader
from scene import Scene
from camera import Camera
from renderer import Renderer

class main:
    def __init__(self,window_width,window_height):
        self.window_obj = Window(window_width,window_height)
        self.camera = Camera(window_width,window_height,0.004)
        self.window_obj.set_cursor_pos_callback(self.camera.mouse_callback)
        self.window_obj.set_scroll_callback(self.camera.scroll_callback)
        self.window = self.window_obj.get_window()
        self.scene = Scene(500,500)
        self.shader = Shader()
        self.shader.use()
        self.shader.set_mat4_uniform("Perspective",self.camera.get_perspective())
        self.shader.set_mat4_uniform("View",self.camera.get_view())
        self.renderer = Renderer()
    def draw(self):
        start = time.perf_counter()
        counter = 0
        points_to_draw = 0
        poses_to_draw = 0 
        bool_loc = self.shader.get_uniform_loc("DrawPoints")
        view_loc = self.shader.get_uniform_loc("View")
        perspective_loc = self.shader.get_uniform_loc("Perspective")
        glBindVertexArray(self.scene.get_vao())
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            end = time.perf_counter()
            counter += 1
            self.camera.process_input(self.window)
            self.camera.set_view()
            view = self.camera.get_view()
            self.camera.set_perspective()
            perspective = self.camera.get_perspective()
            glUniformMatrix4fv(view_loc,1,GL_FALSE,glm.value_ptr(view))
            glUniformMatrix4fv(perspective_loc,1,GL_FALSE,glm.value_ptr(perspective))
            if end - start > 1:
                print(f"FPS : {counter}")
                counter = 0
                points = self.scene.generate_map_points(100)
                points_to_draw = self.scene.upload_points(points,self.scene.n_points)
                poses = self.scene.generate_poses(1)
                poses_to_draw = self.scene.upload_pose(poses,self.scene.n_poses)
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