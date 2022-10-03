import pyautogui, keyboard, threading, time, action

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

while True:
    if __finesh:
        break
    if not __pausar:
        #setGammaForZero()
        while __count < 500:
            #Comendo           
            action.eat()
            time.sleep(1)

            #Bebendo           
            action.water()
            time.sleep(1)

            #Movendo
            action.move(__count)
            time.sleep(1)

            #Pulando        
            action.jump(2)

            __count = __count + 1
            
            #Time do clico
            time.sleep(2)
    print('Estamos no ciclo: '+ __count)

    time.sleep(0.1)    


