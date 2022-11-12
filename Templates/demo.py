# Templates and Django Template Language
# Custom Filters
# Custom Tags
# Template Inheritance
# Static Files

### 1///
    # M - Model(Database) , T - Template(Presentation) , V - View = Business logic (Program logic)
    # It is a text document(usually a html) in which you use the Django template language
    # Django defines a standard API for loading and rendering templates:
        # Loading consists of finding the template and preprocessing it
        # Rendering means interpolating the template with context and returning the resulting data
        # Server - side rendering(SSR) / Client - side rendering (React,Angular,Vue...)
### Django Template Language DTL
    # It is Django's own template system
    # Use to express presentation, not program logic
    # The syntax involves four constructs
        # Variables
        # Filters
        # Tags
        # Comments
    # DTL Variables
        # Outputs a value from the view context(dict-like object)
        # Variables are surrounded by {{ and }}
        # The name of a variable:
            # cannot have spaces or punctuation
            # may not have a DOT in it
            # may not be number
            # may not start with underscore(_)
        # how we use functions in the HTML template
    # DTL Filters
        # Modifies variables for display
            # Use a pipe '|' - to apply a  filter to a variable = {{title|upper}}
            # There are more than 60 filters
            # Filters can be 'chained'
                # The output of one filter is applied to the next
            # Some filters take arguments
                # Use colon ':' to mark arguments
        # Commonly Used Filters
            # {{value|truncatechars:N}} = Display the first N chars of a string
            # {{value|tuncatewords:N}} = Display the first N words of a string
            # {{list|join:","}} = Join list elements
            # {{my_date|date:"Y-M-D"}} = Format a date according to the given format
    # DTL Tags
        # A template tag is a function which returns a value to be displayed
        # Provide custom logic in the rendering process
        # Surrounded by {% ... %}


        # if Tag
            # Evaluates a variable,and if that variable is 'True'(exists,not empty or not false)
            # Requires beginning and ending tags
            #{%if ....%} , always ends with {%endif%}
        # ifchanged Tag
            # Checks if a value has changed from the last iteration of a loop
            # it is used within the loop
                # {% for employee in employees_list%}
                    # {% ifchanged %}{{ employee.name}} {%endifchanged%}
                #{% endfor %}
        # Url tag
            # used for redirection to other pages
            # commonly used
        # Csrf_token Tag
            # Cross site Request Forgery protection
            # Used inside the <form> element
        # Comments
            # Comments are surrounded by {# and #}
            # a multi line comment can be written using a {% comment %} tag
# Custom Filters ////
    # Create templatestags Folder
        # In your application create a templatestag module with you custom filter file
        # the custom filter is created with python code
        # check more at filters.py
# Custom Tags ////
    # {% my_tag %}
    # Template Tags Helper Functions
        # Django provides us with helper functions that allow us to create custom template tags
            # simple_tag
                # Processes the data and returns a string
            # inclusion_tag
                # Processes the data and returns a rendered template
    # Creating Custom Template Tags
        #   simple_tag returns string
            # more at templatetags/tags.py
        # inclusion_tag shows mini reusable view

###3////
    # Template Inheritance
        # Template inheritance allows us to build a base skeleton template
        # the base template contains all the common elements and defines blocks that child templates can override
        # Typically , the header and the footer remain the same in the whole app
        # Using template inheritance , we can reuse the common parts of our app
