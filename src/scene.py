from OpenGL.GL import *
import glfw 
import numpy as np
import random
from map_point import MapPoint
from buffer import Buffer
from shader import Shader
class Scene:
    def __init__(self,n_map_points):
        self.shader = Shader()
        self.buffer = Buffer(n_map_points)
        self.map_point = MapPoint(self.buffer.get_vbo())
        self.point_starting_address = self.buffer.get_buff_ptr()
        buffer_size = self.buffer.get_buffer_size()
        self.mapping_region = buffer_size + self.point_starting_address
        self.point_offset = 0
        self.n_map_points = n_map_points
        self.points_drawn = 0
        self.shader.use()
    def upload_map_points(self,map_points,max_points):
        map_points = np.array(map_points,np.float32)
        map_points_size = map_points.nbytes
        dst = self.point_starting_address + self.point_offset + map_points_size
        if dst > self.mapping_region:
            self.point_offset = 0
        ctypes.memmove(
            ctypes.c_void_p(self.point_starting_address + self.point_offset),
            map_points.ctypes.data,
            map_points.nbytes   
        )
        self.point_offset += map_points.nbytes
        self.points_drawn += map_points.__len__()
        if self.points_drawn > max_points:
            self.points_drawn = max_points
        return self.points_drawn
    def generate_map_point(self,samples):
        map_points = []
        for sample in range(samples):
            map_point = [random.uniform(-1,1),random.uniform(-1,1),0]
            map_points.append(map_point)
        return map_points
    def get_n_map_points(self):
        return self.n_map_points
    def get_map_point_vao(self):
        return self.map_point.get_vao()
    def destroy(self):
        self.shader.delete_program()
        self.buffer.destroy()
        self.map_point.destroy()
if __name__ == "__main__":
    glfw.init()
    glfw.make_context_current(glfw.create_window(800,600,"Test",None,None))
    scene = Scene(10)
    map_points = scene.generate_map_point(5)
    

    
