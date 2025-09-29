<<<<<<< HEAD
import pyautogui
import os
import webbrowser
import time


mensagem = "Olá, tudo bem? sou um bot criado por Erick, está mensagem é automatica."


if os.path.getsize("telefones.txt") == 0:
    print("O arquivo está vazio.")
else:
    with open("telefones.txt", "r") as arquivo:
        for linha in arquivo:
            telefone = linha.strip()
            if telefone: 
                link = f"https://wa.me/{telefone}?text={mensagem.replace(' ', '%20')}"
                webbrowser.open(link)
                time.sleep(10)  

                
                pyautogui.press("enter")
                print(f"Mensagem enviada para {telefone}")
                time.sleep(5) 
                pyautogui.hotkey("alt","f4")
                time.sleep(2)
                pyautogui.hotkey("alt","f4")
=======
import pyautogui
import os
import webbrowser
import time


mensagem = "Olá, tudo bem? sou um bot criado por Erick, está mensagem é automatica."


if os.path.getsize("telefones.txt") == 0:
    print("O arquivo está vazio.")
else:
    with open("telefones.txt", "r") as arquivo:
        for linha in arquivo:
            telefone = linha.strip()
            if telefone: 
                link = f"https://wa.me/{telefone}?text={mensagem.replace(' ', '%20')}"
                webbrowser.open(link)
                time.sleep(10)  

                
                pyautogui.press("enter")
                print(f"Mensagem enviada para {telefone}")
                time.sleep(5) 
                pyautogui.hotkey("alt","f4")
                time.sleep(2)
                pyautogui.hotkey("alt","f4")
>>>>>>> 4e2ccf9ed7b0ef0a2b7a0ac03c443644f790fd0d
                time.sleep(2)