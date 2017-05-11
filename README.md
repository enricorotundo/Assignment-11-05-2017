# Assignment: Single Page TODO App

# Description

Pages are served on [127.0.0.1:8000/](127.0.0.1:8000/).
Both Django and Angular. 
Backend has a couple of APIs available http://localhost:8080.
Angualr tries to call the backend static/app/view1/view1.js but it's not working.


Requirements:

* single-page app
* User login 
* user logout
* Adding todo items
* Editing todo items
* Deleting todo items
* Checking out todo items
* Listing active and done todo items
* Listing supports sorting by due date (ascending/descending)
* A description for the todo
* A due date, where dates are timezone aware
* Python for the backend
* database to store the data
* JS frontend



# Install
    
    git clone https://github.com/tundo91/Assignment-11-05-2017.git
    cd Assignment-11-05-2017
    mkdir venv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

# Run backend

    source venv/bin/activate
    python manage.py runserver 8080

# Install Frontend

[Reference](https://github.com/angular/angular-seed)

    cd static
    sudo npm install -g http-server

# Run frontend
    
    npm start

