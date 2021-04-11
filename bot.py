import keyboard, pyautogui, time, mouse
from pynput.mouse import Button, Controller

#Configurações iniciais
time.sleep(2)
janela = pyautogui.getAllTitles()
print(janela)
mouse = Controller()

#Laço principal
while True:
    
    #Checar qual janela do lol está aberta
    janela = pyautogui.getAllTitles()
    
    #Executar se somente o client estiver aberto
    if "League of Legends" in janela and "League of Legends (TM) Client" not in janela:
        
        #Procurar partida
        if pyautogui.locateOnScreen("encontrar.png"):
            pyautogui.moveTo(pyautogui.locateOnScreen("encontrar.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("ENCONTRAR")
        print("1")
    
        #Aceitar partida
        if pyautogui.locateOnScreen("aceitar.png"):
            pyautogui.moveTo(pyautogui.locateOnScreen("aceitar.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("ACEITAR")
        print("2")
        
        #Jogar novamente no fim da partida
        if pyautogui.locateOnScreen("jogarnovamente.png"):
            pyautogui.moveTo(pyautogui.locateOnScreen("jogarnovamente.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            print("JOGAR DE NOVO")
            time.sleep(5)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
        print("3")
        
    #Checar se o jogo está aberto
    if "League of Legends (TM) Client" in janela:
        
        #Consultar quantidade de jogadores que ja sairam
        lista_0 = list(pyautogui.locateAllOnScreen("4.png"))
        
        #Sair da partida em caso de eliminação
        if pyautogui.locateOnScreen("sair.png"):
            pyautogui.moveTo(pyautogui.locateOnScreen("sair.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            print("SAIR")
        print("4")


        #Sair da partida em caso de 4o lugar
        while int(len(lista_0))>= 4 or pyautogui.locateOnScreen("4-3.png"):    
            keyboard.press_and_release("esc")
            time.sleep(2)
            print("4 LUGAR")
            pyautogui.moveTo(pyautogui.locateOnScreen("surrender.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(pyautogui.locateOnScreen("render-se.png"))
            while pyautogui.locateOnScreen("e.png"):
                pyautogui.moveTo(pyautogui.locateOnScreen("render-se.png"))
                mouse.press(Button.left)
                time.sleep(0.5)
                mouse.release(Button.left)
                lista_0 = []
                print("SURRENDER")
        print("5")
        
        #Comprar o campeão Nasus
        if pyautogui.locateOnScreen("nasus.png"):
            pyautogui.moveTo(pyautogui.locateOnScreen("nasus.png"))
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR NASUS")
        print("6")
        
        #Comprar a campeã Fiora
        if pyautogui.locateOnScreen("fiora.png"):
            pyautogui.moveTo(pyautogui.locateOnScreen("fiora.png"))
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR FIORA")
        print("7")