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

# Example: make run-job JOB=batch2
run-job:
	python -m app.jobs.cli $(JOB)