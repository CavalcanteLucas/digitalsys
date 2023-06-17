# DigitalSys - Desafio Técnico

## Descrição

Este repositório contém uma aplicação Django que implementa uma API REST para gerenciamento de propostas de crédito.

## Requisitos

Para executar a aplicação, é necessário ter instalado `Docker` e `docker-compose`.

## Execução

Opcionalmente, utilize o arquivo `.example.env` como referência para criar um arquivo `.env` com credenciais para o banco de dados.

Execute o comando abaixo para subir os containers: com o banco de dados, com a aplicação, com o serviço de fila e com o celery worker. 
```
make up
```

A aplicação estará disponível em `http://localhost:8000/`.

Por conveniência e para efeitos de demonstração, o comando abaixo cria um super usuário e ter acesso ao painel administrativo do Django. Em um novo terminal, com a aplicação rodando, execute:
```
make createadmin
```

O painel estará disponível em `http://0.0.0.0:8000/admin/proposals/proposal/`.

Utilize as credenciais `admin:admin` para acessá-lo.

## Autor

Este projeto foi desenvolvido por [Lucas Cavalcante](www.github.com/CavalcanteLucas).
