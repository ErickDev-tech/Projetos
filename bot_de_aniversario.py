import pyautogui
from datetime import datetime
import pyperclip


def menu_dino():
    pyautogui.moveTo(1243, 1051, duration=1) #Movimenta o mouse até o app do menu dino
    pyautogui.click(duration=0.2) # Clica no menu dino
    pyautogui.moveTo(996, 627, duration=50) #Movimenta o mouse para o botão entrar
    pyautogui.click() #Clica no botão entrar
    pyautogui.moveTo(1249, 222, duration=11) # Movimenta o mouse para um X de um pop up 
    pyautogui.click() #Clica no X 
    pyautogui.moveTo(56, 74, duration=1) #Movimenta o mouse para o caica
    pyautogui.click(duration=3) # Clica no caixa
    pyautogui.moveTo(545, 335, duration=2) #Movimenta o mouse para um janela 
    pyautogui.click(duration=1) #clica na janela
    pyautogui.write("350") #Escreve na janela o número 350
    pyautogui.press("f2") #aperta a telca f2
    pyautogui.moveTo(1482, 215, duration=1) # Movimenta o mouse para o X da janela 
    pyautogui.click(duration=1) #Clica no X


def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("ctrl", "v")


def preparar_whatsapp():
    # Executa só uma vez no início
    pyautogui.moveTo(1206, 1053, duration=2)  # vai até o zap
    pyautogui.click(duration=1)  # clica no zap
    pyautogui.moveTo(251, 119, duration=5)  # move para a área de procura


def mandar_mensagem(nome, numero):

    # Executa para cada aniversariante
    pyautogui.moveTo(251, 119, duration=1)
    pyautogui.click(duration=0.5)  # clica na barra de pesquisa
    pyautogui.write(numero)  # escreve o numero
    pyautogui.moveTo(238, 194, duration=0.3)  # desce para o numero
    pyautogui.click(duration=0.3)  # clica no numero
    pyautogui.moveTo(709, 1011, duration=1)  # move para area de mensagem
    pyautogui.click()  # clicar na área de mensagem
    escrever(f"""O Passaporte do Galeguinho jamais esqueceria uma data tão especial...
O SEU ANIVERSÁRIO! 🎉🎂

Hoje é dia de celebrar a vida de um cliente incrível, que faz parte da nossa história com muito carinho 💛
Por isso, viemos desejar a você:

Muita paz ✨, muito amor ❤️, saúde 💪, alegrias 😄 e conquistas incríveis 🏆!
Que cada novo ano traga momentos inesquecíveis e que seus sonhos continuem ganhando vida 🌟

Feliz Aniversário, {nome}!! 🎈
Com carinho,
Equipe Passaporte do Galeguinho!🌭🍔""")  # escreve a mensagem
    pyautogui.moveTo(1889, 1003, duration=0.5)  # move para o botão de enviar
    pyautogui.click(duration=1)  # clica no botão de enviar


aniversariantes = []

# Ler arquivo
with open("informacoes.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:
        linha = linha.strip()
        if linha:
            parte = linha.split(";")
            if len(parte) >= 2:
                nome = parte[0]
                numero = parte[1]
                data = parte[2]

                try:
                    data_arquivo = datetime.strptime(data, "%d/%m")
                    data_hoje = datetime.today()

                    if data_arquivo.day == data_hoje.day and data_arquivo.month == data_hoje.month:
                        aniversariantes.append((nome, numero))
                except ValueError:
                    print(f"Data inválida na linha: {linha}")
            else:
                print(f"Linha mal formatada: {linha}")


if aniversariantes:
    preparar_whatsapp()

    for nome, numero in aniversariantes:
        mandar_mensagem(nome, numero)

    menu_dino()

else:
    preparar_whatsapp()
    menu_dino()
