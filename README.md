# Assignment: Single Page TODOs List

## Description

Pages are served on [127.0.0.1:8000/](127.0.0.1:8000/). 


## Requirements:

- [ ] User login 
- [ ] User logout
- [ ] Listing active/done TODO items
- [ ] Adding TODO items
- [ ] Editing TODO items
- [ ] Deleting TODO items
- [ ] Checking out TODO items
- [ ] TODO listing supports sorting by due date (ascending/descending)
- [ ] TODO has a description
- [ ] TODO has a due date, where dates are timezone aware
- [x] Database to store the data (SQLite)
- [x] Python backend (Django+RESTframework)
- [x] JS frontend (AngularJS)
- [x] single-page app


## Install
    
    git clone https://github.com/tundo91/Assignment-11-05-2017.git
    cd Assignment-11-05-2017
    mkdir venv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run server

    source venv/bin/activate
    python manage.py runserver 8000


