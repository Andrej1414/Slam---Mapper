from OpenGL.GL import * 
import glfw
from PIL import Image
from pathlib import Path
class main:
    def __init__(self,window_width,window_height):
        if not glfw.init():
            raise RuntimeError("Cannot initialize glfw library.")
        parent_dir = Path(__file__).parent.parent
        self.window_width = window_width
        self.window_height = window_height
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,6)
        img = Image.open(rf"{parent_dir}\icons\robot_icon.png")
        self.window = glfw.create_window(window_width,window_height,"Mapper",None,None)
        if not self.window:
                    glfw.terminate()
        self.center_window()
        glfw.set_window_icon(self.window,1,[img])
        glfw.set_framebuffer_size_callback(self.window,self.set_window_size_callback)
        glfw.make_context_current(self.window)
        glClearColor(1,1,1,1)
        glViewport(0,0,window_width,window_height)
    def set_window_size_callback(self,window,width,height):
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
    def run(self)
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        glfw.terminate()
if __name__ == "__main__":
    main = main(800,600)
    main.run()