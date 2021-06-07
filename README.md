# tsu-website-back-end

Back end for the community page of the Tech Start UCalgary website at https://tech-start-website.web.app, created referring to the Django Guide from Tech Start UCalgary found at https://docs.google.com/document/d/1Emq59prVwyzpnOW8CkTfz9FEWE00AH0epGFHji2k_lA/edit. 

To run server locally, download repository into a folder with a python virtual environment set up and enter

```
python manage.py runserver
```

in the terminal.

If changes are made to models, enter in terminal 
```
python manage.py makemigrations BackEnd
python manage.py migrate
```

To push changes to heroku app, enter in terminal

```
git push heroku HEAD:main
```

and to migrate in heroku, enter

```
heroku run python manage.py makemigrations BackEnd
heroku run manage.py migrate
```

Endpoints can be found at https://techstartbackend.herokuapp.com/. 

Find swagger documentation at https://techstartbackend.herokuapp.com/swagger/.
