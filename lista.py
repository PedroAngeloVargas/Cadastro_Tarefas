import mysql.connector

#Função de listagem de tarefas

def listar_tarefas():
    
        conn = mysql.connector.connect(
            host="localhost",
            user="SEU_USUARIO",  
            port="3306",
            password="SUA_SENHA",
            database="tarefas_db",
    
        )

        cursor = conn.cursor()

        query = "SELECT id, titulo, descricao, status FROM tarefas"
        cursor.execute(query)

        tarefas = cursor.fetchall()

        if not tarefas:
            print("Nenhuma tarefa encontrada.")
            print("-" * 30)
            return

        print("\n=== Lista de Tarefas ===")
        for tarefa in tarefas:
            id, titulo, descricao, status = tarefa
            status_str = "Concluída" if status else "Pendente"
            print(f"ID: {id}")
            print(f"Título: {titulo}")
            print(f"Descrição: {descricao}")
            print(f"Status: {status_str}")
            print("-" * 30)

        cursor.close()
        conn.close()
