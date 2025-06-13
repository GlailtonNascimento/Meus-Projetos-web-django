# Sistema de Reservas

![Versão do Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Versão do Django](https://img.shields.io/badge/Django-5.x-green.svg)
![Banco de Dados](https://img.shields.io/badge/Banco_de_Dados-MySQL-orange.svg)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-lightgrey.svg)

## 📝 Descrição

Este é um sistema de reservas web desenvolvido com Django, permitindo que usuários façam reservas e gerenciem itens de menu. O projeto foi estruturado para ser robusto, com validações de dados (como CPF condicional para diferentes ambientes) e um fluxo de trabalho de desenvolvimento claro.

## ✨ Funcionalidades

* **Gestão de Reservas:**
    * Criação de novas reservas com informações de contato, número de convidados, data e comentários.
    * Validação de CPF condicional: aceita qualquer sequência de 11 dígitos em modo de desenvolvimento (`DEBUG=True`) e validação rigorosa de CPF real em modo de produção (`DEBUG=False`).
* **Gestão de Itens de Menu:**
    * Adicionar, editar e remover itens do menu do restaurante através da interface administrativa.
* **Interface Administrativa:**
    * Utiliza o painel de administração padrão do Django para gerenciar facilmente reservas e itens de menu.

## 🚀 Tecnologias Utilizadas

* **Backend:** Python, Django 5.x
* **Banco de Dados:** MySQL (configurado para desenvolvimento, mas pode ser adaptado para PostgreSQL, SQLite, etc., em produção)
* **Frontend:** HTML, CSS, JavaScript (formulários e templates padrão do Django)
* **Controle de Versão:** Git & GitHub

## 🛠️ Instalação e Configuração (Ambiente de Desenvolvimento)

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o seguinte software instalado em seu sistema:

* **Python 3.x** (Recomendado Python 3.9 ou superior)
* **pip** (gerenciador de pacotes do Python, geralmente vem com o Python)
* **MySQL Server** (ou outro SGBD de sua preferência, ajustando as configurações no `settings.py`)

### Passos Detalhados

1.  **Clone o Repositório:**
    Abra seu terminal ou prompt de comando e clone o projeto:
    ```bash
    git clone [https://github.com/GlailtonNascimento/Meus-Projetos-web-django.git](https://github.com/GlailtonNascimento/Meus-Projetos-web-django.git)
    cd Meus-Projetos-web-django/SistemaDeReservas
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    É crucial usar um ambiente virtual para isolar as dependências do projeto e evitar conflitos.

    * No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as Dependências:**
    O projeto utiliza um arquivo `requirements.txt` para listar todas as bibliotecas Python necessárias.
    * Se você **não** tem um `requirements.txt` ainda e quer gerar com as suas bibliotecas atuais:
        ```bash
        pip freeze > requirements.txt
        ```
    * Para **instalar** todas as dependências do projeto:
        ```bash
        pip install -r requirements.txt
        ```
        * **Observação para MySQL:** Se você estiver usando MySQL, certifique-se de que o pacote `mysqlclient` está no `requirements.txt` ou instale-o manualmente:
            `pip install mysqlclient`

4.  **Configuração do Banco de Dados (MySQL):**
    * Crie um banco de dados MySQL chamado `django_db` (ou o nome que você preferir) no seu servidor MySQL.
    * Edite o arquivo `SistemaDeReservas/settings.py` e verifique a seção `DATABASES`. As credenciais (`USER`, `PASSWORD`, `HOST`, `PORT`) devem corresponder às suas configurações do MySQL.
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'django_db',
                'USER': 'root',
                'PASSWORD': '@123', # <-- ATENÇÃO: Altere para a sua senha do MySQL!
                'HOST': 'localhost',
                'PORT': '3306',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                },
            }
        }
        ```
        **É fundamental que a `PASSWORD` esteja correta para o seu usuário do MySQL.**

5.  **Aplique as Migrações:**
    Este comando criará as tabelas necessárias no seu banco de dados com base nos modelos do Django.
    ```bash
    python manage.py migrate
    ```

6.  **Crie um Superusuário (Acesso ao Painel de Administração):**
    Este passo é necessário para que você possa acessar o painel de administração do Django.
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções no terminal para definir seu nome de usuário, e-mail e senha.

7.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    O servidor estará ativo e acessível no seu navegador em `http://127.0.0.1:8000/`.

## 🧪 Testando a Validação de CPF

Este projeto implementa uma validação de CPF que se adapta ao ambiente de execução (desenvolvimento ou produção):

* **Em Ambiente de Desenvolvimento/Teste (`DEBUG=True`):**
    * Acesse o formulário de reserva (geralmente em `http://127.0.0.1:8000/reservar/`).
    * Você pode inserir **qualquer sequência de 11 dígitos numéricos** no campo CPF (ex: `11111111111`, `12345678901`). O sistema aceitará, desde que o comprimento seja 11 dígitos e o campo não esteja vazio.
    * Para confirmar que o modo `DEBUG` está ativo, observe o console ao iniciar o servidor: uma mensagem como `DEBUG está definido como: True` deve aparecer.

* **Em Ambiente de Produção (`DEBUG=False`):**
    * **Para simular este modo:** Edite o arquivo `SistemaDeReservas/settings.py` e altere a linha `DEBUG = True` para `DEBUG = False`. **Lembre-se de parar e reiniciar o servidor Django após esta mudança.**
    * Após a alteração e reinício, a validação completa e rigorosa do CPF será ativada. Apenas CPFs brasileiros formatados e válidos (com os dígitos verificadores corretos) serão aceitos.

## 🌐 Acessando a Aplicação

Após iniciar o servidor, você pode acessar as seguintes URLs no seu navegador:

* **Página Principal:** `http://127.0.0.1:8000/`
* **Página de Reservas:** `http://127.0.0.1:8000/reservar/` (Verifique seu `SistemaDeReservas/urls.py` e `firstapp/urls.py` para a URL exata do formulário de reserva)
* **Painel Administrativo:** `http://127.0.0.1:8000/admin/` (Use as credenciais do superusuário que você criou)

## 📦 Estrutura Simplificada do Projeto

SistemaDeReservas/             <-- Este é o diretório raiz do seu projeto Django
├── firstapp/                  # Seu aplicativo Django principal (models, views, forms, etc.)
│   ├── migrations/            # Histórico de alterações do banco de dados
│   ├── admin.py               # Registro de modelos para o painel administrativo
│   ├── forms.py               # Definição de formulários Django (incluindo a validação de CPF)
│   ├── models.py              # Definição dos modelos de dados (MenuItem, Reservation, CPFStatus)
│   ├── views.py               # Lógica das visualizações (o que o usuário vê e interage)
│   └── ...
├── SistemaDeReservas/         # Pasta de configurações do projeto Django (conf. globais)
│   ├── settings.py            # Configurações globais (DEBUG, Banco de Dados, etc.)
│   ├── urls.py                # Rotas URL principais do projeto
│   └── ...
├── static/                    # Arquivos estáticos globais (CSS, JavaScript, imagens)
├── templates/                 # Templates HTML globais do projeto
├── venv/                      # Ambiente virtual do Python (IGNORADO pelo Git)
├── manage.py                  # Utilitário de linha de comando do Django
├── .gitignore                 # Define quais arquivos e pastas o Git deve ignorar
└── README.md                  # Este arquivo! Descrição do projeto "Sistema de Reservas"

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para:

1.  Abrir uma [Issue](https://github.com/GlailtonNascimento/Meus-Projetos-web-django/issues) para relatar bugs ou sugerir novas funcionalidades.
2.  Enviar um [Pull Request](https://github.com/GlailtonNascimento/Meus-Projetos-web-django/pulls) com suas modificações.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### **Passos para o GitHub (Repetindo para Clareza):**

1.  **Abra o arquivo `README.md`** que está na sua pasta `SistemaDeReservas` no VS Code.
2.  **Cole o conteúdo COMPLETO acima** dentro desse arquivo.
3.  **Salve o arquivo.**
4.  **No seu terminal, navegue até a pasta `SistemaDeReservas`**:
    ```bash
    cd C:\Users\T\Documents\Meus-Projetos-web-django\SistemaDeReservas
    ```
5.  **Adicione e commite o `README.md`:**
    ```bash
    git add README.md
    git commit -m "Adiciona README.md detalhado para o projeto Sistema de Reservas"
    ```
6.  **Envie para o GitHub:**
    ```bash
    git push origin main
    ```