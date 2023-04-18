# Heroku Parser Test

* <https://flynnt-knapp-parser-test.herokuapp.com/>
* <https://github.com/brucestull/heroku-parser-test>
* Source code for the URL Parser
    * <https://github.com/brucestull/django-heroku-database-url-parser>

## Heroku CLI Fun

1. Log in to Heroku CLI
    * `heroku login`:

        ```powershell
        (heroku-parser-test) PS C:\Users\FlynntKnapp\Programming\heroku-parser-test> heroku login     
        »   Warning: heroku update available from 7.53.0 to 8.0.4.
        heroku: Press any key to open up the browser to login or q to exit: 
        Opening browser to https://cli-auth.heroku.com/auth/cli/browser/REDACTED?requestor=REDACTED.REDACTED.REDACTED
        Logging in... done
        Logged in as FlynntKnapp@email.app
        (heroku-parser-test) PS C:\Users\FlynntKnapp\Programming\heroku-parser-test>
        ```

1. Start a Python shell on the remote server
    * `heroku run python`:

        ```powershell
        (heroku-parser-test) PS C:\Users\FlynntKnapp\Programming\heroku-parser-test> heroku run python
        »   Warning: heroku update available from 7.53.0 to 8.0.4.
        Running python on ⬢ flynnt-knapp-parser-test... up, run.7301 (Eco)
        Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
        ```

1. Define the function `get_database_config_variables`:
  
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

1. Check that the `get_database_config_variables` function object exists
    * `get_database_config_variables`:

        ```python
        >>> get_database_config_variables
        <function get_database_config_variables at 0x7f57d6ff11b0>
        >>>
        ```

1. Import the `os` module so we can access environment variables
    * `import os`:

        ```python
        >>> import os
        >>>
        ```

1. Call the `get_database_config_variables` function with an argument of
the `DATABASE_URL` environment variable provided by Heroku and assign it to the variable
`database_config_variables`:

    ```python
    database_config_variables = get_database_config_variables(
        os.environ.get('DATABASE_URL')
    )
    ```

1. Inspect the `database_config_variables` dictionary:
    * NOTES:
        * These values are different for each Heroku app.
        * These values shown are for a Heroku app that has been deleted.
        They are only shown here for illustrative purposes.
        * True values of a current application are not shown here since we don't want to provide these to the public. We don't want the public to be able to access our database directly.

    ```python
    >>> database_config_variables
    {'DATABASE_USER': 'nvpdfjnaxetqsn', 'DATABASE_PASSWORD': '135a4d0b4ed4d95e06a6fe93b614fab90a61085ae2233c5445a51cc54f324c44', 'DATABASE_HOST': 'ec2-52-54-200-216.compute-1.amazonaws.com', 'DATABASE_PORT': '5432', 'DATABASE_NAME': 'dc5hsr9pso8lvc'}
    >>>
    ```

    * More readable form:

        ```python
        database_config_variables
        {
            'DATABASE_USER': 'nvpdfjnaxetqsn',
            'DATABASE_PASSWORD': '135a4d0b4ed4d95e06a6fe93b614fab90a61085ae2233c5445a51cc54f324c44',
            'DATABASE_HOST': 'ec2-52-54-200-216.compute-1.amazonaws.com',
            'DATABASE_PORT': '5432',
            'DATABASE_NAME': 'dc5hsr9pso8lvc'
        }
        ```

1. We now have the database credentials and host info in a dictionary, so we can use them to connect to the database.
