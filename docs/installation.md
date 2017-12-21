**Installation:**

pip install -r requirements.txt

create a .env file in funx_test/.env in the same place that settings.py

copy the data from .envexample to .env and change the credentials acording to the credentials created by you

run:

python manage.py migrate

python manage.py runserver




**Testing:**

If you want to run tests, you must to create a database for tests and run command:


python manage.py test