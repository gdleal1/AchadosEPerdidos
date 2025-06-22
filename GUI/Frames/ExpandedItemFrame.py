import customtkinter as ck
import os
from GUI.GUIComponents.SharedComponents.BackButton import BackButton
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from PIL import Image

class ExpandedItemFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_search_frame):
        super().__init__(master)
        self.master = master
        
        # Configure grid
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Back button
        self.back_button = BackButton(self, frame_ref=self, switch_to_previous_frame=switch_to_search_frame)
        self.back_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        
        # Main content frame
        self.content_frame = ck.CTkFrame(self, fg_color="#f0f0f0")
        self.content_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)

    def display_item(self, item_data):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create scrollable container
        scroll_frame = ck.CTkScrollableFrame(self.content_frame)
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        scroll_frame.grid_columnconfigure(0, weight=1)
        
        # Title frame
        title_frame = ck.CTkFrame(scroll_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        ck.CTkLabel(
            title_frame,
            text=item_data['description'].title(),
            font=("Arial", 24, "bold"),
            text_color="#FFFFFF"
        ).pack(anchor="center")
        
        row_counter = 1  # Start after title
        
        # Helper function to add text rows
        def add_detail_row(label, value, row):
            frame = ck.CTkFrame(scroll_frame, fg_color="transparent")
            frame.grid(row=row, column=0, sticky="w", pady=5)
            ck.CTkLabel(
                frame,
                text=f"• {label}:",
                font=("Arial", 16, "bold"),
                anchor="w"
            ).pack(side="left")
            ck.CTkLabel(
                frame,
                text=value,
                font=("Arial", 16),
                anchor="w"
            ).pack(side="left", padx=5)
            return row + 1
        
        # Display status if available
        if 'status' in item_data:
            row_counter = add_detail_row("Status", item_data['status'], row_counter)
        
        # Display category
        row_counter = add_detail_row("Categoria", item_data['category'], row_counter)
        
        # Display location and date
        row_counter = add_detail_row("Local", item_data['location'].title(), row_counter)
        row_counter = add_detail_row("Data", item_data['date'], row_counter)
        
        # Display contact information
        if 'cellphone' in item_data:
            row_counter = add_detail_row("Telefone", item_data['cellphone'], row_counter)
        
        if 'email' in item_data:
            row_counter = add_detail_row("Email", item_data['email'], row_counter)