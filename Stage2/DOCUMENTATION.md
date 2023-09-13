Introduction:<br>
    This Project(Task) is about building a REST API capable of CRUD operations using SQLite and Django as the  framework of my choice i have created an interface that dynamically handles the parameters for the name of the user <br>
Setup Instructions: <br>
    follow the following steps: <br>
    Clone: git clone https://github.com/sapperberet/Backend <br>
    Install the dependencies: <br>
        1- pip install pip install djangorestframework <br>
        2- pip install django <br>
    make necessary migrations: <br>
        1- python manage.py  <br>
        2- python manage.py makemigrations <br>
        3- python manage.py migrate <br>
        4- python manage.py runserver (to run the server) <br>
    open in browser : http://localhost:8000 (Local Host) <br>
    P.S : http://sapperberet.pythonanywhere.com/ (Server) <br>

Setup Description: <br>
    Using the name Class in the models making a new model that of type String being the ID (normally int but for the sake of learning and task Criteria set to String) and also an admin panel was used to test , using the serialization provided by the Django i was able to convert the queryset to readable form for the python to send back the data , the main url being 'api/' given an extention of 'user_id' you can see the users after logging in to the Django Framework API platform .
initial Problems: <br>
        At First it was hard start a models project using django until i found out that i must remove the "Hash Bang" from the manage.py
        then I deleted the pycache__ and reran the project using python manage.py makemigrations then it worked properly
    
Database management system: <br>
    SQLite3 database <br>
Framework: <br>
    Django(Python) <br>
Hosting Platform: <br>
    pythonAnyWhere <br>
Actions: <br>
    Create a New person => Method: POST <br>
    Read (Retrieve) entity => Method: GET <br>
    Update existing person => Method: PUT <br>
    Delete existing person => Method: DELETE <br>
     

Sample usage of the API: <br>
    Say you did provide(Create) a name or an ID to the database for example 'john' it will be added to it and checked if existing within the database then you can fetch that data(Read) it and see if it is there you can also Change (Update) that 'John' to say 'Johns' and lastly you can destroy this data (Delete) and so on with more given data and so forth.
Api Link: <br>
    Using the same Server used in the Stage One task (PythonAnyWhere): <br>
       <em> http://sapperberet.pythonanywhere.com/ </em> <br>
        
Notes: <br>
    Database Modeling: <br>
        The UML diagram is provided as a .png in the project directory <br>
    Testing: <br>
        Using Postman each CRUD was tested when adding/fetching/updating/deleting the persons within the Database <br>
    Validation: <br>
        Testing the different ways of providing input was done to check the validity of the id given <br>
UML Link: <br>
    https://github.com/sapperberet/Backend/edit/main/Stage2/UML.png <br>
E-R Link: <br>
    https://github.com/sapperberet/Backend/edit/main/Stage2/E-R.drawio.png <br>
 <br>
