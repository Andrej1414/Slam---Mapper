from OpenGL.GL import *
import numpy as np
import random
from vao import Vao
from vbo import Vbo
from point import Point
from pose import Pose

class Scene:
    def __init__(self,n_poses,n_points):
        self.vao = Vao()
        self.vbo = Vbo(n_poses,n_points)
        self.point = Point(True)
        self.pose = Pose()
        self.n_poses = n_poses
        self.n_points = n_points
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
        if self.pose_addr + self.pose_draw_offset + pose_size > self.pose_region:
            self.pose_draw_offset = 0
        dst = self.pose_addr + self.pose_draw_offset
        ctypes.memmove(
            ctypes.c_void_p(dst),
            pose.ctypes.data,
            pose_size
        )
        self.pose_draw_offset += pose_size
        self.poses_to_draw += n_poses
        if self.n_poses < self.poses_to_draw:
            self.poses_to_draw = self.n_poses
        return self.poses_to_draw
    def upload_points(self,points):
        points_size = points.nbytes
        n_points = len(points)
        if self.point_addr + self.point_draw_offset + points_size > self.point_region:
            self.point_draw_offset = 0
        dst = self.point_addr + self.point_draw_offset
        ctypes.memmove(
            ctypes.c_void_p(dst),
            points.ctypes.data,
            points_size
        )
        self.point_draw_offset += points_size
        self.points_to_draw += n_points
        if self.n_points < self.points_to_draw:
            self.points_to_draw = self.n_points
        return self.points_to_draw
    def generate_map_points(self,n_points):
        map_points = []
        for point in range(n_points):
            map_point = [random.uniform(-1,1),random.uniform(-1,1),0]
            map_points.append(map_point)
        map_points = np.array(map_points,dtype=np.float32)
        return map_points
    def generate_poses(self,n_poses):
        trans_matrix = []
        for pose in range(n_poses):
            translation_mat = np.array([[1,0,0,np.random.uniform(-1,1)],
                                        [0,1,0,np.random.uniform(-1,1)],
                                        [0,0,1,0],
                                        [0,0,0,1]],np.float32)
            trans_matrix.append(translation_mat.T)
        return np.array(trans_matrix)
    def draw_sphere(self,circle_res,n_circles,radius = 1):
        phi_step = 180 / n_circles
        theta_step = 360 / (circle_res)
        map_points = []
        for circle in range(n_circles):
            phi = circle * phi_step
            for point in range(circle_res):
                theta = point * theta_step
                x = radius*np.sin(np.deg2rad(phi))*np.cos(np.deg2rad(theta))
                y = radius*np.sin(np.deg2rad(phi))*np.sin(np.deg2rad(theta))
                z = radius*np.cos(np.deg2rad(phi))
                map_points.append([x,y,z])
        return np.array(map_points,np.float32)
    def draw_cube(self,resolution):
        points = []
        for point in range(resolution):
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
            z = random.uniform(-1,1)
            points.append([x,y,z])
        points = np.array(points,np.float32)
        return points
    def get_vao(self):
        return self.vao.get_vao()
    def destroy(self):
        self.vao.destroy()
        self.vbo.destroy()
        self.pose.destroy()