# Fase 1 – Arquitetura Monolítica

Nesta fase, toda a aplicação roda em UMA ÚNICA MÁQUINA VIRTUAL.

## Arquitetura

- Frontend (HTML)
- Backend (Python + FastAPI)
- Banco de Dados (PostgreSQL)

Tudo no mesmo servidor.

## Objetivo didático

- Simplicidade
- Rápida implementação
- Identificar o Single Point of Failure (SPOF)

## Pré-requisitos

VM: orders-monolith
SO: Ubuntu Server 22.04
CPU: 2 vCPU
RAM: 2 GB
Disco: 20 GB
Rede: bridge padrão
- Python 3
- PostgreSQL

## Passos

1. Instalar dependências
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip postgresql postgresql-contrib git

2. Configurar e criar banco de dados
sudo -u postgres psql

- CREATE DATABASE orders;
- CREATE USER orders WITH PASSWORD 'orders';
- GRANT ALL PRIVILEGES ON DATABASE orders TO orders;
- \q

- psql -h localhost -U orders -d orders
CREATE TABLE orders (id SERIAL PRIMARY KEY, product TEXT, quantity INT, status TEXT, created_at TIMESTAMP DEFAULT NOW());

3. Criar a estrutura e rodar a aplicação
- mkdir ~/simple-orders
- cd ~/simple-orders

Clone dos arquivos do Git

- pip3 install -r requirements.txt
- uvicorn app:app --host 0.0.0.0 --port 8000

4. Testar no navegador e realizar algumas ordens
5. Entrar no banco de dados e verificar as entradas na tabela para validar funcionamento da aplicação
6. Printar tela que mostra as entradas na tabela
