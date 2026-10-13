#importando a biblioteca pymysql
import pymysql
from time import sleep

#config do banco de dados
conexao = None
cursor = None
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='empresa',
)
try:
    # Conexão com servidor
    cursor = conexao.cursor()

    #Cria um banco de dados com o Nome cadastro!
    cursor.execute('''CREATE DATABASE IF NOT EXISTS Empresa''')


    #Cria uma tabela para seu banco de dados com os registros
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS funcionarios (
           id INT AUTO_INCREMENT PRIMARY KEY,
           nome VARCHAR(60) NOT NULL,
           idade tinyint NOT NULL,
          cpf VARCHAR(11) UNIQUE NOT NULL,
           sexo CHAR(1) NOT NULL,
           salario float NOT NULL,
           cargo VARCHAR(50) NOT NULL
       )
       """)

    #Mensagem de entrada do servidor
    print('-=-'*30)
    print('Sistema de Cadastro de Funcionarios')
    print('-=-'*30)

    #Captura os dados digitados por você no terminal
    nome = str(input('Digite o nome completo do funcionario(a): '))
    idade = int(input('Digite a idade do funcionario(a): '))
    sexo = str(input('Digite o sexo do funcionario(a) M para masculino ou F para feminino: '))
    cpf = str(input('Digite o cpf do funcionario(a) 11 Digitos: '))
    salario = float(input('Digite o salario do funcionario(a): R$'))
    cargo = str(input('Digite o cargo do funcionario(a): '))

    #Inserindo os dados no Banco de dados
    comando_sql = '''INSERT INTO funcionarios(nome,idade,sexo,cpf,salario,cargo) VALUES (%s,%s,%s,%s,%s,%s)'''

    valores = (nome, idade, sexo, cpf, salario, cargo)

    cursor.execute(comando_sql, valores)

    #Gravando as alterações no banco de dados
    conexao.commit()
    print('-=-'*30)
    print('Cadastrando funcionario.....')
    print('-=-' * 30)
    sleep(2)

    print(f'\n✅ \033[32mFuncionario {nome} cadastrado com sucesso no banco de dados')


    #Caso o dado inserido esteja errado
except pymysql.MySQLError as erro:
    print(f"\n❌ \033[31mErro no banco de dados: {erro}")

finally:
    # Fechamento do sistema
    if cursor is not None:
        cursor.close()
    if conexao is not None:
        if hasattr (conexao, 'open') and conexao.open:
            conexao.close()