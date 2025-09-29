import os
import time 

Tarefas = [] #Lista que armazena as tarefas 
def voltar():
    input("\n Precione Enter para voltar ao menu principal")
    limpar_terminal()

def limpar_terminal(): #Função para limpar o terminal

    time.sleep(1)
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')

def adicionar_tarefa(): #Função para adicionar tarefa
    
    print("===== Adicionar Tarefa =====")
    tarefa = input("Adicione sua tarefa >>>>>").capitalize()
    if tarefa in Tarefas:
        print("Essa Tarefa já foi adicionada!!")
        time.sleep(2)
        visualizar_tarefa()
    else:
        Tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!!")
        visualizar_tarefa()
        
def remover_tarefa(): #Função para remover tarefa
    limpar_terminal()
    print("===== Remover Tarefas =====")
    if not Tarefas:
        print("Não há tarefas para remover!")
    else:
        for indice, tarefas in enumerate(Tarefas, start= 1):
            print(f"[{indice}]--{tarefas}")
        indice = int(input("Qual tarefa deseja remover!?"))
        if 1 <= indice <= len(Tarefas):
            tarefa_escolhida = Tarefas[indice - 1]
            print(f"A tarefa escolhida é {tarefa_escolhida}?")
            opção = int(input(" [1]Sim \n [2]Não \n >>>>") )
            if opção == 1:
                Tarefas.remove(tarefa_escolhida)
                print("Tarefa removida com sucesso!!!!")
                time.sleep(2)
                limpar_terminal()
            if opção == 2:
                limpar_terminal()
                print("Voltando para o inicio!!")
                main()
        
def visualizar_tarefa(): #Função para visualizar as tarefas
    limpar_terminal()
    print("===== Suas Tarefas =====")
    if Tarefas:
        for indice, tarefas in enumerate(Tarefas, start= 1):
            print(f"[{indice}]--{tarefas}")
    else:
        print("Nenhuma tarefa adicionada ainda")
    voltar()
           
def main():
    while True:
        print("===== Lista de Tarefas =====")
        print(" [1]Adicionar Tarefa \n [2]Remover Tarefa \n [3]Visualizar Tarefa \n [4]Sair")
        opção = int(input(">>>>>>"))
        if opção == 1:
            
            adicionar_tarefa()
            
        if opção == 2:
            
            remover_tarefa()
        if opção == 3:
            
            visualizar_tarefa()
        if opção == 4:
            print("===== Saindo do Sistema =====")
            time.sleep(2.2)
            limpar_terminal()
            break

main()
