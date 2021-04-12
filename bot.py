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
        encontrar = pyautogui.locateOnScreen("encontrar.png")
        if encontrar:
            print("pau")
            pyautogui.moveTo(encontrar)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("ENCONTRAR")
        print("1")
    
        #Aceitar partida
        aceitar = pyautogui.locateOnScreen("aceitar.png")
        if aceitar:
            pyautogui.moveTo(aceitar)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("ACEITAR")
        print("2")
        
        #Jogar novamente no fim da partida
        jogar_novamente = pyautogui.locateOnScreen("jogarnovamente.png")
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
        
        #Consultar quantidade de jogadores que ja sairam
        lista_0 = list(pyautogui.locateAllOnScreen("4.png"))
        
        #Sair da partida em caso de eliminação
        sair = pyautogui.locateOnScreen("sair.png")
        if sair:
            pyautogui.moveTo(sair)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            print("SAIR")
        print("4")


        #Sair da partida em caso de 4o lugar ou demora
        rodada = pyautogui.locateOnScreen("4-6.png")
        while int(len(lista_0))>= 4 or rodada:    
            keyboard.press_and_release("esc")
            time.sleep(2)
            print("4 LUGAR")
            pyautogui.moveTo(pyautogui.locateOnScreen("surrender.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            render_se = pyautogui.locateOnScreen("render-se.png")
            pyautogui.moveTo(render_se)
            time.sleep(1)
            pyautogui.moveTo(pyautogui.locateOnScreen("e.png"))
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            lista_0 = []
            rodada = None
            print("SURRENDER")
        print("5")
        
        #Comprar o campeão Nasus
        nasus = pyautogui.locateOnScreen("nasus.png")
        if nasus:
            pyautogui.moveTo(nasus)
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR NASUS")
        print("6")
        
        #Comprar a campeã Fiora
        fiora = pyautogui.locateOnScreen("fiora.png")
        print(fiora)
        if fiora:
            pyautogui.moveTo(fiora)
            time.sleep(1)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            pyautogui.moveTo(800,450)
            print("COMPRAR FIORA")
        print("7")