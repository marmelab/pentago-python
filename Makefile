DOCKER := docker run -it --rm pentago-python

install: ## Build the docker container
	docker build -t pentago-python .

start: ## start the game.
	$(DOCKER) python3 ./pentago.py

test: ## Run the tests
	$(DOCKER) python3 -m unittest -v

local-run:
	python3 ./src/pentago.py

local-test: ## Run the tests on local machine
	python3 -m unittest discover -s ./src -v