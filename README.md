# Single Page TODOs List

This app is deployed on [https://agile-thicket-76618.herokuapp.com/static/app/index.html#/](https://agile-thicket-76618.herokuapp.com/static/app/index.html#/) (be patient, loading might take a while).

API is on [https://agile-thicket-76618.herokuapp.com/](https://agile-thicket-76618.herokuapp.com/)

## Description

 
![Image of Yaktocat](items_list.png)

## Requirements:

- [x] Python backend (Django + RESTframework)
- [x] single-page JS frontend (AngularJS)
- [x] Database to store the data (SQLite)
- [ ] User login 
- [ ] User logout
- [x] Listing active/done TODO items
- [x] Adding TODO items
- [x] Editing TODO items
- [x] Deleting TODO items
- [x] Checking out TODO items (flagging an item as done?)
- [ ] TODO listing supports sorting by due date (ascending/descending)
- [x] a TODO has a description
- [x] a TODO has a due date, where dates are timezone aware


## Local install
    
    git clone https://github.com/tundo91/Assignment-11-05-2017.git
    cd Assignment-11-05-2017
    mkdir venv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run server

    source venv/bin/activate
    python manage.py runserver 8000


