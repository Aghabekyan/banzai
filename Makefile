migrations:
	docker-compose run --rm banzai python3 manage.py makemigrations

migrate: 
	docker-compose run --rm banzai python3 manage.py migrate

shell:
	docker-compose run --rm banzai python3 manage.py shell


