from OpenGL.GL import *

class Renderer:
    def __init__(self,point_size):
        glEnable(GL_PROGRAM_POINT_SIZE)
        self.draw_points = 0
    def draw_points(self,bool_loc,points,first = 0):
        self.draw_points = 1
        glUniform1i(bool_loc,self.draw_points)
        glDrawArrays(GL_POINTS,0,points)
    def draw_pose(self,bool_loc,count,instance_count,dtype = GL_UNSIGNED_INT, indices = ctypes.c_void_p(0)):
        self.draw_points = 0
        glUniform1i(bool_loc,self.draw_points)
        glDrawElementsInstanced(GL_LINES,count,dtype,indices,instance_count)