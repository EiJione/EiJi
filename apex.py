# # pyautogui.PAUSE = 0.01
# # pyautogui.FAILSAFE = True
# # x,y = 122,244
# # pyautogui.moveTo(1020,333)[[[[[[[
# # pyautogui.click(x=None,y=None,button='right')
# # c_x,c_y = pyautogui.position()
# # print(c_x,c_y)
# # -*- coding: utf-8 -*-[
# import win32api, win32con, win32gui, win32ui
# import pynput
# import pyautogui
# import time
# from pynput.mouse import Button, Controller
# import keyboard
# mouse_er = Controller()
# x = 1
# # 获取当前鼠标的坐标[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
# breaknum = 1
# print('当前鼠标坐标为 {0}'.format(mouse_er.position))
#
# while 1==1:
#     ni=0
#     flag=0
#     ki=0#以上三个数据用于重启找色部
#
#     #截图部
#     hwndDC=win32gui.GetWindowDC(0)
#     mfcDC=win32ui.CreateDCFromHandle(hwndDC)
#     saveDC=mfcDC.CreateCompatibleDC()
#     saveBitMap=win32ui.CreateBitmap()#以下几行均是在这个bitmap中作画的代码
#     saveBitMap.CreateCompatibleBitmap(mfcDC,300,300)#检测范围可以再大点吗
#     saveDC.SelectObject(saveBitMap)
#     saveDC.BitBlt((0, 0), (300, 300), mfcDC, (810,390), win32con.SRCCOPY) #第一个二元数对是画作左上角在bitmap中的位置，第二个是画作与画作源的大小，第三个是画作源左上角在屏幕中的位置
#     data=saveBitMap.GetBitmapBits() #获取bitmap中每个点的R.G.B.alpha值构成的一个元组（顺序是G.B.R.alpha）。已知的图像大小的情况下，这个有序元组结合二维空间中每一个点的色彩值信息
#     #saveDC.DeleteDC()
#     #mfcDC.DeleteDC()
#     #win32gui.ReleaseDC(hwnd, hwndDC)
#     #win32gui.DeleteObject(saveBitMap.GetHandle())
#     #输出data后便可清空截图的缓存。由于未系统学习win32，原理不明。耗时极短。作为可选项
#     #耗时小于0.0005s/100次
#
#
#
#
#
#
#     #找色部
#     while flag == 0:
#
#         try:#其实这种遍历方式我也不是很喜欢，所以问：是否可以一次只取第一个19，不符合就直接返回未找到？←决定其，我可以在找到合适的函数后看一看这个遍历起到了多大的作用，共占用了多少的时间，最长占用多少时间。
#
#     #目前的感受是，在测试中找色部没有影响程序的流畅感。
#     #完成于凌晨4点，无法正常思考所以实现方式冗杂。尚未改进（便不作太多注释了），但似乎没有太大影响。
#             ni=data[ki:].index(19) #
#             ki=ki+ni
#
#             if ki%4==0 and data[ki+1]==0 and data[ki+2]==-1: #此处的if也可以精简
#                 flag=1
#
#                 x=(ki/4)%300+810+50
#                 y=(ki/4)//300+390+75
#             else:
#                 ki=ki+1
#
#         except:
#             x,y=960,540
#             flag=1
#
#     #此时，输出了x,y
# def click_play_for_aegis():
#
#
#     for i in range(0,4):
#         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE|win32con.MOUSEEVENTF_ABSOLUTE, 0,9)
#         time.sleep(0.01)
#         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, 0, -6)
#         time.sleep(0.01)
#         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, 8, 0)
#         time.sleep(0.01)
#         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, -8, 0)
#         time.sleep(0.01)
#
#
#
#
#     # time.sleep(1)
#     # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE|win32con.MOUSEEVENTF_ABSOLUTE, -10, -10)
#
#
# #     # pyautogui.PAUSE = 0.01
# #     # pyautogui.FAILSAFE = True
# #     # im1 = pyautogui.screenshot('1.jpg')
# #     c_x, c_y = pyautogui.position()
# #     print(c_x, c_y)
# #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 200,200)
# #     c_x, c_y = pyautogui.position()
# #     print(c_x, c_y)
# #     # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)[
# #     # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# #
# #     # pyautogui.click(c_x,c_y,button='right')
#
# #[[
#
# def on_activate_p():
#     click_play_for_aegis()
#
#
# with pynput.keyboard.GlobalHotKeys({'e': on_activate_p}) as h:
#     h.join()












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

