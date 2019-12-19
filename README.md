# How to run this app in Windows Machine.
1. create virtual env using following command.
    - py -m venv venv
2. Activate the environment (the path to virtual environment should be visible under the result of previous command).
    - .\venv\Scripts\activate
3. to install the dependencies run `pip install -r requirements.txt`  
4. in command prompt run following command.
    - set FLASK_APP="app.py"
5. execute the following command to run the app.
    - python -m flask run 
    - python -m flask run=0.0.0.0 (to run on, externally visible server)
