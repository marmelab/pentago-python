.PHONY: test
export UID = $(shell id -u)
export GID = $(shell id -g)

install: ## Install docker environnement
	docker-compose build

start: ## Start the server
	docker-compose up

stop: ## Stop the server
	docker-compose down

test: ## Test the application
	docker-compose run app python3 -m unittest discover -s ./ -v