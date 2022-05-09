import math
from time import sleep
from PIL import Image
import pyautogui
import img
import os

WIDTH, HEIGHT = pyautogui.size()


def load_skin(first):
    # move to load button
    pyautogui.moveTo(0.85 * WIDTH, 0.98 * HEIGHT, duration=0.1)
    pyautogui.click()
    # move to skin folder
    pyautogui.moveTo(0.40 * WIDTH, 0.405 * HEIGHT, duration=0.1)
    # double click
    pyautogui.click()
    pyautogui.click()

    if first:
        # When we load the first skin, we have to click the folder and then the file, so we need two double clicks.
        # After the first load, this double click is not necessary anymore and breaks tabbing.
        pyautogui.click()
        pyautogui.click()


def reset_float_slider():
    pyautogui.press('tab', presses=14, interval=0.1)
    pyautogui.press('pagedown', presses=10, interval=0.1)


def increase_float(current_float, float_goal, min_float, max_float):
    steps = (max_float - min_float) / 100

    while current_float < float_goal:
        pyautogui.press('right')
        current_float += steps
        sleep(0.1)

    pyautogui.press('enter')

    return current_float


def take_screenshot(directory):
    base_directory = directory.split('\\')
    if len(base_directory) > 1:
        base_directory.pop()
        base_directory = "\\".join(base_directory)
        is_exist = os.path.exists(base_directory)
        if not is_exist:
            os.makedirs(base_directory)

    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(directory)


def crop_image(directory):
    # FIXME: Crop config per weapon and working with 4K and 1080P
    im = Image.open(directory)
    im_crop = im.crop((270, 40, 1830, 910))
    im_crop.save(directory, "PNG")


def verify_if_loaded():
    loaded = False
    while not loaded:
        take_screenshot("./is_loaded.png")
        loaded = img.verify_loaded()


def close_workshop():
    pyautogui.moveTo(0.99 * WIDTH, 0.01 * HEIGHT, duration=0.1)
    pyautogui.click()


def close_game():
    close_workshop()
    sleep(0.3)
    pyautogui.typewrite("exit")
    pyautogui.press("enter")


if __name__ == "__main__":
    verify_if_loaded()
