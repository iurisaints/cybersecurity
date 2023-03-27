import re

# Definir o caminho do arquivo de log
log_file = '/var/log/apache2/access.log'

# Ler o arquivo de log e armazenar as linhas em uma lista
with open(log_file, 'r') as f:
    log_lines = f.readlines()

# Definir as expressões regulares para procurar padrões suspeitos
regex_url = re.compile(r'"(GET|POST|HEAD) (.+) HTTP/\d\.\d"')  # Procura por URLs nas linhas do arquivo de log
regex_404 = re.compile(r'HTTP/\d\.\d" 404')  # Procura por solicitações de páginas inexistentes
regex_forbidden = re.compile(r'HTTP/\d\.\d" 403')  # Procura por tentativas de acesso a arquivos proibidos

# Percorrer as linhas do arquivo de log e procurar por padrões suspeitos
for line in log_lines:
    # Procurar por URLs na linha
    url_match = regex_url.search(line)
    if url_match:
        url = url_match.group(2)
        # Verificar se a URL contém caracteres suspeitos
        if '../' in url or '~' in url:
            print(f'[ALERTA] URL suspeita encontrada: {url}')

    # Procurar por solicitações de páginas inexistentes
    if regex_404.search(line):
        print('[ALERTA] Solicitação de página inexistente encontrada.')

    # Procurar por tentativas de acesso a arquivos proibidos
    if regex_forbidden.search(line):
        print('[ALERTA] Tentativa de acesso a arquivo proibido encontrada.')
