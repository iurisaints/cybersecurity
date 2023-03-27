import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('banco_de_dados.db')

# Realizar consulta SQL na tabela de usuários
cursor = conn.execute('SELECT nome, senha FROM usuarios')

# Senhas fracas e quebráveis
senhas_fraca = ['123456', 'senha123', 'qwerty', 'abc123']

# Verificar as senhas dos usuários
for row in cursor:
    nome = row[0]
    senha = row[1]
    if len(senha) < 8 or not any(c.isupper() for c in senha) or not any(c.islower() for c in senha) or not any(c.isdigit() for c in senha) or not any(c in '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`' for c in senha):
        print(f'A senha do usuário {nome} é fraca e deve ser alterada.')
    elif senha in senhas_fraca:
        print(f'A senha do usuário {nome} é quebrável e deve ser alterada.')
    else:
        print(f'A senha do usuário {nome} é forte.')
    
# Fechar a conexão com o banco de dados
conn.close()