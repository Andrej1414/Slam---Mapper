from OpenGL.GL import *
import numpy as np

class MapPoint:
    def __init__(self,buffer):
        MAP_POINT_SIZE = 3 * 4
        MAP_POINT_DIM = 3
        self.vao = ctypes.c_uint()
        glCreateVertexArrays(1,self.vao)
        self.setup_vert_attrib(buffer,MAP_POINT_SIZE,MAP_POINT_DIM)
    def setup_vert_attrib(self,buffer,stride,vert_dim):
        glVertexArrayVertexBuffer(self.vao,0,buffer,0,stride)
        glEnableVertexArrayAttrib(self.vao,0)
        glVertexArrayAttribFormat(self.vao,0,vert_dim,GL_FLOAT,GL_FALSE,0)
        glVertexArrayAttribBinding(self.vao,0,0)
    def get_vao(self):
        return self.vao
    def destroy(self):
        glDeleteVertexArrays(1,self.vao) ### NO Need to turn into an array already ctypes like pointer object