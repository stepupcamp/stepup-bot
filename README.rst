
Getting started
~~~~~~~~~~~~~~~

* Pull the docker image of duckling: ``docker pull rasa/duckling``
* For rasa installation follow: <https://rasa.com/docs/rasa/installation/>.

Running Application
~~~~~~~~~~~~~~~~~~~

- Terminal 1: From ``rasa/rasa-bot`` do: ``docker run -p 8000:8000 rasa/duckling``

- Terminal 2: From ``rasa/project`` do: ``python manage.py runserver 7000``

- Terminal 3: From ``rasa/rasa-bot`` do: ``rasa run -m models --enable-api --cors "*" --debug``


Testing Bot
~~~~~~~~~~~

- Check the application at <http://127.0.0.1:7000/chat_app/>
