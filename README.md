# Twillio-Api

A Python 3 api that uses the Twillio API to send texts

## Initial checkout and setup of codebase

* Open up a terminal window and `cd` into a directory that you wish to run this application in
* Run ``git clone git@github.com:rachhtordoff/Twillio-Api.git``
* Run ``cd Twillio-Api``

### Set up

An example usage using docker-compose.yaml

* ``
twillio_api:
  build: twillio_api
  ports:
    - <chosen ports here>
  volumes:
    - twillio_api:/opt
  environment:
    - FLASK_APP=manage.py
    - APP_NAME=text-message-api
    - FLASK_LOG_LEVEL=DEBUG
    - PYTHONPATH=/opt
    - SECRET_KEY=you-will-never-guess
    - TEXT_ACCOUNT=<twillio account secret key>
    - TEXT_TOKEN=<twillio token>
    - NUMBER_FROM=<twillio mobile number chosen to send texts from>
    - NUMBER_TO=<the number you wish to send texts to, this can be replaced by data passed over if you wish to use this dynamically>
``

* ``docker-compose up --build -d twillio_api`` - Runs the container

## Usage

Example Python request to send a text message:

``requests.post(<twillio_api_url>+'/send-text')``

Example with using the 'number to' dynamically, as a json header

``headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(config.TEXT_API_URL+ '/send-priority-1', data=json.dumps(params), headers=headers)``

## Authors

* Rachael Tordoff - Opti-doc, Racjac Solutions
