# 1.Data Management
# 2.PostgreSQL
# 3.Structured Query Language
# 4.Data Types
# 5.Table Relations
# 6.Basic SQL Commands

# 1//
#
# Storage vs Management
# Database is an organized collection of related information
#     The user doesn't have direct access to the stored data
#     Access to data is usually provided by a DBMS(Database management system)
# !!!The table is the main building block of ANY database
# Each row is called a record or entity
# Each column (field) define the type of data it contains
# DATA BASE MANAGEMENT SYSTEM
    # Provides tools to define,manipulate,retrieve and manage data in database
    # Parses requests from the user and takes the appropriate action
    # Client(browser) >>> Engine(Django) >> DATABASE

# 2// What is PostgreSQL?
# Object - relational database management system(ORDBMS)
# Widely used open-source cross-platform system
# What makes PostgreSQL stand out?
    # First DBMS that implements Multi-version concurrency control feature
    # Able to add custom functions
    # Designed to be extensible
    # Defining custom data types,plugins,etc.
    # Very active community

# 3// SQL???
    # Programming language , designed for managing data in a ralational database
        # Access many records with one single command
        # Eliminates the need to specify how to reach a record

    # Subdivided into several language elements
        # Queries
        # Clauses
        # Expressions
        # Predicates
        # Statements

    # SQL VS NoSQL
        # SQL:                                                          NoSQL:
            # Relational database management system                         # Non-relational database system
            # Predefiened Schema                                            # Dynamic Schema
            # Suited for complex queries                                    # Suited for hierarchical data storage
            # Vertically scalable                                           # Horizontally scalable

    # Data types in SQL
        # CHARACTER/CHAR[(M)]
            # fixed lenght e.g., CHAR(30)
            # CHAR without the lenght specifier(m) is the same as CHAR(1)
        # CHARACHTER VARYING/VARCHAR[(N)]
            # Variable lenght with limig e.g.,VARCHAR(30)
            # VARCHAR without(n) can store a string with unlimited lenght
        # TEXT
            # Stores strings of any length

    # Numeric Data Types
        # Integer Types : The type INTEGER/INT is the commong choice
            # SMALLINT,INTEGER/INT,BIGINT
        # Arbitrary Precision Numbers : Recommended for storing quantities where exactness is required
            # DECIMAL,NUMERIC
        # Floating Point Types : Storing and retrieving a value might show a slight difference
            # REAL,DOUBLE PRECISION
        # Serial Types
            # SMALLSERIAL,SERIAL,BIGSERIAL : Used for creating identifier culumns

    # COLUMN PROPERTIES
        # Set no repeatable characters in the entire table
            # email VARCHAR(50) UNIQUE
        # If a value is not specified,use the default one
            # balance DECIMAL(10,2) DEFAULT 0
        # Set a column that must not assume a null value
            # name VARCHAR(100) NOT NULL

    # Create table using SQL

        # CREATE TABLE department(
        #        def_id SERIAL UNIQUE NOT NULL,
        #        dep_name VARCHAR(100) UNIQUE NOT NULL,
        #        dep_location VARCHAR(100) DEFAULT 'Sofia'
        #        );

# 5//
# Table Relations
    # Relational Database Model in Action
        # Denormalized model = info from table , if we want to add more , we have to add a column manually
        # Its faster,repeating data
        # Normalized model = info from table , if want to add more, we make another table with the info numerised(primary key),
        # and we add the numbers(called foreign key) in the first table as a new column.
        # a little slower,no repeating data to manage

        # !!! Relationships between tables are based on interconnections: PRIMARY KEY / FOREIGN KEY
            # The foreign key is an identifier of a record located in another table(usually its primary key)
            # By using relationships , we avoid repeating data in the database
            # Relationships have multiplicity:
                # One to many eg mountains/peaks
                # Many to many eg student/course
                # One to one eg driver/ cacr
            # Set a primary key to uniquely define a record
                # id BIGINT PRIMARY KEY
            # Set a foreign key to reference the pk of another table
                # fk_column_name REFERENCES parent_table
                # fl_column_name REFERENCES parent_table(column_name)
                # FOREIGN KEY (first_fk,second_fk)
                # REFERENCES other_table(first_column,second_column)

            # On delete option
                # When a record that holds a relation is removed,we have a few options:
                    # Disallow deleting the referenced (parent) record
                    # Delete the referenced(parent) record and all its references as well
                    # Delete the referenced(parent) record but keep the references
                # Delete cascade statement
                    # Restrict deleting the record
                        # fk_column_name REFERENCES parent_table ON DELETE RESTRICT;
                    # Automatically delete rows referencing a deleted record
                        # fk_column_name REFERENCES parent_table ON DELETE CASCADE;
                    #SET NULL to the foreign key columns when the referenced record is deleted
                        # fk_column_name REFERENCES parent_table ON DELETE SET NULL

        # We split related data to not have empty records or redundant information

# 6//
    # Basic SQL Commands
        # Create
        # Read
        # Update
        # Delete
    #Retrieve/Read records using SQL
        # Get all the information from a table
            # SELECT*FROM people; where * means for all and people is the TABLE NAME
        # You can limit the columns and number of records
            # SELECT first_name, last_name FROM people LIMIT 5;
        # You can filter with the command WHERE
            # SELECT last_name, department_id
            # FROM employees
            # WHERE department_id = 1;
        # LOGICAL and COMPARISON OPERATORS can be used for better control
            # SELECT last_name,salary
            # FROM employees
            # WHERE salary >= 10000 AND salary <= 20000;
        # THE SQL UPDATE COMMAND
            # UPDATE employees
            #    SET last_name = 'Brown'
            #   WHERE employee_id = 1;
            #N.B. DONT FORGET THE WHERE clause,because it will update every single row
        # Altering Tables using SQL
            # ALTER TABLE = used when u need to change something on an already created table
                # ALTER TABLE employees
                # add new column
                    # ALTER TABLE employees
                    # ADD COLUMN salary DECIMAL;
            # delete existing column
                # ALTER TABLE people
                # DROP COLUMN full_name
            # modify data type of existing column
                # ALTER TABLE people
                # MODIFY COLUMN email VARCHAR(100);
            # DROPPING and TRUNCATING
                # TO DELETE ALL THE INFO IN A TABLE
                    # TRUNCATE TABLE employees;
                # TO DROP A TABLE = DELETE INFO AND STRUCTURE
                    # DROP TABLE employees;
                # TO DROP ENTIRE DATABASE
                    # DROP DATABASE soft_uni
            # SQL JOINS
                # JOIN ON (...)
