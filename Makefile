SHELL := bash

PHONY: install
install: 
	@poetry install
  
PHONY: brain-games
brain-games: 
	@poetry run brain-games
