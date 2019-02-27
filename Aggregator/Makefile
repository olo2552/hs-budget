.DEFAULT_GOAL := serve

PWD := .
PORT := 8080
USERNAME := admin
PASSWORD := admin
DOCKER_TAG := hs-budget-aggregator

WITH_VENV := . $(PWD)/env/bin/activate && 
MANAGE_PY := python $(PWD)/manage.py
VENV_MANAGE_PY := $(WITH_VENV) $(MANAGE_PY)


.PHONY: serve docker serve-container gunicorn-serve clear-db 
serve: env db.sqlite3 create-superuser open-browser ## start the server in development mode
	$(VENV_MANAGE_PY) runserver 0.0.0.0:$(PORT)

serve-container: docker open-browser ## start the server in a production-grade container
	docker run --rm -p $(PORT):8080 $(DOCKER_FLAGS) $(DOCKER_TAG) $(DOCKER_CMD)

docker: ## build Docker container
	docker build -t $(DOCKER_TAG) -f $(PWD)/deployment/Dockerfile .

#gunicorn-serve: env db.sqlite3 create-superuser open-browser ## run the app via Gunicorn locally
#	$(WITH_VENV) $(PWD)/scripts/entrypoint

clear-db: ## remove everything from the database
	rm db.sqlite3


.PHONY: create-superuser open-browser
create-superuser: db.sqlite3 ## create Django superuser
	$(WITH_VENV) python $(PWD)/scripts/create-django-superuser.py $(MANAGE_PY) $(USERNAME) $(PASSWORD)

open-browser:
	(sleep 2; xdg-open localhost:$(PORT)/admin) &


env: requirements.txt dev-requirements.txt
	test -f $(PWD)/env && true || python3 -m venv env
	$(WITH_VENV) pip install -r requirements.txt
	$(WITH_VENV) pip install -r dev-requirements.txt
	touch env
db.sqlite3: env $(PWD)/main/migrations
	$(VENV_MANAGE_PY) migrate
	touch $(PWD)/db.sqlite3


.PHONY: help
help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
