from OpenGL.GL import *
import numpy as np
class Pose:
    POSE_SIZE = 64
    def __init__(self):
        self.mesh = np.array([[-0.5,0.5,0],
                              [0.5,0.5,0],
                              [0.5,-0.5,0],
                              [-0.5,-0.5,0]])
        self.mesh_size = self.mesh.nbytes
        self.indeces = np.array([[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]],np.uint32)
        self.indeces_size = self.indeces.nbytes
        self.mesh_vbo = ctypes.c_uint()
        self.mesh_ibo = ctypes.c_uint()
        glCreateBuffers(1,self.mesh_vbo)
        glCreateBuffers(1,self.mesh_ibo)
        glNamedBufferStorage(self.mesh_vbo,self.mesh_size,self.mesh,GL_DYNAMIC_STORAGE_BIT)
        glNamedBufferStorage(self.mesh_ibo,self.indeces_size,self.indeces,GL_DYNAMIC_STORAGE_BIT)
    def setup_vao(self,vao,instance_vbo,instance_offset):
        glVertexArrayVertexBuffer(vao,1,self.mesh_vbo,0,self.mesh_size)
        glVertexArrayElementBuffer(vao,self.mesh_ibo)
        glEnableVertexArrayAttrib(vao,1)
        glVertexArrayAttribFormat(vao,1,3,GL_FLOAT,GL_FALSE,0)
        glVertexArrayAttribBinding(vao,1,1)
        glVertexArrayVertexBuffer(vao,2,instance_vbo,instance_offset,self.POSE_SIZE)
        for instance in range(4):
            glEnableVertexArrayAttrib(vao,instance+1)
            glVertexArrayAttribFormat(vao,instance+1,4,GL_FLOAT,GL_FALSE,instance*16)
            glVertexArrayAttribBinding(vao,instance+1,2)
            glVertexArrayBindingDivisor(vao,instance+1,1)
    def destroy(self):
        glDeleteBuffers(2,[self.mesh_ibo.value,self.mesh_vbo.value])

