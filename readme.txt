win:
python -m pip install django
python -m django startproject chaiaurDjango
cd chaiaurDjango
python manage.py startapp chai
python manage.py runserver

mac:
python3 -m pip3 install django
python3 -m django startproject chaiaurDjango
cd chaiaurDjango
python3 manage.py startapp chai
python3 manage.py runserver

intergate tailwind in django:
python3 -m pip3 install django-tailwind
python3 manage.py tailwind init
python3 manage.py tailwind install
python3 manage.py tailwind start
for production = python3 manage.py tailwind build

auto relod in django:
pip3 install django-browser-reload

make super user:
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py changepassword

models:
python3 manage.py  makemigrations chai