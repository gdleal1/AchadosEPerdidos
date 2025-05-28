import customtkinter as ck

class LoginButton(ck.CTkButton):
    def __init__(self, master, frame_ref, switch_to_search_frame, **kwargs):
        super().__init__(master, text="Entrar", command=self.login_action, **kwargs)
        self.frame = frame_ref
        self.switch_to_search_frame = switch_to_search_frame
    
    
    def login_action(self):
        self.switch_to_search_frame()

    