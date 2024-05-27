## Dashboard IBGE
### Análise de dados por Estado.

# Índice
- [Pré-requisitos](#pré-requisitos)
- [Configurar Backend](#configurar-backend)
- [Configurar Frontend](#configurar-frontend)

## Pré-requisitos:
- Python 3.x
- PostgreSQL (opcional, detalhes no passo 6)

## Configuração do Ambiente

### Configurar Backend
Siga estas etapas para configurar seu ambiente de desenvolvimento para o backend:

1. Clone o repositório:
    ```bash
    git clone https://github.com/leemonades/dashboard_ibge
    ```
2. Acesse o repositório do back:
    ```bash
    cd dashboard_back
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```
5. Instale as dependências do projeto:
    ```bash
    pip install --upgrade pip 
    pip install -r requirements.txt
    ```
6. Crie um banco de dados Postgres e atualize as configurações do arquivo `settings.py` com suas credenciais. Caso não queira utilizar Postgres, utilize SQLite atualizando a variável `DATABASES`:

    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "mydatabase",
        }
    }
    ```
7. Execute as migrações do Django:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

8. Acesse o diretório do script:
    ```bash
    cd dashboard_back/dashboard_ibge/script
    ```
9. Execute o script para gerar os dados:
    ```bash
    python gerar_dados_ibge.py
    ```
10. Volte para o diretório dashboard_back
    ```bash
    cd ../..
    ```
11. Popule o banco de dados com os dados providos pelo IBGE:
    ```bash
    python manage.py load_ibge_data
    ```
12. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
13. Configure o `CORS_ALLOWED_ORIGINS` em `settings.py` de acordo com a porta que está rodando o frontend.

### Configurar Frontend
Siga estas etapas para configurar seu ambiente de desenvolvimento para o frontend:

1. Instale o npm:
    ```bash
    npm install
    ```
2. Execute o front:
    ```bash
    npm start
    ```
