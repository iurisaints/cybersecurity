import hashlib
import sqlite3

# Conectando-se ao banco de dados
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Selecionando todas as senhas na tabela "usuarios"
cursor.execute('SELECT senha FROM usuarios')
senhas = cursor.fetchall()

# Verificando a força de cada senha
for senha in senhas:
    senha = senha[0] # Obtém a senha a partir do resultado da consulta
    hash_senha = hashlib.sha256(senha.encode()).hexdigest() # Gera um hash SHA-256 da senha
    
    # Verifica se a senha é fraca ou quebrável
    if len(senha) < 8 or senha.isnumeric() or senha.isalpha() or senha.lower() == senha or senha.upper() == senha:
        print(f'Senha fraca ou quebrável encontrada: {senha}')
    elif hash_senha in stolen_passwords:
        print(f'Senha comprometida encontrada: {senha}')
        
# Fechando a conexão com o banco de dados
conn.close()