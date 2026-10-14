from OpenGL.GL import *
import glfw
from PIL import Image
from pathlib import Path
class Window:
    def __init__(self,window_width,window_height,gl_clear_color = (1,1,1,1)):
        if not glfw.init():
            raise RuntimeError("Cannot initialize glfw library...")
        BASE_DIR = Path(__file__).parent.parent
        self.window_width = window_width
        self.window_height = window_height
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,6)
        window_icon = Image.open(rf"{BASE_DIR}\icons\robot_icon.png")
        self.window = self.create_window(window_width,window_height)
        self.center_window()
        glfw.set_window_icon(self.window,1,[window_icon])
        glfw.set_framebuffer_size_callback(self.window,self.set_framebuffer_size_callback)
        glfw.make_context_current(self.window)
        glClearColor(*gl_clear_color)
        glViewport(0,0,window_width,window_height)
        glEnable(GL_PROGRAM_POINT_SIZE)
        glEnable(GL_DEPTH_TEST)
    def create_window(self,window_width,window_height):
        window = glfw.create_window(window_width,window_height,"Mapper",None,None)
        if not window:
            glfw.terminate()
            raise RuntimeError("Cannot create glfw window object...")
        return window
    def set_framebuffer_size_callback(self,window,width,height):
        glViewport(0,0,width,height)
        self.window_width = width
        self.window_height = height
        self.center_window()
    def center_window(self):
        monitor = glfw.get_primary_monitor()
        x_pos,y_pos,width,height = glfw.get_monitor_workarea(monitor)
        x_pos = (width - self.window_width) // 2
        y_pos = (height- self.window_height) // 2
        if glfw.get_window_attrib(self.window,glfw.MAXIMIZED):
            glfw.set_window_size(self.window,width,height)
        else:
            glfw.set_window_pos(self.window,x_pos,y_pos)
    def get_window(self):
        return self.window
