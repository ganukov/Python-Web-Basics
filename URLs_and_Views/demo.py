# 1.Creating a New Project
# 2.Urls in Django
# 3.Function-Based Views
# 4.Views Returning Errors


# 2///
    # When an URL is entered by a user,it ensures that a certain result is achieved
    # e.g. softuni.bg = home page of softuni
    # How it happens:
        # Django looks for the URLPATTERNS variable in the urls.py file
        # Runs through each URL pattern and stops at the FIRST MATCHING PATTERNS
        # Calls the given VIEW and passes an instance of the class HttpRequest
        # URLs in Django can be dynamic
            # e.g., path('department/1/', views.show_department_with_id_one)
        # Set one dynamic URL pattern for all departments.
            # path('department/<department_name>/', views.show_department_by_name).
            # optionally, can include CONVERTER TYPE(otherwise,it is CONVERTED TO A STRING)
                # path('department/<int:department_name>/', views.show_department_by_name).
            # The value name is passed as an argument to the view
                # def show_department_by_id(request,department_id):
                    # pass
        # Default Path Converters
            # str - matches any non-empty string ,excluding '/'
            # int - matches zero or any positive integer
            # slut - matches any slug string consisting of ASCII letters,numbers,hyphens and underscores
            # path - matches any non-empty string,including '/'
                # Allows you to match a complete URL path
            # uuid - matches a formatted UUID
        # RegEx in URLs
         # Use re_path() instead of path()
         # Makes the matching limited
         # Each captured argument is sent to the view as a string
         # Using unnamed RegEx groups isn't recommended
            # When both styles are mixed,any unnamed groups are ignored and only groups are passed to the view functuion

        # Including URL models
            # at any point you can include urls.py modules with include()
            # it chops off the part of the matched URL('department/') and sends the remaining with the included urls.py
            # for further process
        # Including URL patterns List
            # include([....])
            # It removes redundancy from Urls where a single pattern prefix is used repeatedly

# 3/// Function Based Views
    # Views in Django
        # The view holds the concrete logic to achieve the expected result when a certain URL is entered
        # returns instance of HttpResponse
        # Each view receives
            # HttpRequest object as its FIRST argument(typically named request)
            # *args - matches from no named groups in the URL pattern
            # **kwargs - matches from named parts in the URL pattern
        # Each view returns
            # HttpResponse object
    # Django Shortcut Functions
        # Django shortcut functions are helper functions
        # They make developing with Django easier
        # Connects many different levels of the Model-View_Template paradigm
        # render()
            # Combines a template with a context dictionary
            # Returns an HttpResponse object with the rendered text
            # Required arguments
                # request - generating this response
                # template_name - a full name of a template to use
                # context - optional argument(empty dictionary by default)
                    # A dictionary of value to add to the template context

        # redirect()
            # Use it to redirect the user to the appropriate URL
            # By passing a hardcoded URL to redirect to
                # redirect(some_view_name,*args,**kwargs)
            # By passing the name of a view and optionally some positional or keyword arguments
                # redirect('/some/url/')
            # It returns an HTTP status code 302
        # get_object_or_404()
        # get_list_or_404()

# 4/// Views Returning Errors
    # Returning Errors
        # Instead of a normal HttpResponse object,a view can return an HTTP status code
            # Using HttpResponse subclasses
                # There are a list of HttpResponse subclasses for several common HTTP status codes that can be returned to signify an error

            # Passing an HTTP status code to the HttpResponse class
                # If there is no subclass for specific status code,you could create a return class for any status code
            # Raising Http404 exception
                # Unlike HttpResponseNotFound,it is an exception
                # It returns an application's standard error page and an HTTP 404 status code