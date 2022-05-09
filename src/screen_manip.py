from time import sleep
from PIL import Image
import pyautogui
import img
import os

WIDTH, HEIGHT = pyautogui.size()


def load_skin(first: bool) -> None:
    if first:
        # Move the cursor into the game and select the workbench.
        pyautogui.moveTo(1, 1, duration=0.1)
        pyautogui.click()

    # Move to the "Load" button. The first time we do this, it takes 12 presses. After that, it always
    # takes 6 presses.
    if first:
        pyautogui.press('tab', presses=12, interval=0.1)
    else:
        pyautogui.press('tab', presses=6, interval=0.1)

    # Press the "Load" button.
    pyautogui.press('enter')

    # Navigate to the file select menu.
    pyautogui.press('tab', presses=5, interval=0.1)

    # The first time we do this, we must also select the folder first.
    if first:
        pyautogui.press('up')
        pyautogui.press('enter')

    # Select the file.
    pyautogui.press('up')
    pyautogui.press('enter')


def reset_float_slider() -> None:
    pyautogui.press('tab', presses=14, interval=0.1)
    pyautogui.press('pagedown', presses=10, interval=0.1)
    sleep(0.01)
    pyautogui.press('enter')


def increase_float(current_float: float, float_goal: int, min_float: int, max_float: int) -> float:
    steps = float((max_float - min_float) / 100)

    while current_float < float_goal:
        pyautogui.press('right')
        current_float += steps
        sleep(0.1)

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


def crop_image(directory: str) -> None:
    # FIXME: Crop config per weapon and working with 4K and 1080P
    im = Image.open(directory)
    im_crop = im.crop((270, 40, 1830, 910))
    im_crop.save(directory, 'PNG')


def verify_if_loaded() -> None:
    loaded = False
    while not loaded:
        take_screenshot('./is_loaded.png')
        loaded = img.verify_loaded()
        sleep(1)


def close_game() -> None:
    pyautogui.hotkey('alt', 'f4')
    sleep(0.3)
    pyautogui.typewrite('exit')
    pyautogui.press('enter')


if __name__ == '__main__':
    verify_if_loaded()
