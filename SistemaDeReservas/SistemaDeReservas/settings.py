"""
Configurações do projeto Django 'SistemaDeReservas'. 

Gerado com 'django-admin startproject' usando Django 5.2.

Para mais informações, veja:
https://docs.djangoproject.com/pt-br/5.2/topics/settings/
"""
import os
from pathlib import Path

# Caminho base do projeto (BASE_DIR / 'subpasta')
BASE_DIR = Path(__file__).resolve().parent.parent

# ATENÇÃO: Mantenha esta chave em segredo em produção!
# A chave secreta agora será lida de uma variável de ambiente no PythonAnywhere
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-$t6vf(itrc=137*v+(d-_fg=kjkrwvw1#3l8&-0$1^9p$b^)f')

# ATENÇÃO: Não ative o modo DEBUG em produção
DEBUG = False

# Lista de hosts permitidos a acessar o projeto (em produção)
# Substitua 'GlailtonNascimento88.pythonanywhere.com' pelo seu domínio real no PythonAnywhere
ALLOWED_HOSTS = ['GlailtonNascimento88.pythonanywhere.com', 'localhost']


# Aplicativos instalados no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
]

# Middleware: Camadas intermediárias que processam requisições e respostas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ADICIONADO PARA SERVIR ARQUIVOS ESTÁTICOS EM PRODUÇÃO
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arquivo principal de rotas (urls.py)
ROOT_URLCONF = 'SistemaDeReservas.urls'

# Configurações de template HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Ponto de entrada para servidores WSGI (produção)
WSGI_APPLICATION = 'SistemaDeReservas.wsgi.application'


# Configuração do Banco de Dados MySQL para PythonAnywhere
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GlailtonNascimento88$default', # <--- USE O NOME EXATO DO SEU BANCO DE DADOS NO PYTHONANYWHERE
        'USER': 'GlailtonNascimento88', # <--- USE SEU NOME DE USUÁRIO DO PYTHONANYWHERE
        'PASSWORD': '@Geo2020', # <--- COLOQUE A SENHA REAL QUE VOCÊ ANOTOU AQUI!
        'HOST': 'glailtonnascimento88.mysql.pythonanywhere-services.com', # <--- USE O ENDEREÇO DO HOST DO PA
        'PORT': '3306', # Pode manter 3306
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
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# Configurações de arquivos estáticos (CSS, JavaScript, imagens)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # DIRETÓRIO PARA COLETAR ARQUIVOS ESTÁTICOS EM PRODUÇÃO


# Campo padrão para chaves primárias nos modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'