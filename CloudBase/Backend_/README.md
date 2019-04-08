# CloudBase

delete env folder if it is not created by you\
if you do not have virtualenv, use 'py -m pip install --user virtualenv'\
for details: visit https://packaging.python.org/guides/installing-using-pip-and-virtualenv/ or search install virtualenv\

create your env in the same place\
using 'py -m virtualenv env'\
env should be in Cloudbase/Backend_/ \
for details: visit https://packaging.python.org/guides/installing-using-pip-and-virtualenv/ \

before run django part, you need to get in env first\
for Windows: '.\env\Scripts\activate'\
for max or Linus: 'source env/bin/activate'\

To install django and django rest framework\
pip install django\
pip install djangorestframework\

In your mysql database, create database called "nba_data"\
In Cloudbase/Backend_/src/src/setting.py \
Change Database info (user and password) to your own at line 84 and 85\
DATABASES = {\
    'default': {\
        'ENGINE': 'django.db.backends.mysql',\
        'NAME': 'nba_data',\
		    'USER': '????',\
		    'PASSWORD': '????',\
    }\
}\

I have created a superuser that you can use, but if you want to create your own superuser\
use 'python manage.py createsuperuser' and it will ask you to input username, email, password and re-enter passwork \
User I already made\
username: cloudbase\
email: chzh5137@colorado.edu\
password: cloudbase\

in folder CloudBase/Backend_/src\
run 'py manage.py migrate' to input table I have made with all column names\
run 'py manage.py runserver' to start server and you can see database info in the link\
if you saw page with error, that's fine\
use http://127.0.0.1:8000/admin/ and you will see a login page.\
you can either use my username password or use the one you created\
after inserting all rows using file "nba_data_insert" inside BackendData folder\
you can see all data are in Statss\
