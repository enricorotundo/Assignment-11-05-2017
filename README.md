# Assignment: Single Page TODO App

# Description

Pages are served on [127.0.0.1:8000/](127.0.0.1:8000/). 


Requirements:

- [ ] User login 
- [ ] User logout
- [ ] Adding todo items
- [ ] Editing todo items
- [ ] Deleting todo items
- [ ] Checking out todo items
- [ ] Listing active/done TODO items
- [ ] Listing supports sorting by due date (ascending/descending)
- [ ] TODO has a description
- [ ] TODO has a due date, where dates are timezone aware
- [x] Database to store the data (SQLite)
- [x] Python backend (Django+RESTframework)
- [ ] JS frontend (AngularJS)
- [ ] single-page app



# Install
    
    git clone https://github.com/tundo91/Assignment-11-05-2017.git
    cd Assignment-11-05-2017
    mkdir venv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

# Run server

    source venv/bin/activate
    python manage.py runserver 8000


