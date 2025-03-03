📌 Atalhos e Funções com PyAutoGUI

Este repositório contém scripts em Python que utilizam a biblioteca pyautogui para automação de tarefas repetitivas, aumentando a produtividade e a velocidade no trabalho.

📂 Arquivos

1️⃣ py_atalhos.py

Este arquivo inclui uma coleção de comandos prontos para manipulação do mouse e do teclado com pyautogui. Ele pode ser utilizado como um repositório de referência rápida para atalhos e comandos comuns, incluindo:

Obtenção da posição do mouse.

Simulação de pressionamento de teclas.

Digitação de textos automaticamente.

Uso de combinações de teclas (atalhos).

Cliques do mouse (simples, duplo, triplo, com botão direito, entre outros).

Rolagem do mouse.

2️⃣ funções.py

Este arquivo implementa uma função automatizada para copiar e colar textos utilizando pyautogui, bem como um atalho para encerrar a execução pressionando a tecla q. Ele contém:

**Função **``: Executa uma série de comandos automaticamente, incluindo copiar, colar e interagir com janelas.

**Função **``: Monitora a tecla q para interromper o programa.

Execução em threads: Permite que ambas as funções rodem simultaneamente sem travar a execução.

📌 Requisitos

Para executar os scripts, é necessário instalar as bibliotecas:

time
pyautogui
threading
os
keyboard

⚠️ Aviso

Os scripts manipulam diretamente o mouse e o teclado. Certifique-se de testá-los em um ambiente seguro antes de utilizá-los em aplicações importantes.
