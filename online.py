import pyautogui
import keyboard
import webbrowser
import time
import schedule

def geeks():
          url='https://web.whatsapp.com/'
          chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
          webbrowser.get(chrome_path).open(url)
          time.sleep(4)
# pyautogui.click(x=268,y=225)
          cords=pyautogui.locateCenterOnScreen('school.png')
          pyautogui.click(cords)
          meet=pyautogui.locateCenterOnScreen('meet.png')
          pyautogui.click(meet);
          mic=pyautogui.locateCenterOnScreen('mic.png')
          pyautogui.click(mic)
          camera=pyautogui.locateCenterOnScreen('meet.png')
          pyautogui.click(meet)
          join=pyautogui.locateCenterOnScreen('join.png')
          pyautogui.click(join)

schedule.every().day.at("8:55").do(geeks)
schedule.every().day.at("10:40").do(geeks)
schedule.every().day.at("12:25").do(geeks)

print("Waiting for the Time")
while True:
    schedule.run_pending()
time.sleep(1)