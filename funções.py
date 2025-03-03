import time
import pyautogui
import threading
import os
import keyboard


def x():
    while True:
        # copiar
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'c')
        # atalho
        time.sleep(0.5)
        pyautogui.hotkey('winleft', '4')
        # click em
        time.sleep(0.5)
        pyautogui.doubleClick(x=616, y=267)
        # colar
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        # click em
        time.sleep(0.5)
        pyautogui.click(x=658, y=365)
        
        

def y():
    while True:
        if keyboard.is_pressed('q'):
            os._exit(0)

threading.Thread(target=y).start()

pyautogui.hotkey('winleft', '5') # Abrir app 5

threading.Thread(target=x).start()



