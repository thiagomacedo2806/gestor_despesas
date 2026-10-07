# Gestor de Despesas

Este é um projeto funcional e minimalista construído em Django para gerenciar despesas pessoais de forma ágil e sem complicações de configuração.

## Funcionalidades

- Listar despesas cadastradas.
- Criar novas despesas via requisição JSON.

## Como Executar

1. Instale o Django:
```bash
pip install django
```

2. Inicialize as tabelas do banco de dados (SQLite embutido):
```bash
python manage.py migrate
```

3. Inicie o servidor:
```bash
python manage.py runserver
```

## Como Testar

Para executar os testes automatizados da aplicação:
```bash
python manage.py test tests
```