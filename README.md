## To Run this Project with docker follow below:

"docker-compose up --build"

the project will run at 
http://localhost:7000/

## To Run this Project without docker follow below:
```
for windows:
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
