# Buscador de Vagas de Emprego Automático 🖥️

## Descrição
Este projeto é um **buscador automático de vagas de emprego** desenvolvido em Python. O script realiza a raspagem de dados de sites de emprego e envia as vagas encontradas diretamente para um bot do Telegram. Cada vaga vem com detalhes importantes como título, nome da empresa, descrição, data de publicação e se é exclusiva para PCD. Tudo isso de forma automatizada!

## Funcionalidades
- 🕵️‍♂️ Raspa dados de sites de emprego usando BeautifulSoup.
- ✉️ Envia as vagas encontradas para um bot do Telegram.
- ℹ️ Inclui informações detalhadas sobre cada vaga, como título, empresa, descrição, data de publicação e mais.
- 📅 Adiciona emojis para deixar as mensagens mais atraentes e informativas.

## Exemplo de Saída
- 📢 **Vaga**: Especialista Front-End (Angular) Sênior
- 🏢 **Empresa**: Exemplo Tech
- 📝 **Descrição**: Como a maior empresa brasileira de tecnologia, temos o compromisso com uma política de diversidade...
- 📅 **Publicada**: Há 5 dias
- ♿ **Exclusiva para PCD**: Não

## Tecnologias Utilizadas
- Python
- Requests
- BeautifulSoup
- Telegram Bot API

## Como Usar
1. Clone o repositório:
   ```
   git clone https://github.com/tondevpy/buscador-de-vagas.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd pasta_do_projeto
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```
    Windows
    python -m venv env
    env\Scripts\activate

    Mac/Linux:
    python3 -m venv env
    source env/bin/activate

   ```

4. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

5. Configure o token do bot do Telegram e o chat ID no código:
   ```
    TOKEN = 'SEU_TOKEN_AQUI'
    CHAT_ID = 'SEU_CHAT_ID_AQUI'
   ```

6. Execute o script:
   ```
    python app.py
   ```

## Contribuição
Sinta-se à vontade para contribuir com melhorias, sugestões ou correções! Faça um fork do projeto, crie uma branch e envie um pull request. 😉

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato
Se tiver alguma dúvida ou sugestão, entre em contato comigo pelo https://www.tondevpy.com