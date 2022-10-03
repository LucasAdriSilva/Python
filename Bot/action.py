import pyautogui, keyboard, threading, time

def clicarEsImg(sources = str):
    try:
        x_backup, y_backup = pyautogui.position()
        x, y = pyautogui.locateCenterOnScreen(sources)
        pyautogui.click(x, y)
        pyautogui.moveTo(x_backup, y_backup)
    except:
        pass #pular

def setGammaForZero():
    keyboard.press('tab')
    keyboard.write('gamma 0')
    keyboard.press('enter')

def eat():
    #Procurar img que representa fome
    img = pyautogui.locateCenterOnScreen('res.png')
    if img == None :
        print('Não está com fome' )
    else:
        keyboard.press('0')

def water():
    #Procurar img que representa Sede
    img = pyautogui.locateCenterOnScreen('res.png')
    if img == None :
        print('Não está com Sede')
    else:
        keyboard.press('9')

def move(x):
    if x % 2 == 0:
        pyautogui.keyDown('w')
        time.sleep(3)
        pyautogui.keyUp('w')
        time.sleep(1)
        

    if x % 2 == 1:
        pyautogui.keyDown('s')
        time.sleep(3)
        pyautogui.keyUp('s')
        time.sleep(1)

def jump(x):  
    y = 0
    while y < x:
        pyautogui.press('space')
        time.sleep(2)
        y = y+1

def transfirItems(botao, preset, transfir, fechar):
    #Abrir transfir
    keyboard.press('2')

    #Clicar
    pyautogui.click()

    #Clicar no botão
    if(pyautogui.locateCenterOnScreen(botao)):
        clicarEsImg(botao)
    else:
        print('Não achei o botão ')

    #Clicar no preset
    if(pyautogui.locateCenterOnScreen(preset)):
        clicarEsImg(preset)
    else:
        print('Não achei o botão de preset')

    #Clicar no Transfir
    if(pyautogui.locateCenterOnScreen(transfir)):
        clicarEsImg(transfir)
    else:
        print('Não achei o botão de Transfir')

    #Clicar no Fechar
    if(pyautogui.locateCenterOnScreen(fechar)):
        clicarEsImg(fechar)
    else:
        print('Não achei o botão de fechar')

    #Fechar transfir
    keyboard.press('2')
       
def generateSeed(Seed):
    pyautogui.keyDown('e')

    #Clicar no botão
    if(pyautogui.locateCenterOnScreen(Seed)):
        clicarEsImg(Seed)
        pyautogui.keyUp('e')

    else:
        print('Não achei o botão de gerar semente ')
        pyautogui.keyUp('e')

def msg():
    keyboard.press('enter')
    keyboard.press('.')
    keyboard.press('enter')




    