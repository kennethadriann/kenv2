import win32api, win32con, random, time
from pynput import keyboard
import time

def move(x,y):
    win32api.SetCursorPos((x,y))

res_width = win32api.GetSystemMetrics(0)
res_height = win32api.GetSystemMetrics(1)

break_program = False
def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        rand_x = random.randint(1,res_width/2)
        rand_y = random.randint(1,res_height/2)
        time.sleep(1)
        move(rand_x,rand_y)
    listener.join()
