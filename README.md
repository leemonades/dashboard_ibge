# Dashboard IBGE
Este é um projeto de dashboard que utilizam :

FRONTEND: React
BACKEND: Django Rest Framework
GRAFICOS: biblioteca Plotly
API alimentado: https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo_ibge_uf}/municipios

## Configuração do Ambiente para rodar o backend:

Siga estas etapas para configurar seu ambiente de desenvolvimento:

1. Clone o repositório:
```bash
git clone https://github.com/leemonades/dashboard_ibge
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
source venv/bin/activate
```

4. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

5. Configure o banco de dados:
```bash
Crie um banco de dados Postgres e atualize as configurações do arquivo `settings.py` com suas credenciais.
```

6. Execute as migrações do Django:
```bash
python manage.py migrate
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```