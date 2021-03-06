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
package-install:
	@python3 -m pip install --user dist/*.whl

PHONY: lint
lint:
	@poetry run flake8 brain_games
