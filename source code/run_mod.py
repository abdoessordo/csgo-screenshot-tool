
import os


def run(type):

    if type == "mod":
        start_game = 'start /b "" "C:\Program Files (x86)\Steam\steam.exe" -applaunch 730 -game mod_knive/csgo -console +workshop_workbench'
    elif type == "basic":
        start_game = 'start /b "" "C:\Program Files (x86)\Steam\steam.exe" -applaunch 730 -game mod_gun/csgo -console +workshop_workbench'

    os.system(f'"{start_game}"')




