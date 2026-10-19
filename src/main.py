from OpenGL.GL import *
import glfw
import time
from window import Window
from camera import Camera
from shader import Shader
from scene import Scene

class main:
    def __init__(self,window_width,window_height):
        self.window = Window(window_width,window_height).get_window()
        self.camera = Camera(window_width,window_height,4)
        self.shader = Shader()
        self.scene = Scene(500,500)
        self.shader.use()
        self.shader.set_mat4_uniform("Perspective",self.camera.get_perspective())
        self.shader.set_mat4_uniform("View",self.camera.get_view())
    def draw(self):
        start = time.perf_counter()
        counter = 0
        points_to_draw = 0
        poses_to_draw = 0 
        glBindVertexArray(self.scene.get_vao())
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            end = time.perf_counter()
            counter += 1
            if end - start > 1:
                print(f"FPS : {counter}")
                counter = 0
                points = self.scene.generate_map_points(100)
                points_to_draw = self.scene.upload_points(points)
                poses = self.scene.generate_poses(1)
                poses_to_draw = self.scene.upload_pose(poses)
                start = end
            self.shader.set_bool_uniform("DrawPoints",1)
            glDrawArrays(GL_POINTS,0,points_to_draw)
            self.shader.set_bool_uniform("DrawPoints",0)
            glDrawElementsInstanced(GL_LINES,12,GL_UNSIGNED_INT,ctypes.c_void_p(0),poses_to_draw)
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        self.shader.destroy()
        self.scene.destroy()
        glfw.terminate()
if __name__ == "__main__":
    main = main(800,600)
    main.draw()