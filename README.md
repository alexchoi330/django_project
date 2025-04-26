# Python Django Coding Assignment - Alex Choi

**To set up the project: Windows and macOS**

- create your virtual environment
    
windows
```bash
python -m venv venv
``` 
mac os
```bash
python3 -m venv venv
``` 

- activate your virtual environment, 

windows:
```bash
.\venv\Scripts\Activate.ps1
```
mac OS
```bash
source venv/bin/activate
```

- install the required packages, run 'pip install -r requirements.txt' for windows and macos

- move directory to the app folder, run 'cd .\inventory_app\' for windows and macos

- create database, run 'python manage.py makemigrations' and run 'python manage.py migrate' for windows, replace 'python' with 'python3' for mac os

- load in a sample data, run 'python manage.py loaddata core/data/initial_data.json', replace 'python' with 'python3' for mac os

- run the server, run 'python manage.py runserver', replace 'python' with 'python3' for mac os

- access website, open the given local browser url (default is http://127.0.0.1:8000/) 



**Notes:**
- used chatgpt to create random data, 5 categories, 10 tags and 20 products

