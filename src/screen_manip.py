from time import sleep
import pyautogui
import img
import os

WIDTH, HEIGHT = pyautogui.size()


def load_skin():
    # move to load button
    pyautogui.moveTo(0.85 * WIDTH, 0.98 * HEIGHT, duration=0.1)
    pyautogui.click()
    # move to skin folder
    pyautogui.moveTo(0.40 * WIDTH, 0.4 * HEIGHT, duration=0.1)
    # double click
    pyautogui.click()
    pyautogui.click()


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
    pyautogui.keyDown("enter")


if __name__ == "__main__":
    verify_if_loaded()
