ifndef VERBOSE
.SILENT:
endif

.DEFAULT_GOAL := install

PROJECT := pyDayZ

## Installs a development environment
install: deploy

## Composes project using docker-compose 
deploy:
	docker-compose -f deployments/docker-compose.yml build
	docker-compose -f deployments/docker-compose.yml down -v
	docker-compose -f deployments/docker-compose.yml up -d --force-recreate