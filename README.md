# 904Labs-Assignment

Requirements:

* single-page
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

    mkdir venv
    pip install -r requirements.txt

# Run backend

    source venv/bin/activate
    python manage.py runserver 8080

# Install Frontend

https://github.com/angular/angular-seed

    cd static
    sudo npm install -g http-server
    http-server -a localhost -p 8001

# Run frontend
    
    npm start
