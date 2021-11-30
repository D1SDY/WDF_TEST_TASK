# WDF_TEST_TASK
Requirements: <br>
  pipenv <br>
 
Navigate to the project folder ( so ls command will print the following output Pipfile.lock Pipfile wdf )<br>
Run the "pipenv shell" comamnd <br>
Install all dependencies with "pipenv install" command<br>
Naviagte to the wgf directory <br>
Run the server with "python3 manage.py runserver" or "python manage.py runserver" depending on PATH variable on your system <br><br>

Functional ednpoint - /api/create<br>
request: <br>
{<br>
  "Some log text", // Log text<br>
  "user_id":1 // User id<br>
}<br>
Response:<br>
{<br>
    "status": "success",<br>
    "data": {<br>
        "id": 1, // Log Id in the database<br>
        "text": "Some log text", // Log text<br>
        "user_id": 1 // User id<br>
    }<br>
}<br>