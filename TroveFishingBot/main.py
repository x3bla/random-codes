import cv2
import keyboard
import pyautogui
import time
import win32api
import random


# square top left     : 912 1516
# square bottom right : 1010 1570

centerX = 960
centerY = 1620

def use():
    keyboard.press("f")


def autofish():
    while not keyboard.is_pressed('q'):
        time.sleep(3)
        use()


def location():
    pyautogui.displayMousePosition()
