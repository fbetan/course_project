Project Report 

*** A bash script has been provided to allow for ease of starting the project server. After running the 'run.sh' script, you should be able to access each application via the following:
base localhost/
basic frontend:  /politicians
data collector: /data_collector
data analyzer:  /data_analyzer
***


Purpose: 
This project created a means to quickly and easily access basic information about U.S. politicians, their funding sources, and how industries fund/influcence politics. 

System Requirements:
Requirements are minimal, as a virtual environment containing all necessary python packages is included. Django is the primary framework.

Design:

- Framework:
    Django was used as the framework, as it provided a simple directory structure to support multiple applications, with ease of integration. 

- Database:
    Sqlite is used by default for django projects, and coupled with django's management file, allows for easy migrations, especially in this case where the database is not user/password protected 

- Applications:
    Three applications were created for sensible division of function.
    - Basic Frontend: Politicians 
        - A simple form allowing the user to search for politicians by state, or to search basic information on a politician by name 
    - Data Collector:
        - Primarily a backend application, with additional frontend functionality if needed. This contains the API class that can be called by either the Politicians frontend or the Data Analyzer Application if necessary. 
    - Data Analyzer:
        - Also presented as a simple web form, this application returns data on a politician's funding sources by industry, or returns data on which politicians an industry provides funding to, and a total of funding by party

- Testing:
    - Django provides simple test suite functionality, which can run all test.py files present across applications. Unit and Integration testing for the three separate applications was implemented to ensure proper function of app functions, api calls, and database integration. 

-CI/CD:
    - The project uses a github respository with 2 branches, main and dev, for source control. 
