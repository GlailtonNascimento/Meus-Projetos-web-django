# Meu Primeiro Projeto Django

Este é o meu primeiro projeto Django, criado para aprender os fundamentos do framework e construir aplicações web dinâmicas.

## Configuração

1.  Clone este repositório: `git clone <URL_DO_SEU_REPOSITÓRIO>`
2.  Navegue até a pasta do projeto: `cd firstproject`
3.  Crie um ambiente virtual: `python -m venv venv`
4.  Ative o ambiente virtual:
    * No Windows: `venv\Scripts\activate`
    * No macOS/Linux: `source venv/bin/activate`
5.  Instale as dependências: `pip install -r requirements.txt` (Se tiver um ficheiro `requirements.txt`. Caso contrário, instale as dependências manualmente, por exemplo: `pip install django mysqlclient`)
6.  **Configuração do Banco de Dados:** Este projeto está configurado para usar o MySQL. As configurações do banco de dados podem ser encontradas no ficheiro `firstproject/firstproject/settings.py`. Certifique-se de que as configurações (`ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`) correspondem ao seu servidor MySQL.
7.  Crie as tabelas do banco de dados: `python manage.py migrate`
8.  Crie um superutilizador para acessar o painel de administração: `python manage.py createsuperuser`

## Execução

Para executar o servidor de desenvolvimento:

```bash
python manage.py runserver