.DEFAULT_GOAL := serve
PWD := .

PORT := 8080
WITH_VENV := . $(PWD)/env/bin/activate && 

.PHONY: serve docker
serve: env ## start the server in development mode
	$(WITH_VENV) python $(PWD)/manage.py runserver 0.0.0.0:$(PORT)
#docker:
#	docker build -t buxfer_connector .


env: requirements.txt
	test -f $(PWD)/env && true || python3 -m venv env
	$(WITH_VENV) pip install -r requirements.txt
	

.PHONY: help
help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
