.DEFAULT: all

all: lint run

run:
	poetry run uvicorn src.main:app --reload

lint:
	poetry run black src