from time import sleep
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
