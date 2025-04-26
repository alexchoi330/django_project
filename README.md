Python Django Coding Assignment - Alex Choi

create a Django website that models products, catgegories and tags
- appropriate relationships between models
- populate database with sample data using django built in admin interface
- create a basic HTML that allows:
    - user to search and filter products based on description, category, tags

Data population: (use django admin interface to fill in these data, have at least..)
- 5 categories
- 10 tags
- 20 products

HTML page:
- be able to search products by description
- filter products by category
- filter products by tags
- able to combine search and filter options

Once completed:
- document everything into readme.md (set up, running project, assumptions or notes)
- probably a requirements. txt file 

- upload it to github
- share the link with the hiring team

Django Take-Home Coding Assignment

**To set up the project: Windows and macOS**

to create your virtual environment, run 'python -m venv venv' for windows, run 'python3 -m venv venv' for macOS

to activate your virtual environment, run '.\venv\Scripts\Activate.ps1' for windows, run 'source venv/bin/activate' for macOS

to install the required packages, run 'pip install -r requirements.txt' for windows and macos

to move directory to the app folder, run 'cd .\inventory_app\' for windows and macos

to create database, run 'python manage.py makemigrations' and run 'python manage.py migrate' for windows, replace 'python' with 'python3' for mac os

to load in a sample data, run 'python manage.py loaddata core/data/initial_data.json', replace 'python' with 'python3' for mac os

to run the server, run 'python manage.py runserver', replace 'python' with 'python3' for mac os

to access website, open the given local browser url (default is http://127.0.0.1:8000/) 



**Notes:**
- used chatgpt to create random data, 5 categories, 10 tags and 20 products

