from OpenGL.GL import *
import glfw
import numpy as np
class Buffer:
    def __init__(self,poses):
        self.vbo = ctypes.c_uint()
        buffer_size = poses*64 ### REMOVE MAGIC NUMBERS
        test_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        STORAGE_FLAGS = GL_DYNAMIC_STORAGE_BIT
        MAPPING_FLAGS = GL_MAP_WRITE_BIT | GL_MAP_READ_BIT | GL_MAP_COHERENT_BIT | GL_MAP_PERSISTENT_BIT
        self.create_buffer(self.vbo,buffer_size,test_matrix,STORAGE_FLAGS | MAPPING_FLAGS)
        self.buff_ptr = self.map_buffer(self.vbo,0,buffer_size,MAPPING_FLAGS)
    def create_buffer(self,vbo,size,data,flags):
        glCreateBuffers(1,vbo)
        glNamedBufferStorage(vbo,size,data,flags)
    def map_buffer(self,vbo,offset,length,mapping_flags):
        buff_ptr = glMapNamedBufferRange(vbo,offset,length,mapping_flags)
        return buff_ptr
    def get_buff_ptr(self):
        return self.buff_ptr
    def get_vbo(self):
        return self.vbo
    def get_buffer_size(self):
        buffer_size = ctypes.c_uint()
        glGetNamedBufferParameteri64v(self.vbo,GL_BUFFER_SIZE,buffer_size)
        return buffer_size.value
    def destroy(self):
        glDeleteBuffers(1,self.vbo)
if __name__ == "__main__":
    glfw.init()
    glfw.make_context_current(glfw.create_window(800,600,"Test",None,None))
    buffer = Buffer(15)
    print(buffer.get_buffer_size())
    print(buffer.get_vbo())
    print(buffer.get_buff_ptr())
