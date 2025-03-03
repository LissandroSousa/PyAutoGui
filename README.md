# Automatizando Tarefas com PyAutoGUI

## Visão Geral
Este repositório contém dois scripts em Python que automatizam tarefas utilizando a biblioteca PyAutoGUI. Os scripts proporcionam acesso rápido a ações comuns de teclado e mouse, melhorando a eficiência do fluxo de trabalho.

### Arquivos:
1. **py_atalhos.py**: Um conjunto de comandos PyAutoGUI para referência rápida.
2. **funções.py**: Um script que automatiza tarefas repetitivas utilizando eventos de teclado e mouse.

---

## py_atalhos.py

### Descrição
Este script contém um conjunto de funções frequentemente usadas do PyAutoGUI, como:
- Verificar a posição do mouse.
- Simular pressionamento de teclas.
- Utilizar atalhos de teclado.
- Clicar e rolar com o mouse.

### Funcionalidades
- **Rastreamento da Posição do Mouse:** Exibe as coordenadas do cursor após um curto intervalo.
- **Controle do Teclado:** Simula pressionamento de teclas e combinações.
- **Controle do Mouse:** Realiza cliques simples, duplos, cliques com o botão direito e rolagens em posições especificadas.
- **Simulação de Digitação:** Digita automaticamente textos com intervalos configuráveis.

### Exemplo de Uso
```python
import pyautogui
import time

time.sleep(5)  # Aguarda 5 segundos
print(pyautogui.position())  # Obtém a posição do mouse

pyautogui.write('Olá, mundo!', interval=0.25)  # Digitação com atraso
pyautogui.hotkey('ctrl', 'c')  # Copia o texto
pyautogui.click(x=100, y=200)  # Clica na posição (100, 200)
pyautogui.scroll(10)  # Rola para cima
```

---

## funcoes.py

### Descrição
Este script automatiza uma série de tarefas repetitivas, como copiar, alternar entre janelas, clicar e colar texto. Ele roda em um loop e pode ser interrompido ao pressionar a tecla 'q'.

### Funcionalidades
- **Execução Automatizada de Tarefas:** Copia texto, alterna para outro aplicativo, cola o texto e clica em locais específicos.
- **Multithreading:** Utiliza threads para executar a automação e um listener em segundo plano para o comando de parada.
- **Interrupção pelo Teclado:** Pressione 'q' para parar a execução.

### Exemplo de Uso
```python
import time
import pyautogui
import threading
import os
import keyboard

def automatizar_tarefa():
    while True:
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'c')  # Copiar
        time.sleep(0.5)
        pyautogui.hotkey('winleft', '4')  # Alternar janela
        time.sleep(0.5)
        pyautogui.doubleClick(x=616, y=267)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')  # Colar
        time.sleep(0.5)
        pyautogui.click(x=658, y=365)  # Confirmar ação

def parar_script():
    while True:
        if keyboard.is_pressed('q'):
            os._exit(0)  # Interrompe a execução

threading.Thread(target=parar_script).start()
pyautogui.hotkey('winleft', '5')  # Abre o aplicativo 5
threading.Thread(target=automatizar_tarefa).start()
```

---

## Requisitos

Para rodar esses scripts, instale as seguintes dependências:
```bash
pip install pyautogui keyboard
```

---

## Notas
- Ajuste as coordenadas dos cliques do mouse para corresponder à resolução da sua tela.
- Certifique-se de que os aplicativos necessários estejam abertos antes de executar `funcoes.py`.
- Pressione 'q' a qualquer momento para interromper a automação.

---

## Licença
Este projeto é open-source e está disponível para uso pessoal e profissional.

