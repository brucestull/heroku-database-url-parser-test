# Heroku Parser Test

* <https://flynnt-knapp-parser-test.herokuapp.com/>

## Heroku CLI Fun!!!

1. `heroku login`:

```powershell
(heroku-parser-test) PS C:\Users\FlynntKnapp\Programming\heroku-parser-test> heroku login     
 »   Warning: heroku update available from 7.53.0 to 8.0.4.
heroku: Press any key to open up the browser to login or q to exit: 
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/REDACTED?requestor=REDACTED.REDACTED.REDACTED
Logging in... done
Logged in as FlynntKnapp@email.app
(heroku-parser-test) PS C:\Users\FlynntKnapp\Programming\heroku-parser-test>
```

1. `heroku run python`:

```powershell
(heroku-parser-test) PS C:\Users\FlynntKnapp\Programming\heroku-parser-test> heroku run python
 »   Warning: heroku update available from 7.53.0 to 8.0.4.
Running python on ⬢ flynnt-knapp-parser-test... up, run.7301 (Eco)
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

1. ``:
  
```python
>>> def get_database_config_variables(url):
...     """
...     Parse the Heroku `DATABASE_URL` into a dictionary.
...     """
...     # Remove the `postgres://` from the beginning of the string
...     url = url.split('://')[1]
...     # Split the remaining string into a list on the `@` character, which
...     # separates the database credentials from the host info
...     credentials_and_host_info = url.split('@')
...     # Get the database credentials (`DATABASE_USER` and `DATABASE_PASSWORD`)
...     # from the first item in the `credentials_and_host_info` list
...     credentials = credentials_and_host_info[0].split(':')
...     # Get the database `host_info` from the second item in the
...     # `credentials_and_host_info` list, which is the `DATABASE_HOST`,
...     # `DATABASE_PORT`, and `DATABASE_NAME`
...     host_info = credentials_and_host_info[1].split(':')
...     # Get the database host from the first item in the `host_info` list
...     host = host_info[0]
...     # Get the database port and name from the second item in the
...     # `host_info` list
...     port_and_name = host_info[1].split('/')
...     # Get the database port from the first item in the `port_and_name` list
...     port = port_and_name[0]
...     # Get the database name from the second item in the `port_and_name` list
...     name = port_and_name[1]
...     # Return a dictionary with the database credentials and host info
...     return {
...         'DATABASE_USER': credentials[0],
...         'DATABASE_PASSWORD': credentials[1],
...         'DATABASE_HOST': host,
...         'DATABASE_PORT': port,
...         'DATABASE_NAME': name
...     }
...
>>>
```

1. `get_database_config_variables`:

```python
>>> get_database_config_variables
<function get_database_config_variables at 0x7f57d6ff11b0>
>>>
```

1. `import os`:

```python
>>> import os
>>>
```

1. ``:

```python
database_config_variables = get_database_config_variables(
    os.environ.get('DATABASE_URL')
)
```

1. ``:

```python
>>> database_config_variables
{'DATABASE_USER': 'nvpdfjnaxetqsn', 'DATABASE_PASSWORD': '135a4d0b4ed4d95e06a6fe93b614fab90a61085ae2233c5445a51cc54f324c44', 'DATABASE_HOST': 'ec2-52-54-200-216.compute-1.amazonaws.com', 'DATABASE_PORT': '5432', 'DATABASE_NAME': 'dc5hsr9pso8lvc'}
>>>
```

1. `database_config_variables['DATABASE_NAME']`:

```python
>>> database_config_variables['DATABASE_NAME']
'dc5hsr9pso8lvc'
>>>
```

## Features

* Custom user model.
* Django admin documentation generator.
* Separate DEV and PROD settings.
* Pipfile included.
* Heroku Procfile included.
* [Project Directory Structure](notes/00_directory_structure.md)

## Assumptions

* User has functioning [Python](https://www.python.org/downloads/) 3.11 installation.
* User has functioning [pipenv](https://pypi.org/project/pipenv/) installation.
* User has functioning [git](https://git-scm.com/downloads) installation.
* User is familiar with how to use terminal commands.
* User has [Heroku](https://www.heroku.com/) account.
* User has [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) installed.

## **WARNING:**

* [Deployment checklist - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
  * This template has Django `SECRET_KEY` exposed in both development and production settings files. It is important to create your own separate `SECRET_KEY` for development and production and keep them out of the codebase. This template has `SECRET_KEY` exposed in order to get the user up and running quickly.

## Process

1. [Create Repository from DjangoCustomUserStarter-heroku Template](notes/01_create_repository_from_template.md)
1. [Run Application Locally](notes/02_run_application_locally.md)
1. [Create Heroku Application Server Instance](notes/03_create_heroku_application_server_instance.md)
1. [Provision Database Server Instance](notes/04_provision_database_server_instance.md)
1. [Add DJANGO_SETTINGS_MODULE to Config Vars](notes/05_add_django_settings_module_to_config_vars.md)
1. [Add Django SECRET_KEY to Config Vars](notes/06_add_secret_key_to_config_vars.md)
1. [Add Database Settings to Config Vars](notes/07_add_database_settings_to_config_vars.md)
1. [Modify ALLOWED_HOSTS](notes/08_modify_allowed_hosts.md)
1. [Push to Heroku and Create Superuser](notes/09_push_to_heroku_and_createsuperuser.md)

## Excellent resources, this project wouldn't have been possible without these

* CustomUser method: [Django Best Practices: Custom User Model - Will Vincent - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* Docutils: [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)
* DEV and PROD settings: [Configuring Django Settings for Production - thinkster.io](https://thinkster.io/tutorials/configuring-django-settings-for-production)

## Other Documentation

* [Pipenv & Virtual Environments](https://pipenv-fork.readthedocs.io/en/latest/install.html)

## Links to this project's pages

* [DjangoCustomUserStarter-heroku Repository](https://github.com/brucestull/DjangoCustomUserStarter-heroku)
