import sqlite3

# Conectando-se ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect('usuarios.db')

# Criando a tabela "usuarios"
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        senha TEXT
    );
''')

# Inserindo alguns usuários de exemplo na tabela
usuarios = [
    ('Alice', 'senha123'),
    ('Bob', '12345678'),
    ('Charlie', 'qwerty'),
    ('David', 'P@ssword')
]
cursor.executemany('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', usuarios)

# Salvando as alterações e fechando a conexão com o banco de dados
conn.commit()
conn.close()