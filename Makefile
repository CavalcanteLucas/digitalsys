down:
	docker-compose down

up:
	docker-compose up --build

createadmin:
	chmod +x ./scripts/createadmin.sh
	./scripts/createadmin.sh
