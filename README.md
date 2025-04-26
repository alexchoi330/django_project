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
# run the server
python manage.py runserver
# create a super admin account to populate the database 
python manage.py createsuperuser
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
cd inventory_app
# set up database 
python3 manage.py makemigrations
python3 manage.py migrate
# run the server
python3 manage.py runserver
``` 

- To access the website, open the local browser url given in the terminal (default is http://127.0.0.1:8000/) 

- To access the admin portal: add admin at the end of the url 

- ctrl + c to close the local development server at any moment

**Notes:**
- Used chatgpt to create random data, 5 categories, 10 tags and 20 products
- Refer to initial_data.json inside the data folder for sample data


**Assumptions**
- No need to save the data but rather manually populate the database using the admin portal