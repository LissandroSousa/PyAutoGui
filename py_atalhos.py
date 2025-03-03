import pyautogui
import time

# POSIÇÃO DO MOUSE:
time.sleep(5) # espera de 5 segundos
pyautogui.position() # indica a posição do moouse

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# SEGURAR E SOLTAR TECLAS:
pyautogui.keyDown('enter')  # Pressiona a tecla
pyautogui.keyUp('enter')    # Solta a tecla

# DIGITAR CARACTERES:
pyautogui.write('Hello world!')  # Digita "Hello world!" instantaneamente
pyautogui.write('Hello world!', interval=0.25)  # Digita "Hello world!" com um intervalo de 0,25 segundos entre cada caractere

# PRECINAR TECLAS:
pyautogui.press('enter')  # Pressiona a tecla
pyautogui.press(['left', 'left', 'left']) # Pressiona a tecla 3 vezes
pyautogui.press('left', presses=3) # Pressiona a tecla 3 vezes

# ATALHOS:
pyautogui.hotkey('ctrl', 'c')  # ctrl-c para copiar
pyautogui.hotkey('ctrl', 'v')  # ctrl-v para colar

# CLICK DO MOUSE:
pyautogui.click(x=100, y=200) # Clica na posição
pyautogui.rightClick(x=100, y=200)
pyautogui.middleClick(x=100, y=200)
pyautogui.doubleClick(x=100, y=200)
pyautogui.tripleClick(x=100, y=200)
pyautogui.click(x=100, y=200, clicks=5, interval=5, button='left')

# ROLAGEM DO MOUSE:
pyautogui.scroll(10)   # Rolar para cima 10 "cliques"
pyautogui.scroll(-10)  # Rolar para baixo 10 "cliques"
pyautogui.scroll(10, x=100, y=100)  # Mover o cursor do mouse para (100, 200) e depois rolar para cima 10 "cliques"

