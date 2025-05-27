import customtkinter as ck
from PIL import Image

class LogoImage(ck.CTkLabel):
    def __init__(self, master, image_path="gui/images/logo.png", size=(480, 134), **kwargs):
        self.logo_image = ck.CTkImage(Image.open(image_path), size=size)
        super().__init__(master, image=self.logo_image, text="", **kwargs)

