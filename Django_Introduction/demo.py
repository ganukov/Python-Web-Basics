# 1.What is Django?

# 2.Creating a Django Project

# 3.Creating a Django App

# 4.Setting up a Database

# 5.Writing a Simple Task APP

# 6.Django Admin

# 7.Creating a Simple Design

# 1/// What is a Framework?
    # Platform for developing software apps
    # Provides a foundation on which software developers can build programs for a specific platform
    # A framework includes an API
    # May include code libraries,a complier,and other progmrams used in the software development process

# 1.1/// What is Django?
    # High lever python web framework
    # Ridiculously fast
    # Reassuringly secure
    # Exceedingly scalable
    # Free and Open source

    # Model - View - *(MV*):
        # - Model contains the data (Database)
        # - View handles the UI
        # - *:
            # = Handles business logic
            # - Gets/sets data into 'Model'
            # - Returns data to 'View'
    # Django uses MTV
    # What is MTV?
        # - Model Template View
        #   'Model', 'View', '*'
        # Model - manages the data and is represented by a database
        # Template - the presentation (front-end) layer
        # View - receives HTTP requests and sends HTTP responses

# 2//// Creating Django Project
    # __init__.py = Shows that the directory is a Python package
    # setting.py = The configuration file for the Django Project
    # urls.py = Table of content
    # manage.py = Tool for executing commands
        # the runserver command starts the development server on the internal IP at port 8000 by default
        # this server is intended only for use WHILE DEVELOPING

# 3/// Creating a Django APP
    # APP vs PROJECT
        # Django APP:
            # a Web application that does something - e.g., a wide web blog system or a small task app
            # an app can be IN MULTIPLE PROJECTS
        # Django Project:
            # a collection of configuration and apps for a particular website
            # a project can CONTAIN MULTIPLE APPS
        # Most of the thing in Django are created in the TERMINAL, like the APPS for example

        # python manage.py startapp ''''name''''
    # Directory Structure for each Django APP
        # admin.py = admin page
        # models.py = models of the app
        # views.py = views of the app
        # migrations = command line utility for propagating changes in models

# 4//// Setting up a Database
    # Psycopg2
        # PostgreSQL database adapter for the Python programming language
    # Use the Psycopg2 module to:
        # Connect to PostgreSQL
        # Perform SQL queries and database operations
    # It is an external module

    # Django Model
        # Models store your application`s data
            # The essential fields and behaviours of the stored data
        # Generally, each model maps to a SINGLE DATABASE TABLE
        # Each model is a Python class that subclasses django.db.models.Model
        # Each attribute of the model represents a database field
        # Use models to create a database schema for the app
        # Use migrations to upgrade your database live
            # first,create migrations for the added model
                # 'python manage.py makemigrations'
            # next apply those changes to the database
                # 'python manage.py migrate'
    # Django Admin Site
        # It is an automatic admin interface
            # There trusted users can manage content on the site
        # One of the most powerful parts of Django
        # if u want to use the Django admin u have to create a SUPERUSER with password
        # access it with /admin
        # we always have to add the models in the admin panel of the app
    # Django Views
        # The views.py file contains view functions/classes
        # Each view takes a Web request and returns a Web response
        # Implements the main logic that needs to happen when a given URL is reached
        # The names of the functions are usually related to the URL that is being reached
        # Function based views
        # Class based views

# 7/// Creating a simple Design
    #  What is a Template?
        # Being a web framework,Django needs a convenient way to generate HTML dynamically
        # The most common approach relies on templates
        # A template contains:
            # The static parts of the desired HTML output
            # A special syntax describing how dynamic content will be inserted
        # Adding Context
            # The render function can receive a context
                # It is a dictionary passed to the template and used to display data dynamically