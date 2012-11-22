import ImageGrab
import ImageOps
import win32api, win32con, win32gui
from numpy import *
import os
import time
import re

x_pad = 8
y_pad = 853
 
 
def screenGrab():
    box2 = (x_pad+1,y_pad+1,x_pad+522,y_pad+20)
    #im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) '.png', 'PNG')
    im2 = ImageGrab.grab(box2)
    im2.save(os.getcwd() + '\\last_test.png', 'PNG')
    return im2
 
def send_input_hax(hwnd, msg):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN , 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN , 0)
    for c in msg:
        if c == "\n":
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN , 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN , 0)
    

def color_close_to(c_inp, c_desired):
    for i in range(3):
        if c_inp[i] < c_desired[i] - 5:
            return False
        if c_inp[i] > c_desired[i] + 5:
            return False
    return True

def main():
    im = screenGrab()
    """
    Enemy dragon
    LOC 193,14
    RGB 249, 50, 50
    LOC 370, 8
    RGB 242, 158, 1
    """
    print im.getpixel((193, 14))
    print im.getpixel((370, 8))
    if color_close_to(im.getpixel((193, 14)), (249, 50, 50)) and \
        color_close_to(im.getpixel((370, 8)), (244, 158, 1)):
        print "Dragon will spawn in 6 mins"
    else:
        print "No drag"
    client_hwnd = []
    win32gui.EnumWindows(callback, client_hwnd)
    print "Client hwnd", client_hwnd
    if len(client_hwnd) != 1:
        print "Game client not open."
    else:
        send_input_hax(client_hwnd[0], "or does it matter")

    
def callback(hwnd, client_hwnd):
    if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
        if win32gui.GetWindowText(hwnd).find('League of Legends (TM) Client') != -1:
            client_hwnd.append(hwnd)
        #client_hwnd.append(win32gui.GetWindowText(hwnd))
    
if __name__ == '__main__':
    main()