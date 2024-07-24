import requests
from bs4 import BeautifulSoup

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

print(CYAN + BOLD + r'''
                                                                                   
 _|_|_|_|_|                    _|_|_|                          _|_|_|              
     _|      _|_|    _|_|_|    _|    _|    _|_|    _|      _|  _|    _|  _|    _|  
     _|    _|    _|  _|    _|  _|    _|  _|_|_|_|  _|      _|  _|_|_|    _|    _|  
     _|    _|    _|  _|    _|  _|    _|  _|          _|  _|    _|        _|    _|  
     _|      _|_|    _|    _|  _|_|_|      _|_|_|      _|      _|          _|_|_|  
                                                                               _|  
                                                                           _|_| 
                        Buscador de vagas  
''' + RESET)

# Função para enviar mensagens ao Telegram
def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=payload)
    return response

# URL de exemplo
url = 'https://www.vagas.com.br/vagas-de-programador?m%5B%5D=100%25+Home+Office'

# Cabeçalhos HTTP para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.google.com/'
}

# Token e chat_id do bot do Telegram
TOKEN = ''
CHAT_ID = ''

# Realizando a requisição HTTP com cabeçalhos
response = requests.get(url, headers=headers)
status = response.status_code

if status == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrando todas as tags <a> com a classe específica
    titulos_vagas = soup.find_all('a', class_='link-detalhes-vaga')
    empresas_vagas = soup.find_all('span', class_='emprVaga')
    descricoes_vagas = soup.find_all('div', class_='detalhes')
    datas_publicacao = soup.find_all('span', class_='data-publicacao')

    for i in range(len(titulos_vagas)):
        titulo_vaga = titulos_vagas[i].text.strip()  # Obtendo o texto da tag <a>
        link_vaga = "https://www.vagas.com.br" + titulos_vagas[i]['href']  # Obtendo o link da vaga
        nome_empresa = empresas_vagas[i].text.strip() if i < len(empresas_vagas) else 'Empresa não informada'  # Obtendo o texto da tag <span>
        descricao_vaga = descricoes_vagas[i].text.strip() if i < len(descricoes_vagas) else 'Descrição não informada'  # Obtendo a descrição da vaga
        data_publicacao = datas_publicacao[i].text.strip() if i < len(datas_publicacao) else 'Data não informada'  # Obtendo a data de publicação
        
        # Verificando se a vaga é exclusiva para PCD
        vaga_pcd = 'Não'
        vaga_element = titulos_vagas[i].find_next('span', class_='vaga-pne')
        if vaga_element and vaga_element.text.strip():
            vaga_pcd = 'Sim'

        # Formatando a mensagem com emojis
        mensagem = (
            f"📢 *Vaga*: [{titulo_vaga}]({link_vaga})\n"
            f"🏢 *Empresa*: {nome_empresa}\n"
            f"📝 *Descrição*: {descricao_vaga}\n"
            f"📅 *Publicada*: {data_publicacao}\n"
            f"♿ *Exclusiva para PCD*: {vaga_pcd}\n"
        )

        # Enviando a mensagem para o Telegram
        send_message(TOKEN, CHAT_ID, mensagem)
else:
    print(f'Ocorreu um erro ao acessar o site. Status code: {status}')

print('Processo finalizado.')