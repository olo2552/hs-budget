.DEFAULT_GOAL := serve

PWD := .
PORT := 8080
USERNAME := admin
PASSWORD := admin

WITH_VENV := . $(PWD)/env/bin/activate && 
MANAGE_PY := python $(PWD)/manage.py
VENV_MANAGE_PY := $(WITH_VENV) $(MANAGE_PY)


.PHONY: serve docker
serve: env db.sqlite3 open-browser ## start the server in development mode
	$(VENV_MANAGE_PY) runserver 0.0.0.0:$(PORT)
#docker:
#	docker build -t buxfer_connector .


.PHONY: clear-db create-superuser open-browser
clear-db: ## remove everything from the database
	rm db.sqlite3

create-superuser: db.sqlite3 ## create Django superuser
	# TODO: Make this idempotent and add to `serve` prerequisites
	# TODO: Maybe rewrite it with PyExpect? o.0 :D
	$(WITH_VENV) expect $(PWD)/scripts/create-django-superuser $(MANAGE_PY) $(USERNAME) $(PASSWORD)

open-browser:
	(sleep 1; xdg-open localhost:$(PORT)/admin) &


env: requirements.txt
	test -f $(PWD)/env && true || python3 -m venv env
	$(WITH_VENV) pip install -r requirements.txt
db.sqlite3: env $(PWD)/main/migrations
	$(VENV_MANAGE_PY) migrate
	touch $(PWD)/db.sqlite3


.PHONY: help
help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
