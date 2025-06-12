import customtkinter as ck

class AnnounceButton(ck.CTkButton):
    def __init__(self, master, frame_ref, **kwargs):
        super().__init__(master, text="Anunciar Item", command=self.announce_action, **kwargs)
        self.frame = frame_ref
    
    
    def announce_action(self):
        pass