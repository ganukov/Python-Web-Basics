# 1.Introduction to Internet
# 2.Important Definitions
# 3.HTTP Basics
# 4.URL
# 5.Tools for Developers
# 6.MIME


# 1. #
# Vast network that connects billions of devices together all over the globe
# We get indirectly connected though ISPs (Internet Service Providers)
# Networks is a group of two or more devices that can communicate
# The internet is made of hundreds of thousands of networks
# How does WEB work?
    # WEB Client is app through i`m connecting to another device(Internet Explorer,Firefox,Google Chrome)
    # Web client <<<>>>Request<<<>>>Web Server <<<>>Technology


# 2. #
# a. Servers
    # Servers are the machines that provides serives to other machines
# b. Clients
    # Clients are the machines that are used to connect to those services
# c. Network Protocol
    # Set of rules and standarts,that allow communications between network devices
    # Include mechanisms for devices to identify and make connections with each other
    # Examples : TCP,UDP,IP,ARP
    # Every message,file or stream of information is broken down to small chunks called packets
    # Each packet contains importan informations inside of it called a header:
        # Contents
        # Origin
        # Destination
    # Internet Protocol (IP)
        # All the devices on the Internet have IP Addresses
        # Each IP is unique for each computer
        # An IP Address has many parts,organized in a hierarchy : 192.168.14.120
        # 3th part is called Subnetwork , 4th part is the Device address(Identifier of the device)
    # Domain Name Server (DNS)
        # The domain name is a human way to access IP addresses for devices and websites around the world
        # 216.58.214.46 = Google.com (easier to remember)

# 3.# Hyper Text Transfer Protocol (HTTP)
    # Client --> Request --> Server
    # Methods Requests HTTP
        # Methods = POST, GET, PUT, DELETE
            # POST = Create/store a resource
            # GET = Read/retrieve a resource
            # PUT = Update/modify a resource
            # DELETE = Delete/remove a resource
    # Whats HTTP / 2.0
        # Major revision of the HTTP network protocl used by the World Wide Web (www)
        # Supported by most of the popular web browsers
# 4.# URL (UNIFORM RESOURCE LOCATOR)
    # A URL is a reference to a web resource that specifies its location on a network and mechanism for retrieving it
    # URL ENCODING
        # Safe URL characters : [0-9a-zA-Z],$,-,_,.,+,*,',(,),,,! everything else is ENCODED
            # All other characters are escaped by : %[character hex code]
                # Example = Space is encoded as "+" or "%20"

# 5.# TOOLS FOR DEVELOPERS
    #- Browser Dev Tools
    #- Postman - Chrome
    #- Rested - Firefox

# 6.# MIME = Multi Purpose Internet Mail Extensions
    # Internet standard for encoding resources
    # Originally developed for email attachments
    # Used in many Internet protocols like HTTP and SMTP
    # Commom MIME Media Types:
        # application/json = JSON data
        # image/png = PNG image
        # image/gif = GIF image
        # text/html = HTML
        # text/plain = Text
        # text/xml = XML
        # video/mp4 = MP4 video
        # application/pdf = PDF document

# HTTP request message
    # HTTP request line
        # Request method(GET/POST/PUT/DELETE/...)
        # Resource URI(URL)
        # Protocol version
#<method><url>HTTP/<version><headers>
# (empty line)
# <body>

    # HTTP request headers
        # Additional parameters
    # HTTP request body - optional data
# GET is only for taking information (doesn't have a body)
# POST can have a body

# HTTP Response message
    # sent by the HTTP server
    # HTTP response status line
        # Protocol version
        # Status code
        # Status text
    # HTTP response headers
        # provide meta data from the returned resource
    # HTTP response body
        # The content of the HTTP response(data)
# HTTP Response Codes
    # HTTP response code classes
        # 1xx:informational("100 Continue")
        # 2xx:successful("200 OK","201 Created")
        # 3xx:redirection("304 Not Modified","301 Moved Permanently","302 Found")
        # 4xx:client error("400 Bad Request","404 Not Found","401 Unauthorized","409 Conflict")
        # 5xx:server error("503 Service Unavailable")
        
