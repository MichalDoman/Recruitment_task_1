# Recrutiment_task_1
Technologies used: pymongo, Django, Django Rest Framework, mongoengine, django-rest-framework-mongoengine

The usage of DRF with MongoDB has several advantages. There are decently compatibile, DRF has very good serialization which, at the same time makes it easy to validate data. Easy model conversion with mongoengine and generic views for every CRUD action.

# Docker pull
~~~
docker pull ghcr.io/michaldoman/drf_docker_ghcr:latest
~~~
The app will run on: localhost:8000

# Searching parts
searching for parts is possible through query parameters. E.g. /search_part/?name=N such query will find every part that contains n in the name, considering letter case.

# Screenshots
<p align="center">
    <img src="https://github.com/MichalDoman/Recruitment_task_1/blob/main/screenshots/screen_1.png"  width="80%" height="100%">
    <img src="https://github.com/MichalDoman/Recruitment_task_1/blob/main/screenshots/screen_2.png"  width="80%" height="100%">
    <img src="https://github.com/MichalDoman/Recruitment_task_1/blob/main/screenshots/screen_3.png"  width="80%" height="100%">
</p>
