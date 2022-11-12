##### Models in Django PART 1 ####

# 1/ Understanding Models
    # Models
    # Fields
    # Field Types
# 2/ Models Migration
# 3/ Model Field Options
# 4/ Relationships in Django Models
# 5/ Django Admin Site

#### 1 ###
    # MODELS PURPOSE IS TO KEEP DATA !!!
    # Models Benefits
        # Work with database data using Python code
        # Dont have to write low level SQL queries
        # Focus on the data and the business logic
        # Django automatically creates the needed queries and executes them
        # Django ORM creates SQL through Python Code

    # class Employee(models.Models)
        # first_name = models.CharField(max_lenght = 30)
        # last_name = models.CharField(max_lenght = 40)
        # It will create a database table !!!
    # Fields
        # Field = variable
        # The most important and only required part of a model
            # Field name should not conflict with reserved words
            # Fiend name cannot have MORE THAN ONE UNDESCORE in a row and cannot END WITH AN UNDERSCORE
        # Each field is an instance of an appropriate FIELD CLASS
    # Field Types
        # They determine the column type in a database table ( INTEGER,VARCHAR,TEXT)
        # Django has dozens of built in field types
        # Technically , they are defined in django.db.models.fields
        # For convinience they're imported django.db import models

        # String Field Types
            # CharField
            # Appropriate for small to large sized strings
            # Has one required argument - max_length

        # TextField
            # Appropriate for large texts
            # When specifying max length,it wont be enforced at the model or database level

        # IntegerField
            # Stores integers
        # PositiveIntegerField
            # Stores integers that could be either positive or zero
        # FloatField
        # DecimalField
        # DataField = stores a date
        # TimeField = stores a time
        # DateTimeField = stores a date and a time
        # URLField
        # EmailField

### 2/ MODELS MIGRATION
    # The python code we write connect to the database through Migrations
    # Use to add changes made to the models into the database
    # Django creates migrations FOR YOU
        # Just write the appropriate terminal commands (migrations,make migrations)
    # You can use many database systems with Django
        # However, PostgreSQL is the most capable of all in terms of schema support
    # Migrations commands
        # Creating new migrations
            # Package up the changes into migration files
            # python manage.py makemigrations
            # Every time we have a change on the struction on our MODELS we have to make migrations
        # Applying the created migrations to the database
            # Use after the migration files are created
            # python manage.py migrate
        # Reversing Migrations
            # to reverse concrete migration
                # python manage.py migrate employees 002
            # to reverse all migrations
                # pyton manage.py migrate employees zero
            # SOME MIGRATIONS ARE IRREVERSABLE !!!

### 3/ Model Field Options
    # Field Options
        # Common SQL constraints written with python code
        # Available to all field types
        # All of them are optional
            # unique
                # False by default
                # If True,this field must be unique through the table
                # email_address = models.EmailField(unique=True)
            # default
                # a default value or a default callable object for the field
            # null = database-related
                # False by default.If True, empty values will be stored as NULL
                # Use for non-string fields such as integers,Booleans and dates
            # blank validations related
                # Flase by default.If True,the field is allowed to be blank
        # Primary_key
            # If True, the field becomes the primary key for the model
            # Used to override,

        # choices
            # choices = (
                # 'jr','January'
                # 'fbr','February')
        # verbose_name = 'Seniority level'
        # editable
            # True by default

### Relations
    # ONE TO MANY
    # On delete options MUST HAVE on foreign key
        # on_delete=CASCADE
        # on_delete=SET_NULL works only if null=True always together
        # on_delete=models.RESTRICT u cant delete if there is data in it
    # MANY TO MANY
        # Django auto creates an intermediary join table
        # to manually specify the table use the THROUGH option
            # It creates a Django intermediary model that represents it
        # MOST USED WHEN ASSOCIATING EXTRA DATA WITH A MANY TO MANY RELATION
    # ONE TO ONE
        # requires two positiona arguments
            # the CLASS to which the model is related
            # on_delete option
    # Lazy relations
        # when resolving circular dependencies between two models
            # 1 employee / colleagues

#### 5/ Custom Django Admin Site
    #  Use the ModelAdmin class
        # It represents the model in the admin site
        # make layout changes on 'add' and 'change' pages
            # class EmployeeAdmin(admin.ModelAdmin)
                # field = [('first_name','last_name'),'email_address']
        # fieldsets
            #