import hashlib
from cryptography.fernet import Fernet

# Gera uma chave de criptografia aleatória
key = Fernet.generate_key()

# Cria o objeto Fernet com a chave gerada
cipher = Fernet(key)

# Arquivo para criptografar
file_name = "cryptography/arquivo.txt"

with open(file_name, "rb") as f:
    data = f.read()

# Criptografa os dados
encrypted_data = cipher.encrypt(data)

# Salva os dados criptografados em um arquivo
with open("arquivo_criptografado.txt", "wb") as f:
    f.write(encrypted_data)

# Verifica a integridade dos dados
hash_value = hashlib.sha256(data).hexdigest()
encrypted_hash_value = hashlib.sha256(encrypted_data).hexdigest()

if hash_value == encrypted_hash_value:
    print("Os dados foram criptografados com sucesso!")
else:
    print("Ocorreu um erro durante a criptografia!")
