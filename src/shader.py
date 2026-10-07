from OpenGL.GL import *
from pathlib import Path
import glfw
class Shader:
    def __init__(self,vertex_shader_path = r"shaders/vertex_shader.txt", fragment_shader_path = r"shaders/fragment_shader.txt"):
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
    def use(self):
        glUseProgram(self.id)
    def delete_program(self):
        glDeleteProgram(self.id)

if __name__ == "__main__":
    glfw.init()
    glfw.make_context_current(glfw.create_window(800,600,"test",None,None))
    shader = Shader()
    shader.use()