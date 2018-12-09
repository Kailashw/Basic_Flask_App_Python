Steps to Follow to set up 'Hello World' flask app in Windows Machine.
1. The following commands should create a project folder and install virtual env in it.
    mkdir myproject
    cd myproject
    py -m venv venv
2. Activate the environment (the path to virtual environment should be visible under the result of previous command).
    .\venv\Scripts\activate 
3. pip install Flask
4. create a "hello.py" file and add following code under it.
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
4. in command prompt run following command.
    set FLASK_APP = "hello.py"
5. execute the following command to run your first flasker app.
    python -m flask run 
    python -m flask run=0.0.0.0 (to run on, externally visible server)
