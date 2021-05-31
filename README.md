# my_department_REST
web app (part of final project), REST client for my web service

[![Build Status](https://travis-ci.com/TetianaFirsova/my_department_REST.svg?token=5ZjEYcjLPcSjdBdzxxVo&branch=main)](https://travis-ci.com/TetianaFirsova/my_department_REST)
[![Coverage Status](https://coveralls.io/repos/github/TetianaFirsova/my_department_REST/badge.svg?branch=main)](https://coveralls.io/github/TetianaFirsova/my_department_REST?branch=main)

See application **[specification](/documentation/SPECIFICATION.md)**

The web application is deployed on Heroku with name &quot;imaginary-university&quot; and available at https://imaginary-university.herokuapp.com/


### How to run the project locally:

#### 0. Before you begin:
- Make sure you have **Python3.x** installed on your system.
- Make sure **virtualenv** is installed on your system.

#### 1. Clone the project from Github into new directory:
      $ git clone https://github.com/TetianaFirsova/my_department_REST.git

#### 2. Open up your terminal and CD (change directory) into the app root folder 'my_department_REST'. Create a virtual environment
	> python -m venv env

and activate it

	> env\Scripts\activate (for Windows) 

or

	$ source env/bin/activate (for Linux)

#### 3. Install all dependencies:
From your terminal, make sure you are in the root folder of the project then run the below command:

	> pip install -r requirements.txt

This will download and install all the extensions in [requirements.txt](/requirements.txt)

#### 4. Set configuration and environment variables:
  - set FLASK_CONFIG=development 
  - set FLASK_APP=run (for Windows)

or
  - export FLASK_CONFIG=development (for Linux)
  - export FLASK_APP=run (for Linux)

#### 5. Run the project:
	>  flask run

After running the app you could visit http://127.0.0.1:5000 to see the web app in action.

**Note!**
To work correctly, the web app 'my_department_REST' need running web service 'service'. The web service was launched on heroku. If for some reason it stops working there, you should run it locally and change the corresponding variable in [config.py](/config.py) of web app from

serv_url='http://depemp-service.herokuapp.com'

to

serv_url='http://127.0.0.1:5002'

(see specification for web service)
