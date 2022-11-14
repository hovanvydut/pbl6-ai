dc-up:
	docker compose up -d --build --remove-orphans
install:
	pip install -r requirements.txt
install-local:
	pip install -r requirements-local.txt
run:
	uvicorn app:app --reload --host 0.0.0.0