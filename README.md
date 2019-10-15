## INSTAGRAM-REPLICA

## Description
    This is a clone of instagram web app made out of django a python framework. Users can register, then sign in in order to make posts.

## Setup
    git clone https://github.com/LeoAmby/Instagram-Replica.git

    After cloning, you'll need the following to be able to work around the project:
        * python3.6 installed
        *Create a virtual environment
            python3 -m venv virtual
        *Activate the virtual environment
            source virtual/bin/activate

        *Install django
            pip install d==1.11.23
        *Install all django dependencies
            pip install -r requirements.txt
        *Create a django App.the project is already created for you.
            django-admin startapp <nameOfYourApp>

## Environment Requirements
    * SECRET_KEY= added by default
    * DEBUG= set to false in production
    * DB_USER= database user of choice
    * DB_PASSWORD= database of choice
    * DB_HOST="127.0.0.1" on local
    * MODE= dev or prod , set to prod during production
    *ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'

## Technologies Used
    * Django == 2.0
    * HTML5
    * Bootstrap 3
    * Github for task management
    * Heroku for Deployment

## License
[MIT](https://github.com/LeoAmby/Instagram-Replica/blob/master/LICENSE)