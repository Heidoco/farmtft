import keyboard, pyautogui, time, mouse, pygetwindow
from pynput.mouse import Button, Controller

#Configurações iniciais
time.sleep(2)
janela = pyautogui.getAllTitles()
print(janela)
mouse = Controller()



client = pygetwindow.getWindowsWithTitle("League Of Legends")[0]
client.moveTo(0,0)

#Laço principal
while True:
    #a = time.localtime()
    #b = time.strftime("%H:%M:%S", a)
    #print(b)
    #Checar qual janela do lol está aberta
    
    janela = pyautogui.getAllTitles()
    
    #Executar se somente o client estiver aberto
    if "League of Legends (TM) Client" not in janela:
        
        #Procurar partida
        encontrar = pyautogui.locateOnScreen("encontrar.png",region=(400,650, 250, 50),grayscale=True)
        if encontrar:
            pyautogui.moveTo(encontrar)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("ENCONTRAR")
        print("1")
    
        #Aceitar partida
        aceitar = pyautogui.locateOnScreen("aceitar.png",region=(530, 525, 200, 100),grayscale=True)
        if aceitar:
            pyautogui.moveTo(aceitar)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("ACEITAR")
        print("2")
        
        #Jogar novamente no fim da partida
        jogar_novamente = pyautogui.locateOnScreen("jogarnovamente.png",region=(400,650, 250, 50),grayscale=True)
        if jogar_novamente:
            pyautogui.moveTo(jogar_novamente)
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
        
        jogo = pygetwindow.getWindowsWithTitle("League of Legends (TM) Client")[0]
        jogo.moveTo(0,0)
        
        #Consultar quantidade de jogadores que ja sairam
        lista_0 = list(pyautogui.locateAllOnScreen("4.png",region=(1200, 330, 60, 220),grayscale=True))
        
        #Sair da partida em caso de eliminação
        sair = pyautogui.locateOnScreen("sair.png",region=(450,270, 440, 210),grayscale=True)
        if sair:
            pyautogui.moveTo(sair)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            print("SAIR")
        print("4")


        #Sair da partida em caso de 4o lugar ou demora
        rodada = pyautogui.locateOnScreen("4-6.png",region=(250,0, 600, 100), grayscale=True, confidence=0.9)
        print(rodada)
        while int(len(lista_0))>= 4 or rodada:
            keyboard.press_and_release("esc")
            time.sleep(2)
            print("4 LUGAR")
            pyautogui.moveTo(pyautogui.locateOnScreen("surrender.png",region=(0,0, 1280, 720),grayscale=True))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            time.sleep(1)
            pyautogui.moveTo(555,327)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            lista_0 = []
            rodada = None
            print("SURRENDER")
        print("5")
        
        #Comprar o campeão Nasus
        """
        nasus = pyautogui.locateOnScreen("nasus.png",region=(315,610, 677, 112),grayscale=True)
        if nasus:
            pyautogui.moveTo(nasus)
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR NASUS")
        print("6")
        """
        #Comprar a campeã Fiora
        fiora = pyautogui.locateOnScreen("fiora.png",region=(315,610, 677, 112),grayscale=True)
        if fiora:
            pyautogui.moveTo(fiora)
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR Sapo")
        print("7")
        
        maokai = pyautogui.locateOnScreen("maokai.png",region=(315,610, 677, 112),grayscale=True)
        if maokai:
            pyautogui.moveTo(maokai)
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR Maokai")
        print("8")