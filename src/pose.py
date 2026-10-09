from OpenGL.GL import *
import numpy as np

class Pose:
    def __init__(self,instance_vbo):
        self.mesh = np.array([[-0.5,0.5,0],
                              [0.5,0.5,0],
                              [0.5,-0.5,0],
                              [-0.5,-0.5,0]],np.float32)
        self.mesh_size = self.mesh.nbytes
        self.indices = np.array([[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]],np.uint32)
        self.indices_size = self.indices.nbytes
        self.vao = ctypes.c_uint()
        glCreateVertexArrays(1,self.vao)
        self.ibo = ctypes.c_uint()
        glCreateBuffers(1,self.ibo)
        glNamedBufferStorage(self.ibo,self.indices_size,self.indices,GL_DYNAMIC_STORAGE_BIT)
        self.mesh_vbo = ctypes.c_uint()
        glCreateBuffers(1,self.mesh_vbo)
        glNamedBufferStorage(self.mesh_vbo,self.mesh_size,self.mesh,GL_DYNAMIC_STORAGE_BIT)
        
        self.setup_vao(self.vao,self.mesh_vbo,instance_vbo,12,self.ibo)
    def setup_vao(self,mesh_vao,mesh_vbo,instance_buffer,mesh_stride,ibo):
        glVertexArrayVertexBuffer(mesh_vao,0,mesh_vbo,0,mesh_stride)
        glVertexArrayElementBuffer(mesh_vao,ibo)
        glEnableVertexArrayAttrib(mesh_vao,0)
        glVertexArrayAttribFormat(mesh_vao,0,3,GL_FLOAT,GL_FALSE,0)
        glVertexArrayAttribBinding(mesh_vao,0,0)
        glVertexArrayVertexBuffer(mesh_vao,1,instance_buffer,0,64)
        for instance in range(4):
            glEnableVertexArrayAttrib(mesh_vao,instance+1)
            glVertexArrayAttribFormat(mesh_vao,instance+1,4,GL_FLOAT,GL_FALSE,instance*16)
            glVertexArrayAttribBinding(mesh_vao,instance+1,1)
        glVertexArrayBindingDivisor(mesh_vao,1,1)
    def get_vao(self):
        return self.vao
    def destroy(self):
        glDeleteBuffers(2,[self.ibo.value,self.mesh_vbo.value])
        glDeleteVertexArrays(1,self.vao)
