from tkinter import filedialog, Listbox, Scrollbar
import tkinter as tk
import configparser
import shutil
import sys
import os
from tkinter import messagebox

config = configparser.ConfigParser()

def save_path(game_path):
    config['DEFAULT'] = {'GamePath': game_path}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def load_path():
    config.read('config.ini')
    return config['DEFAULT'].get('GamePath', None)

def search_for_game(default_path="C:/Program Files (x86)/Steam/steamapps/common/"):
    if os.path.exists(default_path):
        for folder in os.listdir(default_path):
            # If game's folder name is unique, this should suffice:
            if "Dadish" == folder:
                return os.path.join(default_path, folder)
            else:
                tk.messagebox.showwarning("Warning", "Game folder not found!")
    return None

def ensure_base_game_folder_exists(game_path):
    base_game_path = os.path.join(mods_directory, "base_game")
    base_game_assets_path = os.path.join(base_game_path, "assets")
    if not os.path.exists(base_game_assets_path):
        assets_path = os.path.join(game_path, "assets")
        if os.path.exists(assets_path):
            shutil.copytree(assets_path, base_game_assets_path)


def get_mods_list(mods_folder_path):
    if os.path.exists(mods_folder_path):
        return [folder for folder in os.listdir(mods_folder_path) if os.path.isdir(os.path.join(mods_folder_path, folder))]
    else:
        return []

def on_mod_selected(event):
    global mod_name
    widget = event.widget
    selection = widget.curselection()
    mod_name = widget.get(selection[0])

def load_mod():
    global mod_name
    try:
        mod_path = os.path.join(mods_directory, mod_name)  # assuming mods_directory is your mod's main directory
        copy_mod_to_game(mod_path, game_directory)  # assuming game_directory is your game's main directory
        
        graphics_path = os.path.join(mod_path, "assets", "graphics","1x")
        if os.path.exists(graphics_path):
            mod_files = os.listdir(graphics_path)
        else:
            mod_files = os.listdir(mod_path)
        contains_graphics = any(file.endswith(('.png', '.jpg')) for file in mod_files)
        if contains_graphics:
            message = "Mod loaded successfully. Since this mod contains graphics, you need to restart the game for the changes to take effect."
        else:
            message = "Mod loaded successfully."

        # Display the message to the user
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showinfo("Mod Loaded", message)
        root.destroy()
    except:
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showerror("Error", "The game path is incorrect or the mod doesn't exist.")
        root.destroy()  # Destroy the root window after the error message is shown
        return

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        game_path_var.set(folder_selected)
        save_path(folder_selected)
        ensure_base_game_folder_exists(folder_selected, mod_path)

def copy_mod_to_game(mod_path, game_path):
    game_path = game_path_var.get()
    # Paths for various game assets
    data_path = os.path.join(game_path, "assets", "data")
    graphics_path = os.path.join(game_path, "assets", "graphics", "1x")
    music_path = os.path.join(game_path, "assets", "music")
    sfx_path = os.path.join(game_path, "assets", "sfx")
    
    # If mod follows the standardized structure
    if os.path.exists(os.path.join(mod_path, "assets")):
        for category in ["data", "music", "sfx"]:
            src = os.path.join(mod_path, "assets", category)
            if os.path.exists(src):
                for item in os.listdir(src):
                    shutil.copy2(os.path.join(src, item), os.path.join(game_path, "assets", category))
        
        # Handle graphics separately due to additional sub-directory
        src_graphics = os.path.join(mod_path, "assets", "graphics", "1x")
        if os.path.exists(src_graphics):
            for graphic in os.listdir(src_graphics):
                shutil.copy2(os.path.join(src_graphics, graphic), graphics_path)
                
    # If mod doesn't follow the standardized structure
    else:
        for item in os.listdir(mod_path):
            item_path = os.path.join(mod_path, item)
            if os.path.isfile(item_path):
                extension = os.path.splitext(item)[-1].lower()
                if extension == ".ogg":
                    shutil.copy2(item_path, sfx_path)
                elif extension in [".mbs", ".scn"]:
                    shutil.copy2(item_path, data_path)
                elif extension in [".png", ".jpg", ".jpeg", ".gif"]:  # add other image extensions if needed
                    shutilutil.copy2(item_path, graphics_path)

def search_folder():
    path = search_for_game()
    if path:
        game_path_var.set(path)
        game_directory = path
        save_path(path)

def refresh_mod_list():
    # Clear the current listbox
    mods_listbox.delete(0, tk.END)

    # Get the updated list of mods
    mods_list = get_mods_list(mods_directory)

    # Repopulate the listbox
    for mod in mods_list:
        mods_listbox.insert(tk.END, mod)
    
if getattr(sys, 'frozen', False):
    current_directory = os.path.dirname(sys.executable)
else:
    current_directory = os.path.dirname(os.path.abspath(__file__))

mods_directory = os.path.join(current_directory, "mods")

game_directory = load_path()
if not game_directory:
    game_directory = search_for_game()
    if not game_directory:
        messagebox.showinfo("Info", "Game not found in default Steam folder. Please provide the path to your game.")
    else:
        ensure_base_game_folder_exists(game_directory)
    save_path(game_directory)
else:
    ensure_base_game_folder_exists(game_directory)
    
mod_name = "base_game"

# Create the main window
root = tk.Tk()
root.title("BROccoli - Mod Loader") 
photo = tk.PhotoImage(file = os.path.join(current_directory,"icon.ico"))
root.wm_iconphoto(False, photo)

# 1. Text label input for game path
game_path_var = tk.StringVar(value=game_directory)
game_path_label = tk.Label(root, text="Game Path:")
game_path_label.pack(pady=(20, 5))
game_path_entry = tk.Entry(root, textvariable=game_path_var, width=40)
game_path_entry.pack(pady=(0, 10))

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 20))

# The Browse button
browse_button = tk.Button(button_frame, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=0, padx=(0, 10))

# The Scan for Folder button
scan_button = tk.Button(button_frame, text="Scan for Folder", command=search_folder)
scan_button.grid(row=0, column=1, padx=(10, 0))

# 2. Text label for mods folder path
mods_path_label = tk.Label(root, text=f"Mods Folder: {mods_directory}")
mods_path_label.pack(pady=(0, 10))

# 3. A selectable list of the game mods in the folder with scroll
mods_list = get_mods_list(mods_directory)
mods_listbox = Listbox(root, height=10, selectmode=tk.SINGLE)
for mod in mods_list:
    mods_listbox.insert(tk.END, mod)
mods_listbox.bind('<<ListboxSelect>>', on_mod_selected)
mods_listbox.pack(pady=(0, 10))

# Adding a scrollbar
scrollbar = Scrollbar(root, command=mods_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
mods_listbox.config(yscrollcommand=scrollbar.set)

refresh_button = tk.Button(root, text="Refresh", command=refresh_mod_list)
refresh_button.pack(pady=(0, 10))

# 4. Button
load_mod_button = tk.Button(root, text="Load Mod", command=load_mod)  # Placeholder command
load_mod_button.pack(pady=(10, 20))

root.mainloop()
