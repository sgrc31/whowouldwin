.PHONY: runserver
runserver:
	cd src/ && poetry run python3 manage.py runserver

.PHONY: test
test:
	poetry run pytest --cov

.PHONY: clean
clean:
	find src/ tests/ -name "*~" -type f -delete
	find src/ tests/ -name "*.pyc" -type f -delete
	find src/ tests/ -name "__pycache__" -type d -delete
