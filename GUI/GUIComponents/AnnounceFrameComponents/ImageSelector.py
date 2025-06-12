import customtkinter as ck
from tkinter import filedialog
import os

class ImageSelector(ck.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.image_path = None

        # Button for selecting an image
        self.select_button = ck.CTkButton(self, text="Selecionar Imagem", command=self.select_image)
        self.select_button.pack(pady=10)

        # Label to show the selected image path/name
        self.file_label = ck.CTkLabel(self, text="Nenhuma imagem selecionada", wraplength=300)
        self.file_label.pack()

    def select_image(self):
        filetypes = [("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp"), ("Todos os arquivos", "*.*")]
        filepath = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=filetypes)

        if filepath:
            self.image_path = filepath
            filename = os.path.basename(filepath)
            self.file_label.configure(text=f"Imagem selecionada: {filename}")
        else:
            self.image_path = None
            self.file_label.configure(text="Nenhuma imagem selecionada")

    def get_image_path(self):
        return self.image_path  # Can be None if no image is selected
