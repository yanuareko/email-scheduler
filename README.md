# email-scheduler

### How to run:
1. make sure using python 3.7+ (I used 3.7.12)
2. create database named `email_scheduler`
3. `pip install -r requirement.txt`
4. `python init.py` running at least once to register the extensions,
and create the tables
5. `flask db init`
6. `flask db migrate`
7. `flask db stamp head`
8. `flask db upgrade`
9. 