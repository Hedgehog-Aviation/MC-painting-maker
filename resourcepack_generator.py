import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random
import zipfile

# Painting sizes and identifiers
painting_data = {
    "1x1": ["alban", "aztec", "aztec2", "bomb", "earth", "kebab", "plant", "wasteland", "water", "wind"],
    "1x2": ["graham", "wanderer"],
    "2x1": ["courbet", "creebet", "pool", "sea", "sunset"],
    "2x2": ["bust", "fire", "match", "skull_and_roses", "stage", "void", "wither"],
    "4x2": ["fighters"],
    "4x3": ["donkey_kong", "skeleton"],
    "4x4": ["burning_skull", "pigscene", "pointer"],
}

def create_resource_pack(painting_id, png_path, zip_file_path):
    # Create a zip file of the resource pack
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        # Add the painting texture
        painting_texture_path = f"assets/minecraft/textures/painting/{painting_id}.png"
        zip_file.write(png_path, painting_texture_path)

        # Create and add the pack.mcmeta file
        pack_mcmeta_content = '''{
            "pack": {
                "pack_format": 22,
                "description": "Custom Minecraft Resource Pack"
            }
        }'''
        zip_file.writestr("pack.mcmeta", pack_mcmeta_content)

    messagebox.showinfo("Success", f"Replaced painting '{painting_id}' with '{png_path}' and created the zip file at:\n{zip_file_path}.")

def upload_image():
    # Open file dialog to upload PNG
    png_path = filedialog.askopenfilename(title="Select a PNG file", filetypes=[("PNG files", "*.png")])
    
    if png_path:
        # Ask for the zip file save location
        zip_file_path = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP files", "*.zip")],
            title="Save Resource Pack"
        )
        
        if zip_file_path:
            selected_size = size_var.get()
            if selected_size in painting_data:
                painting_id = random.choice(painting_data[selected_size])
                create_resource_pack(painting_id, png_path, zip_file_path)
                messagebox.showinfo("Replacement", f"Replaced '{painting_id}' painting.")
            else:
                messagebox.showerror("Error", "Invalid painting size selected.")
        else:
            messagebox.showwarning("Cancelled", "Save operation was cancelled.")

# GUI setup
root = tk.Tk()
root.title("Minecraft Painting Texture Replacer")

# Title label
title_label = tk.Label(root, text="Minecraft Painting Texture Replacer", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Size selection
size_var = tk.StringVar()
size_label = tk.Label(root, text="Select Painting Size:")
size_label.pack()

for size in painting_data.keys():
    radio_btn = tk.Radiobutton(root, text=size, variable=size_var, value=size)
    radio_btn.pack(anchor=tk.W)

# Upload button
upload_btn = tk.Button(root, text="Select Image and Generate Pack", command=upload_image)
upload_btn.pack(pady=20)

# GitHub link
github_label = tk.Label(root, text="GitHub: https://github.com/Hedgehog-Aviation/MC-painting-maker", fg="blue", cursor="hand2")
github_label.pack(pady=10)

# Open the GitHub page when clicked
def open_github(event):
    import webbrowser
    webbrowser.open("https://github.com/Hedgehog-Aviation/MC-painting-maker")

github_label.bind("<Button-1>", open_github)

root.mainloop()
