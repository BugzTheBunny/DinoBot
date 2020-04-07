import pyautogui
from numpy import *
from PIL import ImageGrab, ImageOps
import time

# This code, will work, only in case that the resolution is 1920x1080


def press_replay_btn():
    """ אחראי על לחיצת הכפתור REPLAY, זה יעבוד באופן קבוע, יזהה את התמונה, ויחפש ערך הערך המספרי של הכפתור
    במידה והוא ימצא את הערך 5160 הוא יגרום לעכבר ללחוץ על הנקודה במסך, שבה מופיע הכפתור (Aאותו אנחנו קבענו)"""
    replay_btn = (920, 540, 1000, 600)
    btn = ImageGrab.grab(replay_btn)
    gray_btn = ImageOps.grayscale(btn)
    sum_of_colors = array(gray_btn.getcolors()).sum()
    if int(sum_of_colors) == 5160:
        pyautogui.click(920, 540)



def find_an_michol():
    """
    בדיוק כמו קודם, זה יחפש שינויים בריבוע שקבענו את הערך המספרי ה"נורמאלי" שלו ל6933, במידה והמספר הזה משתנה, הדינוזאור יקפוץ.
    קפיצה = לגרום לקוד לדמות לחיצה של הכפתור SPACE (רווח).
    """
    dino_nose_x_y = (217, 615)
    detection_square = (dino_nose_x_y[0] + 5, dino_nose_x_y[1], dino_nose_x_y[0] + 350, dino_nose_x_y[1] + 20)
    capture = ImageGrab.grab(detection_square)
    gray_capture = ImageOps.grayscale(capture)
    sum_of_colors = array(gray_capture.getcolors()).sum()
    if sum_of_colors != 6933:
        pyautogui.keyDown("space")


time.sleep(2)

while True:
    press_replay_btn()
    find_an_michol()
