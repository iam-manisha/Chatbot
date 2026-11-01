Python runs our backend code.
FastAPI helps us create the backend API.
pip installs FastAPI and other Python packages.

--> -m Tells Python to run a module
A module in Python is a file that contains Python code, such as variables, functions, or classes, that we can use in our programs.

-->What is pip in Python?
"pip is Python's package installer use to install the external libraries required for project, such as FastAPI and the Supabase Python client."

-->Question: Why do we need FastAPI?

"FastAPI is a Python web framework that helps us create APIs. In my Live Chat Support System, the backend will use these APIs to process messages, manage conversations, and communicate with the database."

--> What is a virtual environment in Python?

Answer: A virtual environment is an isolated Python environment that allows us to install project-specific packages without affecting other projects.

In our project: We use a virtual environment to keep our backend dependencies separate from other Python projects.

--->Which command creates a virtual environment in Python?

Answer: We use py -m venv .venv to create a virtual environment named .venv.
venv is a built-in Python module used to create virtual environments.

---

       VISITOR
          |
          | Sends a message
          v
     FASTAPI BACKEND
          |
          | Processes the message
          v
       SUPABASE
          |
          | Saves the message
          v
     FASTAPI BACKEND
          |
          | Generates or retrieves a reply
          v
       SUPABASE
          |
          | Saves the reply
          v
       VISITOR

---

-->What is @?

In Python, @ is used to apply a decorator.

A decorator allows us to add behavior to a function. Here, the decorator tells FastAPI to use the function below to handle a particular HTTP request.

-->What is app.get()?

It tells FastAPI to handle an HTTP GET request.

# A GET request is generally used to retrieve information from a server.

--> @app.get("/") #is a FastAPI path operation decorator that registers a function to handle GET requests sent to the root URL.

-->What is Uvicorn?

Uvicorn is a web server that runs your FastAPI application.

# FastAPI helps you build the API.

# Uvicorn runs the server that serves your FastAPI application.

What is the purpose of the app folder?
The app folder will contain the Python code for our backend application.

File or folder Purpose
main.py- Starts and configures the FastAPI application.
routes/ Contains API endpoints.
schemas/ Defines the structure and validation of request and response data.
services/ Contains application logic.
database.py Handles database connectivity.

-->What is **init**.py?
It's a special Python file commonly used to mark a directory as a Python package and optionally initialize that package.

In our project, it will help us organize and import Python modules.

-->1. What is a route?
In FastAPI, a route connects a URL and an HTTP method to a function.

-->What is a health-check endpoint?

A health-check endpoint is an API endpoint used to check whether an application or service is running and responding to requests.

-->What is JSON?
->JSON stands for JavaScript Object Notation.
->JSON is a format used to store and exchange data between applications.
->Remember: JSON organizes information using keys and values.
example:-{
"brand": "Oppo",
"color": "Black",
"price": 20000
}
->JSON is useful because it provides a standardized way for the frontend and backend to exchange structured data.
