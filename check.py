import pyautogui
import keyboard
import webbrowser

while True:
       if keyboard.is_pressed('c'):
                 print(pyautogui.position())
