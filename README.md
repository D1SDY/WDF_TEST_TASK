# WDF_TEST_TASK
Requirements:
  pipenv 
 
Navigate to the project folder ( so ls command will print the following output Pipfile.lock Pipfile wdf )
Run the "pipenv shell" comamnd 
Install all dependencies with "pipenv install" command
Naviagte to the wgf directory 
Run the server with "python3 manage.py runserver" or "python manage.py runserver" depending on PATH variable on your system 

Functional ednpoint - /api/create
request: 
{
  "Some log text", // Log text
  "user_id":1 // User id
}
Response:
{
    "status": "success",
    "data": {
        "id": 1, // Log Id in the database
        "text": "Some log text", // Log text
        "user_id": 1 // User id
    }
}
