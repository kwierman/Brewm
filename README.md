# Brewm

## TODO:

    * Add new apps into settings
        * Ingredients
        * Breweries
        * Market information
    * User Account Information
        * Create User accounts and  method for creating/destroying privilages
    * Logging
        * Post to sidebar so users can see new additions to database

## Setup
    Prototyping is done in sqllite. Production will move to postgres.

    Setup the super user

    ~~~ bash
        python manage.py createsuperuser
    ~~~

### Settings

    You can init the default settings with:

    ~~~ bash
        inv defaultsettings
    ~~~
