"""
Configurações do projeto Django 'firstproject'.

Gerado com 'django-admin startproject' usando Django 5.2.

Para mais informações, veja:
https://docs.djangoproject.com/pt-br/5.2/topics/settings/
"""

from pathlib import Path

# Caminho base do projeto (BASE_DIR / 'subpasta')
BASE_DIR = Path(__file__).resolve().parent.parent

# ATENÇÃO: Mantenha esta chave em segredo em produção!
SECRET_KEY = 'django-insecure-$t6vf(itrc=137*v+(d-_fg=kjkrwvw1#3l8&-0$1^9p$b^)f'

# ATENÇÃO: Não ative o modo DEBUG em produção
DEBUG = True

# Lista de hosts permitidos a acessar o projeto (em produção)
ALLOWED_HOSTS = []


# Aplicativos instalados no projeto
INSTALLED_APPS = [
    'django.contrib.admin',          # Interface de administração
    'django.contrib.auth',           # Sistema de autenticação
    'django.contrib.contenttypes',   # Tipos de conteúdo
    'django.contrib.sessions',       # Gerenciamento de sessões
    'django.contrib.messages',       # Sistema de mensagens
    'django.contrib.staticfiles',    # Arquivos estáticos (CSS, JS, imagens)
    'firstapp',                      # Sua aplicação personalizada
]

# Middleware: Camadas intermediárias que processam requisições e respostas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # <-- ADICIONAR AQUI
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arquivo principal de rotas (urls.py)
ROOT_URLCONF = 'firstproject.urls'

# Configurações de template HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pasta opcional para seus templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necessário para o admin funcionar
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Ponto de entrada para servidores WSGI (produção)
WSGI_APPLICATION = 'firstproject.wsgi.application'


# Banco de dados SQLite (padrão para desenvolvimento)
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': '@123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Validações de senha para usuários
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internacionalização
LANGUAGE_CODE = 'pt-br'  # Idioma do projeto

TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário

USE_I18N = True  # Ativa tradução

USE_TZ = True  # Usa timezone nativo

LOCALE_PATHS = [
    BASE_DIR / 'locale',  # Diretório onde ficarão os arquivos de tradução
]


# Configurações de arquivos estáticos (CSS, JavaScript, imagens)
STATIC_URL = 'static/'  # URL base para arquivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']  # Pasta onde ficam seus arquivos estáticos


# Campo padrão para chaves primárias nos modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
