import time
import pyautogui


def wait():
    time.sleep(0.2)

def move():
    pyautogui.keyUp("d")
    pyautogui.keyDown("w")
    wait()
    pyautogui.keyUp("w")
    pyautogui.keyDown("a")
    wait()
    pyautogui.keyUp("a")
    pyautogui.keyDown("s")
    wait()
    pyautogui.keyUp("s")
    pyautogui.keyDown("d")

while True: 
    move()