from OpenGL.GL import *
from pyglm import glm
from vao import Vao
from vbo import Vbo
from point import Point
from pose import Pose

class Scene:
    def __init__(self,n_poses,n_points):
        self.vao = Vao()
        self.vbo = Vbo(n_poses,n_points)
        self.point = Point()
        self.pose = Pose()
        pose_buffer_offset = n_points * self.point.POINT_SIZE
        self.point.setup_vao(self.vao.get_vao(),self.vbo.get_vbo(),0)
        self.pose.setup_vao(self.vao.get_vao(),self.vbo.get_vbo(),pose_buffer_offset)
        self.point_draw_offset = 0
        self.pose_draw_offset = 0
        self.point_addr = self.vbo.get_buff_ptr()
        self.pose_addr = self.vbo.get_buff_ptr() + pose_buffer_offset
        self.point_region = self.point_addr + self.vbo.get_point_region()
        self.pose_region = self.pose_addr + self.vbo.get_pose_region()
        self.poses_to_draw = 0
        self.points_to_draw = 0
    def upload_pose(self,pose):
        pose_size = pose.nbytes
        n_poses = len(pose)
        dst = self.pose_addr + self.pose_draw_offset
        if dst + pose_size > self.pose_region:
            self.pose_draw_offset = 0
        ctypes.memmove(
            ctypes.c_void_p(dst),
            pose.ctypes.data,
            pose_size
        )
        self.pose_draw_offset += pose_size
        self.poses_to_draw += n_poses
        return self.poses_to_draw
    def upload_points(self,points):
        points_size = points.nbytes
        n_points = len(points)
        dst = self.point_addr + self.point_draw_offset
        if dst + points_size > self.point_region:
            self.point_draw_offset =0
        ctypes.memmove(
            ctypes.c_void_p(dst),
            points.ctypes.data,
            points_size
        )
        self.point_draw_offset += points_size
        self.points_to_draw += n_points
        return self.points_to_draw
    def destroy(self):
        self.vao.destroy()
        self.vbo.destoy()
        self.pose.destroy()