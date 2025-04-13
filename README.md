# IronKing

## Sobre
IronKing é uma aplicação para gerenciamento de jogos e competições.

## Tecnologias
- Backend:
  - Python
  - FastAPI
  - SQLAlchemy
  - PostgreSQL
- Frontend:
  - HTML
  - CSS (Bulma)
  - JavaScript (Alpine.js + HTMX)
- DevOps:
  - Docker
  - Docker Compose

## Instalação

### Usando Docker (Recomendado)
1. Clone o repositório
```bash
git clone https://github.com/Oracy/IronKing.git
cd IronKing
```

2. Crie um arquivo `.env` baseado no `.env_template`
```bash
cp .env_template .env
```

3. Inicie os containers
```bash
docker compose up -d
```

4. Acesse a aplicação em `http://localhost:8000`

### Instalação Local
1. Clone o repositório
```bash
git clone https://github.com/Oracy/IronKing.git
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
```

3. Instale as dependências
```bash
cd backend
pip install -r requirements.txt
```

4. Execute o servidor
```bash
uvicorn app.main:app --reload
```

5. Acesse a aplicação em `http://localhost:8000`

## Versões

### v0.0.2 (2024-04-13)
- 🐳 Adição de suporte a Docker
- 🗃️ Integração com PostgreSQL
- 🔧 Correção dos caminhos de arquivos estáticos
- 📝 Atualização da documentação

### v0.0.1 (2024-03-19)
- ✨ Estrutura inicial do projeto
- 🎨 Setup do FastAPI com templates
- 🔧 Configuração básica do frontend com Bulma, Alpine.js e HTMX
- ♻️ Renomeação do projeto de IronKing Ranking para IronKing 