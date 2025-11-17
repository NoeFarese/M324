PYTHON = python3
SRC_DIR = src
TEST_DIR = tests

.PHONY: test coverage clean

test:
	python3 -m unittest discover -s $(TEST_DIR) -p "test*.py"

coverage:
	python3 -m coverage run --source=$(SRC_DIR) -m unittest discover -s $(TEST_DIR) -p "test*.py"
	python3 -m coverage report -m
	rm -f .coverage
