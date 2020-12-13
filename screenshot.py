import time
import pyautogui

def screenshot():
    time.sleep(5)
    ing = pyautogui.screenshot("test.png")
    ing.show()
    
    
    
screenshot()