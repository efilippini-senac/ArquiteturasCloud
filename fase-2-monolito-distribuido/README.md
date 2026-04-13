# Fase 2 – Monolito Distribuído

Nesta fase, a aplicação continua sendo UM MONOLITO,
mas distribuído em MÚLTIPLAS MÁQUINAS.

## Arquitetura

- VM Frontend (HTML)
- VM Backend (FastAPI)
- VM Database (PostgreSQL)

## Importante

Mesmo estando separado em VMs diferentes:
- O backend continua sendo um único sistema
- O deploy ainda é acoplado
- NÃO é microserviço

## Objetivo didático

- Introduzir comunicação em rede
- Separar responsabilidades
- Trabalhar latência e dependência entre serviços

## Passos

Para o front>>>>
Subir um Nginx no servidor de front e hospedar o site.

Para database>>>>

Editar arquivo /etc/postgresql/14/main/postgresql.conf
listen_addresses = '*'

Editar arquivo /etc/postgresql/14/main/pg_hba.conf e adicionar:
host all all 0.0.0.0/0 md5

Reiniciar PG
sudo systemctl restart postgresql

Check PG
ss -lntp | grep 5432

Para o backend>>>>

Exportar variáveis de ambiente:
export DB_HOST=IP_DA_VM_DB
export DB_NAME=orders
export DB_USER=orders
export DB_PASS=orders

Rodar aplicação (backend)
uvicorn app:app --host 0.0.0.0 --port 8000