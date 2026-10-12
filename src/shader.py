from OpenGL.GL import *
from pathlib import Path
import glfw
from pyglm import glm
class Shader:
    def __init__(self,vertex_shader_path = r"shaders\vertex_shader.txt", fragment_shader_path =r"shaders\fragment_shader.txt"):
        BASE_DIR = Path(__file__).parent.parent
        vertex_shader_path = BASE_DIR / vertex_shader_path
        fragment_shader_path = BASE_DIR / fragment_shader_path
        self.id = glCreateProgram()
        self.compile_shaders(vertex_shader_path,fragment_shader_path)
    def compile_shaders(self,vertex_shader_path,fragment_shader_path):
        with open(f"{vertex_shader_path}",'r') as file:
            text = file.read()
            vertex_shader = glCreateShader(GL_VERTEX_SHADER)
            glShaderSource(vertex_shader,text)
            glCompileShader(vertex_shader)
            glAttachShader(self.id,vertex_shader)
        
        with open(f"{fragment_shader_path}",'r') as file:
            text = file.read()
            fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
            glShaderSource(fragment_shader,text)
            glCompileShader(fragment_shader)
            glAttachShader(self.id,fragment_shader)
        
        glLinkProgram(self.id)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
    def get_uniform_loc(self,name):
        loc = glGetUniformLocation(self.id,name)
        return loc
    def set_uniform(self,name,value):
        loc = glGetUniformLocation(self.id,name)
        glUniformMatrix4fv(loc,1,GL_FALSE,glm.value_ptr(value))
    def use(self):
        glUseProgram(self.id)
    def destroy(self):
        glDeleteProgram(self.id)
