import customtkinter as ck

class RegisterButton(ck.CTkButton):
    def __init__(self, master, frame_ref, **kwargs):
        super().__init__(master, text="Registrar-se", command=self.register_action, **kwargs)
        self.frame = frame_ref
    
    
    def register_action(self):
        pass

    