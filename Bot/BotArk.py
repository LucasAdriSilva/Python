import pyautogui, keyboard, threading, time

global __pausar, __finesh
__pausar = False
__finesh = False
__count = 0

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

def eat():
    #Procurar img que representa fome
    img = pyautogui.locateCenterOnScreen('Fome.png')
    if img == None :
        print('Não está com fome' )
    else:
        keyboard.press('0')
        time.sleep(1)
        keyboard.press('0')
        time.sleep(1)
        keyboard.press('0')
        time.sleep(1)
        keyboard.press('0')
        print('COMI')

def water():
    #Procurar img que representa Sede
    img = pyautogui.locateCenterOnScreen('Sede.png')
    if img == None :
        print('Não está com Sede')
    else:
        keyboard.press('9')
        print('BEBI')

def move(x):
    if x % 2 == 0:
        pyautogui.keyDown('w')
        time.sleep(3)
        pyautogui.keyUp('w')
        time.sleep(1)
        print('Movi para frente')
        

    if x % 2 == 1:
        pyautogui.keyDown('s')
        time.sleep(4)
        pyautogui.keyUp('s')
        time.sleep(1)
        print('Movi para traz')

def jump(x):  
    y = 0
    while y < x:
        keyboard.press('space')
        time.sleep(1)
        y = y+1
    print('Pulei')

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
    print('Mandei msg')
    

while True:
    if __finesh:
        break
    if not __pausar:
        #setGammaForZero()
        while __count < 500:
            #Movendo
            move(__count)
            time.sleep(1)

            if __count % 3:
                msg()  
            
            #Pulando        
            jump(2)

            #Comendo           
            eat()
            time.sleep(1)

            #Bebendo           
            water()
            time.sleep(1)

            __count = __count + 1
            
            #Time do clico
            time.sleep(300)
    print('---------------------------'+ __count+'---------------------------')
 