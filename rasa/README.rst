
**Getting started**

* Pull the docker image of duckling: ``docker pull rasa/duckling``

**Running Application**

* Terminal 1:
- From ``rasa/rasa-bot`` folder do: ``docker run -p 8000:8000 rasa/duckling``

* Terminal 2:
- From ``rasa/project`` folder do: ``python manage.py runserver 7000``

* Terminal 3:
- From ``rasa/rasa-bot`` folder do: ``rasa run -m models --enable-api --cors "*" --debug``


**Test Bot**

- Check the application at ``<http://127.0.0.1:7000/chat_app/>``