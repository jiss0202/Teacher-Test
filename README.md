# Teacher Test

멋쟁이 사자처럼 8기 선생님 테스트를 위한 강의평가 프로토타입 사이트 제작

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Building

It is best to use the python `venv` tool to build locally:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## requirements.txt

Don't forget to update your requirements.txt file with these new pips.
requirements.txt should have the following two lines:

```
asgiref==3.2.3
dj-database-url==0.5.0
Django==3.0.3
gunicorn==20.0.4
psycopg2-binary==2.8.4
pytz==2019.3
sqlparse==0.3.0
whitenoise==5.0.1
```

## Collaborator
- 지현이
- 이주형
- 유지연
- 최정연
- 최예은


