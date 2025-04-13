# IronKing

## Sobre
IronKing é uma aplicação para gerenciamento de jogos e competições.

## Tecnologias
- Backend:
  - Python
  - FastAPI
  - SQLAlchemy
- Frontend:
  - HTML
  - CSS (Bulma)
  - JavaScript (Alpine.js + HTMX)

## Instalação
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

### v0.0.1 (2024-03-19)
- ✨ Estrutura inicial do projeto
- 🎨 Setup do FastAPI com templates
- 🔧 Configuração básica do frontend com Bulma, Alpine.js e HTMX
- ♻️ Renomeação do projeto de IronKing Ranking para IronKing 