from OpenGL.GL import *
import numpy as np
from pyglm import glm
import random
from pose import Pose
from buffer import Buffer
class Scene:
    def __init__(self,n_poses):
        self.n_poses = n_poses
        self.buffer = Buffer(n_poses)
        self.pose = Pose(self.buffer.get_vbo())
        self.offset = 0
        self.poses_drawn = 0
        self.pose_region = self.buffer.get_buffer_size() + self.buffer.get_buff_ptr()
    def upload_pose(self,pose):
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
        if self.n_poses < self.poses_drawn:
            self.poses_drawn = self.n_poses
        return self.poses_drawn
    def generate_identity(self):
        return np.eye(4)
    def generate_poses(self,n_poses):
        trans_matrix = []
        for pose in range(n_poses):
            translation_mat = np.array([[1,0,0,np.random.uniform(-5,5)],
                                        [0,1,0,np.random.uniform(-5,5)],
                                        [0,0,1,0],
                                        [0,0,0,1]],np.float32)
            #translation_mat = glm.translate(glm.mat4(1),glm.vec3(random.uniform(-1,1),random.uniform(-1,1),0))
            trans_matrix.append(translation_mat.T)
        #translation_mat = np.array([[1,0,0,random.uniform(-0.5,0.5)],
        #                                [0,1,0,random.uniform(-0.5,0.5)],
        #                                [0,0,1,0],
        #                                [0,0,0,1]],np.float32)
        return trans_matrix
    def get_vao(self):
        return self.pose.get_vao()
    def get_n_poses(self):
        return self.n_poses
    def destroy(self):
        self.pose.destroy()
        self.buffer.destroy()