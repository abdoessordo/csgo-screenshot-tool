import shutil


def copy_skin_config(directory):
    game_base_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive"

    shutil.copyfile(directory, f"{game_base_path}\\__custom_skin\\skin_custom.txt")
