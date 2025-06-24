import mysql.connector

#Função de cadastro de tarefas 

def cadastro_tarefa():
    print("Insira o Título: ")
    titulo = input("")

    print("Insira a Descrição: ")
    descricao = input("")

    print("Status (C - Concluída / P - Pendente): ")
    status_input = input("").strip().upper()

    if status_input == 'C':
        status = True
    elif status_input == 'P':
        status = False
    else:
        print("Status inválido. Usando Pendente como padrão.")
        print("-" * 30)
        status = False


    conn = mysql.connector.connect(
        host="localhost",
        user="SEU_USUARIO",
        port="3306",
        password="SUA_SENHA",
        database="tarefas_db"
    )

    cursor = conn.cursor()

    query = "INSERT INTO tarefas (titulo, descricao, status) VALUES (%s, %s, %s)"
    valores = (titulo, descricao, status)

    cursor.execute(query, valores)
    conn.commit()

    print("Tarefa cadastrada com sucesso!")
    print("-" * 30)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    cadastro_tarefa()


