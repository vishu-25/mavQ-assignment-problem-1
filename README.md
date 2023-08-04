# MavQ internship assignment problem 1

## Objective
Create a JSON API Server that will receive GET and POST requests from any external client.
The API server will connect with any SQL database (of your choice) and the server will be able
to write the data received from APIs to the server and return the result based on the query. The
read query will be able to support filters as well as defined by the data model. The entire stack
(API Server & database) should be containerized in a docker container and the ecosystem
should be able to run with a simple docker-compose up command.

Specification 

Data Model 

1. Teacher <br>
        a. teacher_id  <br>
        b. name <br>
        c. is_active <br> 
        d. designation <br>


2. Course <br>
        a. course_id <br> 
        b. course_mentor <br>
        c. name <br>
        d. start_date <br> 
        e. end_date <br>
        f. description <br>
        
#

## Dependencies
- [Python (version 3.7 or above)](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)
- [Postman](https://www.postman.com/)
- [SQLite3](https://www.sqlite.org/index.html)
  
### To run the application locally using Docker, follow these steps (compatible with Linux and macOS):

```
git clone https://github.com/vishu-25/mavQ-assignment-problem-1.git
cd mavQ-assignment-problem-1/src/
chmod +x setup.sh 
./setup.sh
```

#

### To execute the code directly using Python, follow these steps:

```
git clone https://github.com/vishu-25/mavQ-assignment-problem-1.git
cd mavQ-assignment-problem-1/src/
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8080
```

