Install virtualenv: `pip3 install virtualenv`

To create virtual environment: `virtualenv env`

To activate virtual environment: `source env/bin/activate`

Install Requirements from file: `pip3 install -r path/to/requirements.txt`

Create tables in development database:

1. Start python3 shell :`python3`
2. Import db from app.py: `from app import db`
3. Generate tables: `db.create_all()`

Start RabbitMQ: `rabbitmq-server` or `sudo service rabbitmq-server start`

Start Celery Worker: `celery -A app.celery worker --loglevel=info`

Start Flask App (new shell): `python3 app.py`

Export/Save Requirements: `pip3 freeze > requirements.txt`
