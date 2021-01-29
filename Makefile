.PHONY: test

install: ## Install app & dependencies
	docker-compose build

start: ## Start the server
	docker-compose run app

stop: ## Stop the server
	docker-compose down

test: ## Test the application
	docker-compose run app coverage run --omit=*/tests/* -m unittest discover

test-verbose: ## Test the application in verbose mode
	docker-compose run app coverage run -m unittest discover -v

coverage-report: ## Run test with coverage
	docker-compose run app coverage report

