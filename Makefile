run:
	uvicorn app.main:app --reload

format:
	black app

lint:
	ruff app

typecheck:
	mypy app

freeze:
	uv pip freeze > requirements.txt

# Example: make run-job JOB=print-hello-world
run-job:
	python -m app.jobs.cli $(JOB)