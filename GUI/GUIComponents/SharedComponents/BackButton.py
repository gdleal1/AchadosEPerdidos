import customtkinter as ck
from PIL import Image

class BackButton(ck.CTkButton):
    def __init__(self, master, frame_ref, switch_to_previous_frame=None, **kwargs):
        
        # Load the image for the button
        image = Image.open("GUI\\images\\back-button-icon.png")  
        self.back_image = ck.CTkImage(light_image=image, dark_image=image, size=(45, 45))

        # Create the button with the image and command
        super().__init__(
            master,
            text="",  
            image=self.back_image,
            command=self.back_action,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            width=40,
            height=40,
            **kwargs
        )

        self.frame = frame_ref
        self.switch_to_previous_frame = switch_to_previous_frame

    def back_action(self):
        self.switch_to_previous_frame()
