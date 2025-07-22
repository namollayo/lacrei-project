# Lacrei Saúde - API de Agendamento de Consultas

Esta é uma API RESTful para gerenciamento de agendamentos de consultas médicas, desenvolvida como parte do desafio técnico da Lacrei Saúde.

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração do Ambiente de Desenvolvimento

1.  **Clone o repositório:**

    ```bash
    git clone <repository-url>
    cd lacrei-saude-api
    ```

2.  **Instale as dependências com Poetry:**

    ```bash
    poetry install
    ```

3.  **Configure as variáveis de ambiente:**

    Crie um arquivo `.env` a partir do exemplo:

    ```bash
    cp .env.example .env
    ```

    Revise e atualize as variáveis no arquivo `.env` conforme necessário.

## Executando com Docker

1.  **Construa e inicie os containers:**

    ```bash
    docker-compose up -d
    ```

2.  **Aplique as migrações do banco de dados:**

    ```bash
    docker-compose exec web poetry run python manage.py migrate
    ```

3.  **Crie um superusuário para acessar o Admin:**

    ```bash
    docker-compose exec web poetry run python manage.py createsuperuser
    ```

    Siga as instruções para criar um usuário administrador.

## Acessando a Aplicação

-   **API:** [http://localhost:8000/](http://localhost:8000/)
-   **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Verificando a Conexão com o PostgreSQL

Você pode verificar se a aplicação está conectada ao banco de dados de duas maneiras:

1.  **Acessando o container do banco de dados:**

    ```bash
    docker-compose exec db psql -U <DB_USER> -d <DB_NAME>
    ```

    Substitua `<DB_USER>` e `<DB_NAME>` pelos valores definidos no seu arquivo `.env`. Após conectar, você pode listar as tabelas com o comando `\dt` para ver as tabelas criadas pelo Django.

2.  **Acessando o Django Admin:**

    Acesse o painel de administração do Django e tente adicionar, editar ou remover algum dado. Se as operações forem bem-sucedidas, a conexão com o banco de dados está funcionando.

    
## Testando a API

Para testar os endpoints da API, você pode usar ferramentas como `curl` ou [Postman](https://www.postman.com/).

### Criando um Profissional

-   **Endpoint:** `POST /api/professionals/`
-   **Payload:**

    ```json
    {
        "social_name": "Dr. João da Silva",
        "profession": "Cardiologista",
        "address": "Rua das Flores, 123",
        "contact": "(11) 99999-9999"
    }
    ```

-   **Exemplo com `curl`:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"social_name": "Dr. João da Silva", "profession": "Cardiologista", "address": "Rua das Flores, 123", "contact": "(11) 99999-9999"}' http://localhost:8000/api/professionals/
    ```

### Criando uma Consulta

-   **Endpoint:** `POST /api/appointments/`
-   **Payload:**

    ```json
    {
        "date": "2025-12-31T14:00:00Z",
        "professional": 1
    }
    ```

-   **Exemplo com `curl`:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"date": "2025-12-31T14:00:00Z", "professional": 1}' http://localhost:8000/api/appointments/
    ```

### Buscando Consultas por Profissional

-   **Endpoint:** `GET /api/appointments/by-professional/<professional_id>/`

-   **Exemplo com `curl`:**

    ```bash
    curl http://localhost:8000/api/appointments/by-professional/1/
    ```

## Migrações

Após criar ou modificar modelos, você precisa criar e aplicar as migrações no banco de dados.

1.  **Criar migrações:**

    ```bash
    docker-compose exec web poetry run python manage.py makemigrations api
    ```

2.  **Aplicar migrações:**

    ```bash
    docker-compose exec web poetry run python manage.py migrate
    ```




## Documentação da API (Swagger UI)

A documentação da API é gerada automaticamente e está disponível em formato Swagger UI.

-   **Swagger UI:** [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
-   **ReDoc:** [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)
-   **Schema (YAML):** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

## Como Atualizar o Ambiente

Após as alterações, você precisa reconstruir a imagem do Docker para instalar a nova dependência e reiniciar os containers.

```bash
docker-compose up -d --build
```
