import pyautogui
from numpy import *
from PIL import ImageGrab, ImageOps
import time

# Location by pixels:
replay_btn = (960, 595)  # The location of the replay button.
dino_location = (217, 615)  # Sexy dino nose location (X / Y) (Dinos did exist).

bad_values = []
# Trees Check:
# X = 425 | Y = 625

#FOV - The distance on which the dinosaur should see the obstacle and jump
fov = 350

def fetch_obstacle():
    """
    Chckes of obstecles in a certein place, still need to find the perfect spot.
    :return:
    """
    verify_obst = (dino_location[0], dino_location[1], dino_location[0] + fov, dino_location[1] + 90)
    box = ImageGrab.grab(verify_obst)
    gray_box = ImageOps.grayscale(box)
    colors_array = array(gray_box.getcolors())
    # print(colors_array.sum())
    return int(colors_array.sum())


def check_for_restart():
    """
    The restart value of the box on a 1920x1080 resolution is 6429
    :return:
    """
    box = (920, 532, 1000, 606)  # Replay Box location
    capture = ImageGrab.grab(box)
    capture = ImageOps.grayscale(capture)
    colors_amount = array(capture.getcolors()).sum()
    if colors_amount != 6429: return False
    else: return True

# TODO: This needs to be verified, still working on it
def night_time():
    """
    night = 25
    :return:
    """
    verify_obst = (0, 0, 5, 5)
    box = ImageGrab.grab(verify_obst)
    gray_box = ImageOps.grayscale(box)
    colors_array = array(gray_box.getcolors())
    # print(colors_array.sum())
    return int(colors_array.sum())


def start_this_thing():
    """
    Everything start hre
    :return:
    """
    while True:
        print(f'time: {night_time()}')
        data = fetch_obstacle()
        print(data)
        check_for_restart()
        if data > 31566:
            pyautogui.keyDown('space')
        if check_for_restart():
            print(f'Ohhhhhh... Should have jumped on {data}')
            time.sleep(3)
            pyautogui.click(replay_btn)


start_this_thing()
