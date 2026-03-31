.PHONY: setup run evals clean

setup:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
	cp .env.example .env
	@echo "Setup completo! Adicione ANTHROPIC_API_KEY no .env"

run:
	.venv/bin/jupyter notebook

evals:
	.venv/bin/python tests/run_evals_ci.py

clean:
	find . -name "*.pyc" -delete
	find . -name ".ipynb_checkpoints" -type d -exec rm -rf {} +
