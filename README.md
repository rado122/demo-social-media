# demo-social-media

## Prerequisites
- Ubuntu server (*app was tested using 18.04, other versions could work as well*)
- Python 3.6 (*other versions compatibility is not guaranteed*)
- (*optional*) [virtualenv](https://virtualenv.pypa.io/en/stable/installation/ )  

## Instalation
1. Clone the repo sowhere and `cd` into it.
2. Run `pip install -r requirements.txt` to install dependencies.
4. Cd into `/socialmedia` folder
5. Run `manage.py migrate` to migrate DB schema
6. Run `manage.py createsuperuser` and follow instructions to create an admin user
7. Run `manage.py runserver`

Auto-generated api documentation is available at `/docs`

## Authentication
The API uses JWT tokens for authentication

Steps to authenticate:
  1. Send `POST` request to `/api/login` with json payload having username and password in it
  ```json
  {
      "username": "username",
      "password": "password"
  }
  ```
  
  2. If username and password are correct the API will answer with response JSON containing  `token` property
  ```json
  {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOjMsImlhdCI6MTUzNjU4MzkxOSwiZXh",
  }
  ```
  
  3. In your requests, specify the access token in an Authorization header as follows
  ```authorization: Bearer {token}```


## TODO
- create demo bot
- use clearbit.com/enrichment for getting additional data for the user on signup
- Create tests
- Add docstrings to undocumented parts of the code
- Add User endpoints
- Handle validator out of requests edgecase in email validator
- Improve API Docs
- Change API urls to paths.