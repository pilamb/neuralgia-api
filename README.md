Python3.7
---------
Prepared for a "db.sqlite3" database.

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

curl -H 'Accept: application/json; indent=4' -u superusername:superuserpasss http://127.0.0.1:8000/users/

(httpie needed)

http://127.0.0.1:8000/hits/
http://127.0.0.1:8000/hit/1

http http://127.0.0.1:8000/hits/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/hits/ Accept:text/html         # Request HTML

Or by appending a format suffix:

http http://127.0.0.1:8000/hits.json  # JSON
http http://127.0.0.1:8000/hits.api   # Browsable API suffix

http --json POST http://127.0.0.1:8000/hits/ note="example"
http --json POST http://127.0.0.1:8000/hits/ note="example" area="VR1"