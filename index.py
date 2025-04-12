from cadastro import cadastro_tarefa
from lista import listar_tarefas
from alterar import alterar_status_tarefa
from excluir import excluir_tarefa
import mysql.connector
import math

# Função principal. Pagina inicial

def main():
    while True:
        print("\n\U0001F525", "Sistema de Controle de Tarefas :P", "\U0001F525\n")
        print("1 - Cadastrar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Alterar Status")
        print("4 - Excluir Tarefa")
        print("0 - Sair")
        op = input("Qual opcao? ")
        print("-" * 30)

        match op:

            case "1":
                cadastro_tarefa()
            case "2":
                listar_tarefas()
            case "3":
                alterar_status_tarefa()
            case "4":
                excluir_tarefa()
            case "0":
                print("Saindo...")
                break


if __name__ == "__main__":
    main()