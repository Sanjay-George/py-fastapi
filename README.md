### Contributing

1. Create environment
```bash
uv venv    
source .venv/bin/activate
```

2. Install packages
```bash
uv pip install --upgrade pip
uv pip install fastapi uvicorn[standard] sqlalchemy psycopg2-binary asyncpg pgvector typer langchain llama-index python-dotenv

uv pip install <all packages>
```

3. Freeze dependencies
```bash
uv pip freeze > requirements.txt
```

4. Run
```bash
make run
```