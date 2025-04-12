import mysql.connector

#Função de exclusão de tarefas

def excluir_tarefa():
  
        id_tarefa = input("Digite o ID da tarefa (Consultar na Listagem): ").strip()

        if not id_tarefa.isdigit():
            print("ID invalido")
            print("-" * 30)
            return

        conn = mysql.connector.connect(
            host="localhost",
            user="pedro", 
            port="3306",          
            password="senha123",
            database="tarefas_db",
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id_tarefa,))
        tarefa = cursor.fetchone()

        if not tarefa:
            print("Tarefa nao encontrada.")
            print("-" * 30)
            return


        confirm = input(f"Tem certeza que deseja excluir a tarefa (Essa acao nao podera ser desfeita)'{tarefa[1]}'? (S/N): ").strip().upper()
        if confirm != 'S':
            print("Exclusao cancelada")
            print("-" * 30)
            return


        cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_tarefa,))
        conn.commit()

        print("Tarefa excluida com sucesso.")
        print("-" * 30)

        cursor.close()
        conn.close()

