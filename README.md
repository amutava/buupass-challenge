# buupass-challenge
A challenge for buupass
This is a submission for the challenge presented via BUUPASS

Kindly note that the application is not fully complete but basic functions are working as expected

## What is working

* Register
* Login
*  Get all homes, cars, flights, hotels and experiences
* can search cars , homes, flights, hotels and experiences.

## What is not working:
* Linking up the api with the api for searches and all objects
* Add security features for the api side.


## Why I didn't manage to finish the tasks
 * Given more time theses functionalities could be implemented and also I'll continue working on the application post the submission time.

## How to run the application

* Clone the repository  `git@github.com:amutava/buupass-challenge.git`

* Configure the virtual environment or download a virtual wrapper(makes things easier instead of having envs all over) and configure to an appropriate location in your machine

* In your virtual aenvironment run the command. This will install all the requirements for the application to run locally on your machine

    `pip -r requirements.txt`

* Navigate to the folder `app`

* Finally run the application with the command

    `python manage.py runserver`


## Technologies used
Decided to use python flask framework. Although I have worked with django for the better part of coding with python I decided to use flask  because of the abstracted nature of django.


## API Endpoints
| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `/api/v1/resources/experiences` | `GET` | search an experiences|
| `/api/v1/resources/flights | `GET` | search  a flights|
| `/api/v1/resources/cars | `GET` | search  a car|
| `/api/v1/resources/homes | `GET` | search a home|
| `/api/v1/resources/hotels | `GET` | search a hotels|
| `/api/v1/resources/experiences/all` | `GET` | Get all experiences|
| `/api/v1/resources/flights/all | `GET` | Get all flights|
| `/api/v1/resources/cars/all | `GET` | Get all cars|
| `/api/v1/resources/homes/all | `GET` | Get all homes|
| `/api/v1/resources/hotels/all | `GET` | Get all hotels|


Kindly note that these two endpoints are implemented as a web page...I'll be intergrating everything as a web page.

| `/auth/register` | `POST`  | Register a new user|
|  `/auth/login` | `POST` | Login |



## Some screen shots from testing the application.



