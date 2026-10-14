from OpenGL.GL import *


class Point:
    POINT_SIZE = 12
    POINT_COLOR_SIZE = 24
    def __init__(self,color = False):
        self.point_size = self.POINT_SIZE
        if color:
            self.point_size = self.POINT_COLOR_SIZE  
    def setup_vao(self,vao,instance_vbo,offset):
        glVertexArrayVertexBuffer(vao,0,instance_vbo,offset,self.point_size)
        glEnableVertexArrayAttrib(vao,0)
        glVertexArrayAttribFormat(vao,0,3,GL_FLOAT,GL_FALSE,0)
        glVertexArrayAttribBinding(vao,0,0)
    