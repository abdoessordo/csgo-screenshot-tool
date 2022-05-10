from time import sleep
from get_all_skins import get_all_skins
import screen_manip
import config_file_manip

all_skins, base_directory, output_directory = get_all_skins()

for i, skin in enumerate(all_skins):
    input_skin = skin['input_config_file']
    output_img = skin['output_screenshot_directory']
    has_wear = skin['has_wear']
    from_float = int(float(skin['from_float']) * 100)
    to_float = int(float(skin['to_float']) * 100)
    min_float = int(float(skin['min_float']) * 100)
    max_float = int(float(skin['max_float']) * 100)

    screen_manip.open_workshop()
    sleep(0.5)

    print('Waiting for workbench availability...')
    screen_manip.verify_if_loaded()
    print(f'Working on {input_skin}')
    config_file_manip.copy_skin_config(f'{base_directory}/configs/{input_skin}')
    screen_manip.load_skin()
    sleep(1.5)
    if has_wear:
        screen_manip.reset_float_slider()
        sleep(1.5)
    print('Loaded skin config')

    current_float_goal = from_float
    current_float = float(min_float)
    last_output_img_dir = None

    while current_float_goal <= to_float:
        print(f'Current float {"{:.2f}".format(current_float)}, current float goal {current_float_goal}')

        output_img_dir = f'{output_directory}\\screenshots\\{output_img}\\{current_float_goal}.png'

        while True:
            print('Taking screenshot...')
            screen_manip.take_screenshot(output_img_dir)
            screen_manip.crop_image(output_img_dir)

            if last_output_img_dir is None:
                print('Breaking because of None')
                break

            if screen_manip.is_screenshot_correct(output_img_dir, last_output_img_dir):
                print('Breaking because of correct screenshot')
                break

            print('Screenshot not correct')

        last_output_img_dir = output_img_dir

        current_float_goal += 1
        if current_float_goal <= to_float:
            current_float = screen_manip.increase_float(
                current_float,
                current_float_goal,
                min_float,
                max_float,
                has_wear,
            )

    screen_manip.close_workshop()
    sleep(0.5)

screen_manip.close_game()
