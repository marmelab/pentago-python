.PHONY: test

install: ## Install docker environnement
	docker-compose build

start: ## Start the server
	docker-compose run app

stop: ## Stop the server
	docker-compose down

test: ## Test the application
	docker-compose run app python3 -m unittest discover -s ./ -v