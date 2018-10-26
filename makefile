CONF_FILE=faas.yml

.PHONY: build
build:
	faas-cli build -f $(CONF_FILE)

.PHONY: push
push: build
	faas-cli push -f $(CONF_FILE)

.PHONY: deploy
deploy: push
	faas-cli deploy -f $(CONF_FILE)
