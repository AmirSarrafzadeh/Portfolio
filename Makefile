# Apply migrations
migrate:
	@echo "Applying database migrations..."
	python manage.py migrate

# Make migrations
make:
	@echo "Creating database migrations..."
	python manage.py makemigrations

# Run the Loyalty application
run:
	@echo "Starting Loyalty application..."
	python manage.py runserver

static:
	@echo "Collecting static files..."
	python manage.py collectstatic

# Create requirements.txt and push to git
push:
	@echo "Creating requirements.txt"
	pip freeze > requirements.txt
	@echo "Pushing to git"
#	git add *.*
#	git commit -m "Update `date +'%Y/%m/%d %H:%M:%S'`"
#	git push

# pull from git
pull:
	@echo "Pulling from git"
	git pull

pop:
	@echo "Populating database..."
	python manage.py populate_db

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Help
help:
	@echo "Available targets:"
	@echo "  run            - Start the Loyalty Application"
	@echo "  push           - Create requirements.txt, Add, commit, and push changes to git"
	@echo "  pull           - Pull changes from git"
	@echo "  migrate        - Apply database migrations"
	@echo "  make		    - Create database migrations"
	@echo "  install        - Install dependencies from requirements.txt"
	@echo "  help           - Show this help message"

