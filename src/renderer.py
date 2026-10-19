from OpenGL.GL import *
import time

class Renderer:
    def __init__(self,point_size):
        glEnable(GL_PROGRAM_POINT_SIZE)
        glEnable(GL_DEPTH_TEST)
        glPointSize(point_size)    
    def draw_points(self,bool_loc,points):
        draw_points = 1
        glUniform1i(bool_loc,draw_points)
        glDrawArrays(GL_POINTS,0,points)
    def draw_pose(self,bool_loc,count,instance_count,dtype = GL_UNSIGNED_INT, indices = ctypes.c_void_p(0)):
        draw_points = 0
        glUniform1i(bool_loc,draw_points)
        glDrawElementsInstanced(GL_LINES,count,dtype,indices,instance_count)
    def render(self,bool_loc,scene):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        scene.upload_points(points)

