# keyboard.hook_key('enter', bcd)
# recorded = keyboard.record(until='esc')
import win32api
import win32con
import time
from pynput import mouse
#
import threading
active = False
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up', (x, y)))
def on_click(x, y, button, pressed):
    global active
    print(pressed)
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if pressed:
        print(1)

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

