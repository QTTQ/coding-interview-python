TEST_PATH=./

test:
	python3 -m pytest --verbose --color=yes $(TEST_PATH)