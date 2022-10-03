import pyautogui, keyboard, threading, time

global __pausar, __finesh
__pausar = False
__finesh = False

def pausarDespausar():
    global __pausar, __finesh
    while True:
        tleca_press = keyboard.read_key()
        if str(tleca_press).upper() == 'Y':
            __pausar = not __pausar
            time.sleep(1)
        elif str(tleca_press).upper() == 'C':
            __finesh = True
            print('Programa finalizado')
            break

threading.Thread(target=pausarDespausar).start()  

def clicarEsImg(sources = str):
    try:
        x_backup, y_backup = pyautogui.position()
        x, y = pyautogui.locateCenterOnScreen(sources)
        pyautogui.click(x, y)
        pyautogui.moveTo(x_backup, y_backup)
    except:
        pass #pular

def clicarDiImg(sources = str):
    try:
        x_backup, y_backup = pyautogui.position()
        x, y = pyautogui.locateCenterOnScreen(sources)
        pyautogui.click(x, y, button='right')
        pyautogui.moveTo(x_backup, y_backup)
    except:
        pass #pular


while True:
    if __finesh:
        break
    if not __pausar:
        clicarEsImg('res.png')
    time.sleep(0.1)    


