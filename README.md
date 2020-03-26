To install application please make following steps:

Clone a project to your machine and go inside directory.

**Create virtualenv**

`python3 -m venv venv`

**Activate it**

`source venv/bin/activate`

**Install requirements**

`pip install -r requirements.txt`

**Initialize database and migrations**

`flask db init
 flask db migrate 
 flask db upgrade`

**To run an application**

`python app.py`

**To run unittests**

`python -m unittest tests/test*.py`