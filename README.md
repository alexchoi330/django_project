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

- activate your virtual environment

windows:
```bash
.\venv\Scripts\Activate.ps1
```
mac OS
```bash
source venv/bin/activate
```

- install the required packages

windows and macOS
```bash
pip install -r requirements.txt
```

- move directory to the app folder

windows and macOS
```bash
cd .\inventory_app\
```

- create database 

windows 
```bash
python manage.py makemigrations
python manage.py migrate
```
mac OS
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

- load in a sample data 

windows
```bash
python manage.py loaddata core/data/initial_data.json
```
macOS
```bash
python3 manage.py loaddata core/data/initial_data.json
```

- run the server

windows
```bash
python manage.py runserver
```
macOS
```bash
python3 manage.py runserver
```

- access website, open the given local browser url (default is http://127.0.0.1:8000/) 



**Notes:**
- used chatgpt to create random data, 5 categories, 10 tags and 20 products

