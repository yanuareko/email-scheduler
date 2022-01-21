# email-scheduler

### How to run backend app:
1. make sure using python 3.7+ (I used 3.7.12)
2. create database named `email_scheduler`
3. `pip install -r requirement.txt`
4. `python init.py` running at least once to register the extensions,
and create the tables
5. `flask db init`
6. `flask db migrate`
7. `flask db stamp head`
8. `flask db upgrade`
9. make edit in file `config.yml` (set **testing** to False for sending email)
10. make sure to put file `config.yml` beside file `app.py`
11. run with: `python app.py`

### How to run celery worker
`celery -A app.celery worker --loglevel=info -E`

### Running test
`python -m pytest tests/`