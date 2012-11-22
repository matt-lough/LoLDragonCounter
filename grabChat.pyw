# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="l0ngt1ger"
__date__ ="$7/11/2012 1:30:19 PM$"

import ImageGrab
import os
import time

x_pad = 8
y_pad = 853
 
 
def screenGrab():
    box = (1717,0,1917,67)
    box2 = (x_pad+1,y_pad+1,x_pad+522,y_pad+20)
    #im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) '.png', 'PNG')
    im2 = ImageGrab.grab(box2)
    im2.save(os.getcwd() + '\\full_snap2__' + str(int(time.time())) +
    '.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()