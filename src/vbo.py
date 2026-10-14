from OpenGL.GL import *

class Vbo:
    def __init__(self,n_poses,n_points):
        self.STORAGE_FLAGS = GL_DYNAMIC_STORAGE_BIT
        self.MAPPING_FLAGS = GL_MAP_READ_BIT | GL_MAP_WRITE_BIT | GL_MAP_COHERENT_BIT | GL_MAP_PERSISTENT_BIT
        self.point_region_size = n_points * 12
        self.pose_region_size = n_poses * 64
        self.vbo_size = self.point_region_size + self.pose_region_size
        self.create_buffer()
        self.buffer_ptr =  self.map_buffer()
    def create_buffer(self):
        self.vbo = ctypes.c_uint()
        glCreateBuffers(1,self.vbo)
        glNamedBufferStorage(self.vbo,self.vbo_size,None,self.STORAGE_FLAGS | self.MAPPING_FLAGS)
    def map_buffer(self):
        buffer_ptr = glMapNamedBufferRange(self.vbo,0,self.vbo_size,self.MAPPING_FLAGS)
        return buffer_ptr
    def get_point_region(self):
        return self.point_region_size
    def get_pose_region(self):
        return self.pose_region_size
    def destroy(self):
        glDeleteBuffers(1,self.vbo)
    def get_buff_ptr(self):
        return self.buffer_ptr
    def get_vbo(self):
        return self.vbo
    def get_vbo_size(self):
        size = ctypes.c_uint()
        glGetNamedBufferParameteri64v(self.vbo,GL_BUFFER_SIZE,size)
        return size
        