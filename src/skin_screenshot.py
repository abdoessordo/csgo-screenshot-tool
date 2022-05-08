from time import sleep
from get_all_skins import get_all_skins
import screen_manip
import guns_knives
import config_file_manip
import run_mod


all_skins, base_directory, output_directory = get_all_skins()

for skin in all_skins:
    input_skin, output_img, gun_name, wear = [skin.strip('"') for skin in skin.split('" "')]
    wear = float(wear)
    gun_index = guns_knives.ALL_GUNS_KNIVES.index(gun_name.upper())

    screen_manip.verify_if_loaded()
    screen_manip.change_gun(gun_index)
    screen_manip.side_view()
    screen_manip.load_skin()
    try:
        config_file_manip.modify_skin(f'{base_directory}/configs/{input_skin}', wear)
    except:
        print(input_skin)
    screen_manip.load_skin()
    sleep(1.5)
    print(output_img)
    screen_manip.take_screenshot(f'{output_directory}\screenshots\{output_img}')

screen_manip.close_game()
