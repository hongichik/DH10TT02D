import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master, text="", command=None, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            bg="#4da6ff",
            fg="white",
            font=("Arial", 10, "bold"),
            bd=0,
            padx=10,
            pady=5,
            activebackground="#3399ff",
            cursor="hand2",
            **kwargs
        )