setup:
	python3.8 -m venv .venv && . .venv/bin/activate
	pip3 install --upgrade pip
	pip3 install -r requirements.dev
	pip3 install -r requirements.prod
	pip3 install pytest==5.4.3

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

test: clean
	. .venv/bin/activate && pytest tests --cov=src --cov-report=term-missing --cov-fail-under 40 #95

mypy:
	. .venv/bin/activate && mypy src

lint:
	#. .venv/bin/activate && pylint src -j 4 --reports=y

docs: FORCE
	cd docs; . .venv/bin/activate && sphinx-apidoc -o ./source ./src
	cd docs; . .venv/bin/activate && sphinx-build -b html ./source ./build
FORCE:

format:
	. .venv/bin/activate && black ./src/*.py
	. .venv/bin/activate && isort ./src/*.py -c -v

check: test lint mypy format