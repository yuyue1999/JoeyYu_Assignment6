install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint: 
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

test: 
	python -m pytest -vv --nbval -cov=mylib -cov=main test_main.py  # Run tests after main.py



all: install format lint test
