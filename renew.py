#!/usr/bin/python
# Welcome to CLRenew, a simple python script that automates mouse clicks to
# renew craigslist postings credit to https://github.com/yuqianli for base code
import pyautogui
import os
# Set a counter to count the # of exceptions occur
counter = 0

# Start the while loop
while True:
    try:
        print ("Be sure your active listings page is up and active")
        pyautogui.time.sleep(2)
        renewButtonLocationX, renewButtonLocationY  = pyautogui.locateCenterOnScreen('renew.png')
        pyautogui.moveTo(renewButtonLocationX, renewButtonLocationY)
        pyautogui.click()
        pyautogui.time.sleep(2)

# This part of the loop will depend on your browser binding to go back a page:
        pyautogui.keyDown('alt')
        pyautogui.press('left')
        pyautogui.keyUp('alt')

        pyautogui.time.sleep(2)

# Exception handle when pyautogui can't locate the renew button on the screen
# or if it clicks away by mistake
# this section needs work and sometimes fails to function properly
    except Exception:
        print ("Exception thrown, calculating course of action")
        pyautogui.press('pgdn')
        counter += 1
        print ("counter =" + str(counter))
        if counter >= 3: counter = 0
        pyautogui.time.sleep(2)
        renewButtonLocationX,renewButtonLocationY  = pyautogui.locateCenterOnScreen('page2.png')
        pyautogui.moveTo(renewButtonLocationX, renewButtonLocationY)
        pyautogui.click()
        pyautogui.time.sleep(2)

