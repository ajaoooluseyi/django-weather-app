# django-weather-app


## Description
It is a weather forecast app API built on Django. It takes latitude and longitude and returns weather forecast of the location
on either of this three categories:

* Minute forecast for 1 hour
* Hourly forecast for 48 hours
* Daily forecast for 7 days

### Dependencies

* Django
* Python version 3.10.6
* Openweathermap


### Executing program

On the terminal execute the below command to create the projects' working directory and move into that directory.

 
```python
$ mkdir app
cd app
```

In the projects' working directory execute the below command to create a virtual environment for our project. Virtual environments make it easier to manage packages for various projects separately.

 
```python
$ py -m venv venv
```

To activate the virtual environment, execute the below command.

```python
$ source venv/Scripts/activate
```
Clone this repository in the projects' working directory by executing the command below.

```python
$ git clone https://github.com/ajaoooluseyi/django-weather-app.git
$ cd django-weather-app

```

To install all the required dependencies execute the below command.

```python
$ pip install -r requirements.txt
```

To run the app, navigate to the app folder in your virtual environment and execute the command below
```python
$ python manage.py migrate

$ python manage.py runserver
```
