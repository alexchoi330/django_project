# Python Django Coding Assignment - Alex Choi

**Setting up the project: Windows and macOS**
    
windows
```bash
# create your virtual environment
python -m venv venv
# activate your virtual environment
.\venv\Scripts\Activate.ps1
# install the required packages
pip install -r requirements.txt
# move directory to the app folder
cd .\inventory_app\
# set up database 
python manage.py makemigrations
python manage.py migrate
# load in a sample data 
python manage.py loaddata core/data/initial_data.json
# run the server
python manage.py runserver
``` 

macOS
```bash
# create your virtual environment
python3 -m venv venv
# activate your virtual environment
source venv/bin/activate
# install the required packages
pip install -r requirements.txt
# move directory to the app folder
cd .\inventory_app\
# set up database 
python3 manage.py makemigrations
python3 manage.py migrate
# load in a sample data 
python3 manage.py loaddata core/data/initial_data.json
# run the server
python3 manage.py runserver
``` 

- access website, open the given local browser url (default is http://127.0.0.1:8000/) 

- ctrl + c to exit the local server at any moment

**Notes:**
- used chatgpt to create random data, 5 categories, 10 tags and 20 products

