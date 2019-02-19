.DEFAULT_GOAL := serve
PWD := .

PORT := 8080
WITH_VENV := . $(PWD)/env/bin/activate && 

MANAGE_PY := $(WITH_VENV) python $(PWD)/manage.py

.PHONY: serve docker
serve: env db.sqlite3 ## start the server in development mode
	$(MANAGE_PY) runserver 0.0.0.0:$(PORT)
#docker:
#	docker build -t buxfer_connector .



.PHONY: clear-db venv
clear-db: ## remove everything from database
	rm db.sqlite3
create-superuser: db.sqlite3 ## create Django superuser (username: admin, pass: admin)
	$(WITH_VENV) $(PWD)/scripts/create-admin-admin

env: requirements.txt
	test -f $(PWD)/env && true || python3 -m venv env
	$(WITH_VENV) pip install -r requirements.txt
db.sqlite3: env $(PWD)/main/migrations
	$(MANAGE_PY) migrate
	touch $(PWD)/db.sqlite3

.PHONY: help
help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
