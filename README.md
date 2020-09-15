# Backend
This is the django backend portion on tap-dating platform.

## /api
The API portion of the backend is using a Django stack with Graphene as a GraphQL server to handle API request.
The full list of dedependencies are found in the file `requirements.txt` but are listed here with links for further reading.

- [Django == 3.1](https://www.djangoproject.com/download/)
- [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/installation/)
- [django-graphql-auth](https://github.com/PedroBern/django-graphql-auth)
- [django-graphql-jwt](https://github.com/flavors/django-graphql-jwt)
- [django-filter](https://github.com/carltongibson/django-filter)
- [psycopg2](https://www.psycopg.org/install/)


<hr />

## Getting Started
In order to develop for tap-dating's backend you'll need MacOS, Linux flavor of choice, or Windows 10 Professional (to run WSL2+ and have a Linux flavor of choice and Windows Terminal installed).


### 1. Setup gcloud SDK
If you do not already have Google Cloud SDK installed then follow the [instructions outlined here](https://www.codingforentrepreneurs.com/blog/google-cloud-cli-and-sdk-setup)

Once completed setup your `gcloud` to point to our project via this command:

`gcloud config set project tap-dating-app`


### 2. Setup Docker Desktop
If you do not have Docker Desktop already installed then you need to visit: https://hub.docker.com, sign-up for an account and follow the instructions specific to your OS. For windows 10 users, you must be running Windows 10 Professional in order to use Docker.

### 3. Setup SQL Proxy
If you do not already have Google Cloud SQL Proxy installed then follow the instructions here:

https://cloud.google.com/sql/docs/postgres/sql-proxy

Don't forget to make the file executable and/or on your PATH. I installed mine in `~/.local/bin` for example.

### 4. Setup Python
If you do not have `python3` and `pipenv` setup then install the latest Python runtime for your machine by visiting https://www.python.org/downloads/

Once this is installed then install `pipenv` for your OS by visiting https://pipenv.pypa.io/en/latest/install/#installing-pipenv


### 5. Setup PostgreSQL 12 & User
If you do not have PostgreSQL server running on your local machine, then follow the installation instructions for your OS from here:

https://www.postgresql.org/download/

Be sure to setup your local PostgreSQL 12 server user(s) to manage databasses (create, etc).

For local development the following user needs to be setup. In `psql` the command is:

`CREATE USER tap-dating WITH PASSWORD 'tap-dating' CREATEDB;`

This will allow the tap-dating user to create database should it be needed as well as to be able to create the test database, which by default Django will drop after tests are ran.

You'll also want to create the `tap-dating_dev` database and grant permissions on it:

`CREATE DATABASE tap-dating_dev;`
`GRANT ALL PRIVILEGES ON DATABASE tap-dating_dev TO tap-dating;`

You might also want to create a user on your system to be able to log into `psql`:

`sudo adduser tap-dating`, set password to `tap-dating` and follow the rest of the propmts for your OS

To use that user to log into `psql` run: `su - tap-dating` then enter the password. Then run `psql -d tap-dating_dev` to connect to the DB.


### 5. Clone this repo 
Clone the repo by running:
`git clone git@github.com:tap-dating-Events-Engineering/backend.git`

From your terminal or use GitHub Desktop to pull the repository to your local machine. I *HIGHLY* recommend setting up a `Projects/tap-dating` folder in your `~/` so you do not need to modify the `./scripts/build.sh` file to point to where you clode the repo to.

`cd` to the repository folder and run `pip install` to download all the requirements for the project.

If you run into issues with installing `psycopg2` then make sure you have the required build tools installed. You can also view this [GitHub Issue](https://github.com/psycopg/psycopg2/issues/684). Namely you need to make sure your OS has `postgresql-dev gcc python3-dev` installed, and if you see issues on Docker Builds then Alpin requires this `musl-dev` as well.


### 6. Make `/scripts/` files executable
You may need to make the script files located within the `/scripts` folder executable with `chmod +x <file>`