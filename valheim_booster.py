'''
Author = xShikari - Ivan Tagle
'''

import pyautogui
import time
import argparse
from datetime import datetime, timedelta
from pynput.mouse import Button, Controller

mouse = Controller()

def jump():
    end_time = datetime.now() + timedelta(seconds=3)

    while datetime.now() < end_time:
        pyautogui.press('space')

def punch():
    #this function will keep punching for 11 seconds and then stop
    end_time = datetime.now() + timedelta(seconds=11)

    while datetime.now() < end_time:
        pyautogui.click()

def repair():
    pyautogui.press('6')
    pyautogui.click()
    pyautogui.press('6')

#this function will repair the elegible tools on the work station
def repairTool():
    #Get the screen size:
    screenWith, screenHeight = pyautogui.size()

    #After pressing e on a workbench the mouse location will always move to the center of the screen
    #Just to be sure we will move the mose to the center again.
    pyautogui.moveTo(screenWith/2, screenHeight/2, 0.5)
    currentMouseX, currentMouseY = pyautogui.position()
    print("Center Screen coordinates: X mouse value: {}, Y mouse value: {}".format(currentMouseX, currentMouseY))

    #To make the movement compatible with all sreens we will make it move with percentages
    buttonX = 61.2*screenWith/100
    buttonY = 44*screenHeight/100
    pyautogui.moveTo(buttonX, buttonY, 2)
    currentMouseX, currentMouseY = pyautogui.position()
    print("Repair button coordinates: X mouse value: {}, Y mouse value: {}".format(currentMouseX, currentMouseY))

def turnAndRepair():
    #Get the screen size:
    screenWith, screenHeight = pyautogui.size()

    #dar vuelta de 180 grados usando porcentajes
    print("Moviendo")
    pyautogui.moveTo(screenWith/2+400, 0, 4)
    #mouse.position = (2000, 10)
    currentMouseX, currentMouseY = pyautogui.position()
    print("X mouse value: {}, Y mouse value: {}".format(currentMouseX, currentMouseY))
    print("Esperando")
    time.sleep(5)
    # Regresar al mismo lugar
    print("Moviendo 2")
    #mouse.position = (1000, 10)
    currentMouseX, currentMouseY = pyautogui.position()
    print("X mouse value: {}, Y mouse value: {}".format(currentMouseX, currentMouseY))
    pyautogui.moveTo(screenWith/2+400, 0, 4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--punch', action='store_true', help='Boost Bare Hands')
    parser.add_argument('-j', '--jump', action='store_true', help='Boost Jump and Run')
    parser.add_argument('-t', '--test', action='store_true', help='Try test funcion')
    args = parser.parse_args()


    try:
        if args.jump:
            print('Boosting jump in 10 secs, switch to Valheim')
            time.sleep(5)
            print('Started')
            pyautogui.keyDown('w')

            while True:
                pyautogui.keyDown('shift')
                print('Jumping')
                jump()
                print('Chillaxing')
                pyautogui.keyUp('shift')
                time.sleep(3)

        elif args.punch:
            print('Boosting bare hands in 10 secs, switch to Valheim')
            time.sleep(5)
            print('Started')
            while True:
                print('Punching')
                punch()
                time.sleep(1)
                print('repair')
                repair()
                print('Chillaxing')
                time.sleep(10)

        elif args.test:
            print('Boosting bare hands in 10 secs, switch to Valheim')
            time.sleep(5)
            print('Started')

            while True:
                turnAndRepair()
                #repairTool()

                #Print the current mouse location every 2 seconds
                """
                currentMouseX, currentMouseY = pyautogui.position()
                print("X mouse value: {}, Y mouse value: {}".format(currentMouseX, currentMouseY))
                time.sleep(2)
                """


        else:
            parser.print_help()

    except KeyboardInterrupt:
        print('Enjoy the boost')
