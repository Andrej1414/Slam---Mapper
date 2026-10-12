from OpenGL.GL import *
import glfw
from window import Window
from camera import Camera
from shader import Shader

class main:
    def __init__(self,window_width,window_height):
        self.window = Window(window_width,window_height).get_window()
        self.camera = Camera(window_width,window_height)
        self.shader = Shader()
        self.shader.use()
        self.shader.set_mat4_uniform("perspective",self.camera.get_perspective())
        self.shader.set_mat4_uniform("view",self.camera.get_view())
    def draw(self):
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        self.shader.destroy()
        glfw.terminate()
if __name__ == "__main__":
    main = main(800,600)
    main.draw()