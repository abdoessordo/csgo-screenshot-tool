import json
from time import sleep

import numpy as np
from PIL import Image, ImageChops
import pyautogui
import img
import os

WIDTH, HEIGHT = pyautogui.size()


def load_skin() -> None:
    # Move to the "Load" button.
    pyautogui.press('tab', presses=1, interval=0.1)
    # Press the "Load" button.
    pyautogui.press('enter')
    # Navigate to the file select menu.
    pyautogui.press('tab', presses=1, interval=0.1)
    # Select the folder.
    pyautogui.press('up')
    pyautogui.press('enter')
    # Select the file.
    pyautogui.press('up')
    pyautogui.press('enter')


def reset_float_slider() -> None:
    pyautogui.press('tab', presses=1, interval=0.1)
    pyautogui.press('pagedown', presses=10, interval=0.1)
    sleep(0.01)
    pyautogui.press('enter')


def increase_float(current_float: float, float_goal: int, min_float: int, max_float: int, has_wear: bool) -> float:
    steps = float((max_float - min_float) / 100)

    while current_float < float_goal:
        if has_wear:
            pyautogui.press('right')
        current_float += steps
        sleep(0.1)

    if has_wear:
        pyautogui.press('enter')

    return current_float


def take_screenshot(directory: str) -> None:
    base_directory = directory.split('\\')
    if len(base_directory) > 1:
        base_directory.pop()
        base_directory = '\\'.join(base_directory)
        is_exist = os.path.exists(base_directory)
        if not is_exist:
            os.makedirs(base_directory)

    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(directory)


def is_screenshot_correct(img_path: str, reference_img_path: str) -> bool:
    # FIXME: Improve this function to detect correct/wrong screenshots better
    im = Image.open(img_path)
    reference_img = Image.open(reference_img_path)

    diff = ImageChops.difference(im, reference_img)
    diff = diff.crop(diff.getbbox())

    # Start both at 1 to avoid a division by zero.
    black = 1
    other = 1

    for pixel in diff.getdata():
        if pixel[0] <= 10 and pixel[0] <= 10 and pixel[0] <= 10:
            black += 1
        else:
            other += 1

    ratio = black / other

    # There must be at least 10 times as much black pixels than other pixels.
    return ratio > 10


def crop_image(directory: str, box: tuple) -> None:
    im = Image.open(directory)
    im_crop = im.crop(box)
    im_crop.save(directory, 'PNG')


def store_bounding_box(directory: str, weapon: str, base: tuple) -> None:
    # FIXME: Remove this function when not needed anymore
    im = Image.open(directory)
    im = im.convert('RGBA')

    # This is a height x width x 4 numpy array.
    data = np.array(im)
    # Temporarily unpack the bands for readability.
    red, green, blue, alpha = data.T
    # Replace our background color with transparency.
    white_areas = (red == 31) & (green == 41) & (blue == 55) & (alpha == 255)
    data[...][white_areas.T] = (0, 0, 0, 0)

    im2 = Image.fromarray(data)
    box = list(im2.getbbox())
    print(box, base)
    box[0] += (base[0] - 10)
    box[1] += (base[1] - 10)
    box[2] += (base[0] + 10)
    box[3] += (base[1] + 10)
    print(box)

    with open('./tmp/bounding.json', 'r+', encoding='utf-8') as f:
        content = json.load(f)
        content[weapon] = box
        f.seek(0)
        json.dump(content, f, ensure_ascii=False, indent=4)


def verify_if_loaded() -> None:
    loaded = False
    while not loaded:
        take_screenshot('./tmp/is_loaded.png')
        loaded = img.verify_loaded()
        sleep(1.0)


def close_workshop() -> None:
    pyautogui.hotkey('alt', 'f4')


def open_workshop() -> None:
    # Move the cursor into the game.
    pyautogui.moveTo(1, 1, duration=0.1)
    pyautogui.click()
    # NOTE: This `write` operation causes some weird behaviour which makes the tabbing functionality of the workbench
    # work in reverse. No idea why, but we adapt all our tabbing logic to this side effect!
    pyautogui.write('workshop_workbench')
    pyautogui.press('enter')


def close_game() -> None:
    sleep(0.3)
    pyautogui.write('exit')
    pyautogui.press('enter')
