EMAIL_BACKEND# Installation

base requirements:

 * Docker
 * Docker-compose

optionaly:
* fabric / fabric3

instalation:

 * clone project
 * cat .env-example > .env

### build and run dev:

 * fab build
 * fab start
 * fab migrate
 * fab imprt_cities
 * fab runserver
 * fab run_watch
 * fab run_dev
 * ...
 * profit

 ### deploy:

 * connect
 * cd to /home/hamster/
 * git pull; docker-compose -f docker-compose.production.yml build; docker-compose down; docker-compose -f docker-compose.production.yml up -d
