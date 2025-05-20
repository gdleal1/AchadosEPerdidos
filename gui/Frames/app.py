import customtkinter
from gui.Frames.SearchFrame import SearchFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Resolution
        full_screen_width = self.winfo_screenwidth()
        full_screen_height = self.winfo_screenheight()

        screen_width = int(full_screen_width * 0.8)   # 80% da largura
        screen_height = int(full_screen_height * 0.7) # 70% da altura

        x_offset = (full_screen_width - screen_width) // 2
        y_offset = (full_screen_height - screen_height) // 2

        self.geometry(f"{screen_width}x{screen_height}+{x_offset}+{y_offset}")
        self.title("Sistema de Achados e Perdidos")

        # Style
        self._set_appearance_mode("dark") 

        # Creating frames
        self.search_frame = SearchFrame(self)
        self.search_frame.pack(fill="both", expand=True)