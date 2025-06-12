import customtkinter as ck

class FullItemDescriptionText(ck.CTkTextbox):
    def __init__(self, master, **kwargs):
        
        kwargs.setdefault("width", 500)
        kwargs.setdefault("height", 50)
        kwargs.setdefault("wrap", "word")

        super().__init__(master, **kwargs)

    
       
     