# Simple Django application for filling contacts data by uploading excel file
## Getting Started
These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project.
### Prerequisites
What additional tools you need to install and build the app:
* Docker Engine
* Docker Compose
# Rest API for contact and excel file entities
  - Base URL: 127.0.0.1:9090/api/v1
  - Excel file API Methods: GET | POST 
    - [POST] BASE-URL/excel-files - upload excel file , attach file to file form-data key
    - [GET]  BASE-URL/excel-files - get uploaded excel files s3 url's 
  - Contacts API Methods: GET
    - [GET]  BASE-URL/contacts - get list of uploaded contacts ordered by created date

* Simple excel file's inner structure sample
```
Name     |   Phone Number     |     Email Address
--------------------------------------------------
Jack     |   +1877-323-5432   |     jack@mail.com
--------------------------------------------------
Bob      |   +1877-561-3295   |     bob@mail.com
...
...
...
```
* Arrangement of columns in excel file can be arbitrary

## Deployment

Clone or download the project. Go to the backend directory and run the following commands to build and run the app
```
docker-compose pull
docker-compose build
docker-compose up
the application running on 127.0.0.1:9090
```
Application is ready to use.

## Built With
* [Python 3+](https://docs.python.org/3/)
* [Django v3.0.5](https://www.djangoproject.com/)
* [PostgreeSQL](https://www.postgresql.org/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Docker](https://www.docker.com/)

