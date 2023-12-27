Запуск селениума в докере

docker build -t full_screenshot .
docker run -d -v $(pwd)/screenshots:/src/screenshots --name test full_screenshot


docker run -it -w /usr/workspace -v "$(pwd)":/usr/workspace joyzoursky/python-chromedriver:latest bash
docker run -it -w /usr/workspace -v "$(pwd)":/usr/workspace -v /usr/workspace/screenshots my-django-app



рабочие команды но нет проброса файлов

   docker build -t my-django-app .
   docker run -it -p 8000:8000 my-django-app

docker run -it -p 8000:8000 -v "$(pwd)":/code my-django-app


вот так работает
docker build -t full_screenshot .
docker-compose up

