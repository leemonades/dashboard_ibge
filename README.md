## Dashboard IBGE
### Analise de dados por Estado.

# Pré Requisitos:
- Python 3.x
- PostgreSQL(opcional, detalhes no passo 6)


## Configuração do Ambiente para rodar o backend:

Siga estas etapas para configurar seu ambiente de desenvolvimento:

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


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}



7. Execute as migrações do Django:
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Popule o banco de dados com os dados providas pelo IBGE:
```bash
python manage.py load_ibge_data
```

9. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

10. Configure o CORS_ALLOWED_ORIGINS em `settings.py` de acordo com a porta que está rodando o backend:


## Configuração do Ambiente para rodar o frontend:

1. Installe o npm:
```bash
npm install
```

2. Execute o front:
```bash
npm start
```
