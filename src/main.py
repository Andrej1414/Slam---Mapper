from OpenGL.GL import * 
import glfw
from pyglm import glm

import time
from PIL import Image
from pathlib import Path
from scene import Scene
class main:
    def __init__(self,window_width,window_height):
        if not glfw.init():
            raise RuntimeError("Cannot initialize glfw library.")
        BASE_DIR = Path(__file__).parent.parent
        self.window_width = window_width
        self.window_height = window_height
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,6)
        img = Image.open(rf"{BASE_DIR}\icons\robot_icon.png")
        self.window = glfw.create_window(window_width,window_height,"Mapper",None,None)
        if not self.window:
             glfw.terminate()
        self.center_window()
        glfw.set_window_icon(self.window,1,[img])
        glfw.set_framebuffer_size_callback(self.window,self.set_window_size_callback)
        glfw.make_context_current(self.window)
        glClearColor(1,1,1,1)
        glViewport(0,0,window_width,window_height)
        glEnable(GL_DEPTH_TEST)
        self.scene = Scene(1000)
        self.scene.use_shader()
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
    def run(self):
        glBindVertexArray(self.scene.get_vao())
        counter = 0
        start = time.perf_counter()
        poses_to_draw = 0
        view_loc = glGetUniformLocation(self.scene.shader.id,"view")
        trans = glm.mat4(1)

        trans = glm.translate(trans,glm.vec3(0,0,-3))
        glUniformMatrix4fv(view_loc,1,GL_FALSE,glm.value_ptr(trans))
        projection_loc = glGetUniformLocation(self.scene.shader.id,'perspective')
        projection = glm.perspective(glm.radians(45.0), 800.0 / 600.0, 0.1, 100.0)
        glUniformMatrix4fv(projection_loc,1,GL_FALSE,glm.value_ptr(projection))

        print(trans)
        setted = False
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            end = time.perf_counter()
            counter += 1
            if end - start > 0.5:
                print(f"FPS : {counter} ")
                counter = 0
                if setted == False:
                    pose = self.scene.generate_poses(100)
                    #pose = self.scene.generate_identity()
                    poses_to_draw = self.scene.upload_pose(pose,1000)
                    #setted = True
                start = end
            glDrawElementsInstanced(GL_LINES,12,GL_UNSIGNED_INT,ctypes.c_void_p(0),poses_to_draw)    
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        self.scene.destroy()
        glfw.terminate()
if __name__ == "__main__":
    main = main(800,600)
    main.run()