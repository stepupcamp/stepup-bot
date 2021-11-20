
Getting started
~~~~~~~~~~~~~~~

* Pull the docker image of duckling: ``docker pull rasa/duckling``
* For installing rasa inside virtual environment check <https://rasa.com/docs/rasa/installation/>. Then to install some other dependencies do ``pip install google-auth==1.10.1 prompt-toolkit==2.0.10 questionary==1.4.0 SQLAlchemy==1.3.12 urllib3==1.25.7``

Running Application
~~~~~~~~~~~~~~~~~~~

- Terminal 1: From ``rasa/rasa-bot`` do: ``docker run -p 8000:8000 rasa/duckling``

- Terminal 2: From ``rasa/project`` do: ``python manage.py runserver 7000``

- Terminal 3: From ``rasa/rasa-bot`` do: ``rasa run -m models --enable-api --cors "*" --debug``


Testing Bot
~~~~~~~~~~~

- Check the application at <http://127.0.0.1:7000/chat_app/>
