from OpenGL.GL import *

class Vao:
    def __init__(self):
        self.vao = ctypes.c_uint()
        self.create_vao()
    def create_vao(self):
        glCreateVertexArrays(1,self.vao)
    def get_vao(self):
        return self.vao
    def destroy(self):
        glDeleteVertexArrays(1,self.vao)