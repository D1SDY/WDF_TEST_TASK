# WDF_TEST_TASK
Requirements: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsppipenv <br>
 
Navigate to the project folder ( so ls command will print the following output Pipfile.lock Pipfile wdf )<br>
Run the "pipenv shell" comamnd <br>
Install all dependencies with "pipenv install" command<br>
Naviagte to the wgf directory <br>
Run the server with "python3 manage.py runserver" or "python manage.py runserver" depending on PATH variable on your system <br><br>

Functional ednpoint - /api/create<br>
Request: <br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"Some log text", // Log text<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"user_id":1 // User id<br>
}<br>
<br>
Response:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"status": "success",<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"data": {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"id": 1, // Log Id in the database<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"text": "Some log text", // Log text<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp"user_id": 1 // User id<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp}<br>
}<br>