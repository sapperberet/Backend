Introduction:
    This Project(Task) is about building a REST API capable of CRUD operations using SQLite and Django as the  framework of my choice i have created an interface that dynamically handles the parameters for the name of the user 
Setup Instructions
    follow the following steps:
    Clone: git clone https://github.com/sapperberet/Backend
    Install the dependencies:
        1- pip install pip install djangorestframework
        2- pip install django
    make necessary migrations:
        1- python manage.py 
        2- python manage.py makemigrations
        3- python manage.py migrate
        4- python manage.py runserver (to run the server)
    open in browser : http://localhost:8000 (Local Host)
    P.S : http://sapperberet.pythonanywhere.com/ (Server)

Setup Description:
    Using the name Class in the models making a new model that of type String being the ID (normally int but for the sake of learning and task Criteria set to String) and also an admin panel was used to test , using the serialization provided by the Django i was able to convert the queryset to readable form for the python to send back the data , the main url being 'api/' given an extention of 'user_id' you can see the users after logging in to the Django Framework API platform .
initial Problems:
        At First it was hard start a models project using django until i found out that i must remove the "Hash Bang" from the manage.py
        then I deleted the pycache__ and reran the project using python manage.py makemigrations then it worked properly
    
Database management system:
    SQLite3 database
Framework:
    Django(Python)
Hosting Platform:
    pythonAnyWhere
Actions:
    Create a New person => Method: POST
    Read (Retrieve) entity => Method: GET
    Update existing person => Method: PUT
    Delete existing person => Method: DELETE
    

Sample usage of the API:
    Say you did provide(Create) a name or an ID to the database for example 'john' it will be added to it and checked if existing within the database then you can fetch that data(Read) it and see it if it is there you can also Change (Update) that 'John' to say 'Johns' and lastly you can destroy this data (Delete) and so on with more given data and so forth.
Api Link:
    Using the same Server used in the Stage One task (PythonAnyWhere):
       <em> http://sapperberet.pythonanywhere.com/ </em>
        
Notes:
    Database Modeling:
        The UML diagram is provided as a .png in the project directory
    Testing:
        Using Postman each CRUD was tested when adding/fetching/updating/deleting the persons within the Database
    Validation:
        Testing the different ways of providing input was done to check the validity of the id given
UML Link:
    https://github.com/sapperberet/Backend/edit/main/Stage2/UML.png
E-R Link:
    https://github.com/sapperberet/Backend/edit/main/Stage2/E-R.drawio.png
