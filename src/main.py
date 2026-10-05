from OpenGL.GL import * 
import glfw
from PIL import Image
from pathlib import Path
class main:
    def __init__(self,window_width,window_height):
        if not glfw.init():
            raise RuntimeError("Cannot initialize glfw library.")
        parent_dir = Path(__file__).parent.parent
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,6)
        img = Image.open(rf"{parent_dir}\icons\robot_icon.png")
        self.window = glfw.create_window(window_width,window_height,"Mapper",None,None)
        glfw.set_window_icon(self.window,1,[img])
        glfw.make_context_current(self.window)
        glClearColor(1,1,1,1)
        glViewport(0,0,window_width,window_height)
        if not self.window:
            glfw.terminate()
    def run(self):
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        glfw.terminate()

if __name__ == "__main__":
    main = main(800,600)
    main.run()