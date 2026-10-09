from OpenGL.GL import *
import numpy as np
from pose import Pose
from shader import Shader
from buffer import Buffer
import random
class Scene:
    def __init__(self,n_poses):
        self.buffer = Buffer(n_poses)
        self.pose = Pose(self.buffer.get_vbo())
        self.shader = Shader()
        self.offset = 0
        self.poses_drawn = 0
        self.pose_region = self.buffer.get_buffer_size() + self.buffer.get_buff_ptr()
    def rotation_matrix_4x4_y(self,angle_deg):
        angle_rad = np.deg2rad(angle_deg)
        c, s = np.cos(angle_rad), np.sin(angle_rad)
        return np.array([
            [ c,  0,  s,  0],
            [ 0,  1,  0,  0],
            [-s,  0,  c,  0],
            [ 0,  0,  0,  1]
        ])
    def upload_pose(self,pose,max_poses):
        pose = np.array(pose,np.float32)
        dst = self.buffer.get_buff_ptr() + self.offset + pose.nbytes
        if dst > self.pose_region:
            self.offset = 0
        ctypes.memmove(
            ctypes.c_void_p(self.buffer.get_buff_ptr() + self.offset),
            pose.ctypes.data,
            pose.nbytes
        )
        self.offset += pose.nbytes
        self.poses_drawn += pose.__len__()
        if max_poses < self.poses_drawn:
            self.poses_drawn = max_poses
        return self.poses_drawn
    def generate_identity(self):
        return np.eye(4)
    def generate_poses(self,n_poses):
        trans_matrix = []
        for pose in range(n_poses):
            translation_mat = np.array([[1,0,0,random.uniform(-1,1)],
                                        [0,1,0,random.uniform(-1,1)],
                                        [0,0,1,0],
                                        [0,0,0,1]],np.float32)
            trans_matrix.append(translation_mat)
        #translation_mat = np.array([[1,0,0,random.uniform(-0.5,0.5)],
        #                                [0,1,0,random.uniform(-0.5,0.5)],
        #                                [0,0,1,0],
        #                                [0,0,0,1]],np.float32)
        #trans_matrix.append(translation_mat)
        return trans_matrix
    def use_shader(self):
        return self.shader.use()
    def get_uniform_loc(self,name):
        return self.shader.get_uniform_loc(name)
    def get_vao(self):
        return self.pose.get_vao()
    def destroy(self):
        self.shader.delete_program()
        self.pose.destroy()
        self.buffer.destroy()