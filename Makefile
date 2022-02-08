SHELL := bash

PHONY: install
install: 
	@poetry install
  
PHONY: brain-games
brain-games: 
	@poetry run brain-games
	
PHONY: build
build: 
	@poetry build

PHONY: publish
publish: 
	@poetry publish --dry-run

PHONY: package-install
publish: 
	@python3 -m pip install --user dist/*.whl
