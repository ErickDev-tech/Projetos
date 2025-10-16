import webbrowser
import pyperclip
from time import sleep
from datetime import datetime
import pyautogui


def mandar_mensagem():
    with open("lista.txt", "r", encoding="utf-8") as lista:
        next(lista)  
        
        hoje = datetime.now().date()
        
        for linha in lista:
          
            partes = [p.strip() for p in linha.strip().split("|")]
            if len(partes) < 3:
                continue  
            
            nome = partes[0]
            numero = partes[1]
            data_str = partes[2]
            
           
            data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
            
           
            if data_obj == hoje:
                mensagem = f"Olá {nome}! Esta é uma mensagem automática."
                sleep(6)
                link = f"https://wa.me/{numero.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')}"
                webbrowser.open(link)
                sleep(10)
                escrever(mensagem)

                print(f"Mensagem pronta para {nome} ({numero})")


def escrever(texto):
     pyperclip.copy(texto)
     sleep(3)
     pyautogui.hotkey("ctrl","v")
     sleep(3)
     pyautogui.press("enter")



mandar_mensagem()
