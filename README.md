What is this for
----------------

:hospital:

This software aims to help with [**trigeminal neuralgia disorder**](https://www.ninds.nih.gov/Disorders/Patient-Caregiver-Education/Fact-Sheets/Trigeminal-Neuralgia-Fact-Sheet) but it can be extended to other persistent pain neuropathies.

Every time a neuralgia patient has pain it can be registered via app with parameters such as date and time, how painful it was in a rank of 1 to 10, if meds have been taken or not and the area.
Notes can also be added to complement the context: "I took the meds 2 hours ago", "while eating", "while using floss".

Patients can show their specialist doctor the data gathered, study the impact of external factors, see timelines, etc.

With all this inside a database students, Doctors, investigators and so can use it in many ways. Who knows, maybe patters are discovered using big data and this terrible sickness is finally beaten up.

### Made with

:snake:

Python3.7, Django 2.1 and DjangoREST 3.9.1

Prepared for a "db.sqlite3" database.

### Quick install

Make a virtualenv or a docker and then in the command line:

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser   and set a user/password
    python manage.py runserver

#### Usage

The project *won't run* if SECRET_KEY is not set to a value in the settings.py file.
You can set it to a random value.

Users need to be registered, for now, as superusers.

In the settings set the secret_key value to something or Django won't run.

Visit the home url with a browser or try this on a command shell:

    curl -H 'Accept: application/json; indent=4' -u superusername:superuserpasss http://127.0.0.1:8000/users/

Some requests made with httpie:


    http://127.0.0.1:8000/hits/   And see all
    http://127.0.0.1:8000/hit/1   Or see a detail


`http http://127.0.0.1:8000/hits/ Accept:application/json`  # Request JSON

`http http://127.0.0.1:8000/hits/ Accept:text/html`         # Request HTML

Or by appending a format suffix:

`http http://127.0.0.1:8000/hits.json`  # JSON

`http http://127.0.0.1:8000/hits.api`   # Browsable API suffix

`http --json POST http://127.0.0.1:8000/hits/` note="example"

`http --json POST http://127.0.0.1:8000/hits/` note="example" area="VR1"

Type `httpie -v` for more help.

An example of a response in JSON format:

    {
        "model": "data_api.hit",
        "pk": 1,
        "fields": {
            "created": "2019-02-26T18:23:19.516Z",
            "triggered_by": "eating",
            "area": "VL3",
            "note": "note1",
            "rank": 5,
            "meds": true,
            "owner": 1
        }
    }

#### Tests

Can be found at data/api/tests.

Run them with `coverage run --source="./data_api" manage.py test data_api && coverage report`

#### ToDos:

0. Users separated app
1. A front client, desirable Vue.js
2. A mobile client, flutter?
3. Graphs, maybe 3DS or HighCharts. Timelines are interesting


After:

- Improve the areas where pain can hit. See data_api/models
- Deploy on gCloud
- Features welcome