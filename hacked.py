import pyautogui
import ctypes
pyautogui.FAILSAFE = False

def search_bar(search):
    pyautogui.moveTo(300, 1100)
    pyautogui.click(button='left')
    pyautogui.write(search, interval=0.2)
    pyautogui.moveTo(300, 200, 1)
    pyautogui.click(button='left')
    

def google_search(search):
    pyautogui.moveTo(1100, 300, 2)
    pyautogui.moveTo(1100, 600, 2)
    pyautogui.click(button='left')
    pyautogui.write(search, interval=0.15)
    pyautogui.press('enter')
    pyautogui.moveTo(400, 300, 2)
    pyautogui.click(button='left')

def save_image(file_name):
    pyautogui.moveTo(400, 500, 2)
    pyautogui.click(button='left')
    pyautogui.moveTo(1300, 400, 2)
    pyautogui.click(button='right')
    pyautogui.moveTo(1350, 700, 2)
    pyautogui.click(button='left')
    pyautogui.moveTo(1300, 650, 2)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    pyautogui.press('backspace')
    pyautogui.write(file_name, interval=0.15)
    pyautogui.moveTo(1200, 750, 1)
    pyautogui.click(button='left')
    pyautogui.moveTo(2000, 0, 1)
    pyautogui.click(button='left')

def set_background(file_name):
    pyautogui.moveTo(300, 1100)
    pyautogui.click(button='left')
    pyautogui.write(file_name, interval=0.2)
    pyautogui.moveTo(1100, 200, 2)
    pyautogui.click(button='left')
    pyautogui.moveTo(1100, 400, 2)
    pyautogui.click(button='right')
    pyautogui.moveTo(1130, 660, 2)
    pyautogui.click(button='left')
    pyautogui.moveTo(1350, 700, 2)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    pyautogui.moveTo(1520, 220, 2)
    pyautogui.click(button='left')

def box(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def main():
    image_name = 'hacker_background'
    search_bar('Google Chrome')
    google_search('You have been hacked')
    save_image(image_name)
    set_background(image_name)
    for _ in range(10):
        box('WARNING', 'You have been hacked', 1)

  
main()