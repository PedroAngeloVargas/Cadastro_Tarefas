import mysql.connector

#Função de alteração de status

def alterar_status_tarefa():

        conn = mysql.connector.connect(
            host="localhost",  
            user="pedro",
            port="3306", 
            password="senha123",  
            database="tarefas_db"  
        )

        cursor = conn.cursor()

        print("Insira o ID da tarefa (Consultar na listagem): ")
        id_tarefa = input()

        cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id_tarefa,))
        tarefa = cursor.fetchone()

        if not tarefa:
            print("Tarefa nao encontrada.")
            print("-" * 30)
            return


        confirm = input(f"Tem certeza que deseja alterar o status da tarefa '{tarefa[1]}'? (S/N): ").strip().upper()
        if confirm != 'S':
            print("Alteracao cancelada")
            print("-" * 30)
            return

        print("Insira o novo Status C - Concluída / P - Pendente): ")
        status_input = input().strip().upper()

        if status_input == 'C':
            status = True
        elif status_input == 'P':
            status = False
        else:
            print("Status inválido. Usando Pendente como padrão.")
            print("-" * 30)
            status = False

        query = "UPDATE tarefas SET status = %s WHERE id = %s"
        valores = (status, id_tarefa)

        cursor.execute(query, valores)
        conn.commit()  

        print("Status da tarefa atualizado com sucesso!")
        print("-" * 30)

  
        cursor.close()
        conn.close()

if __name__ == "__main__":

    id_tarefa = 1  
    status = True  
    
    alterar_status_tarefa(id_tarefa, status)

