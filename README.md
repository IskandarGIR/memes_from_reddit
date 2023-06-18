# Берёт мемы из reddit и присылает в телеграм-канал
### Use
```
Создайте в https://www.reddit.com/prefs/apps приложение
Добавьте бота в телеграм-канал
В перменных окружения задайте API_TOKEN, SECRETE_CODE, CLIENT_ID, CHANNEL_ID
$ git clone https://github.com/IskandarGIR/memes_from_reddit.git
$ cd memes_from_reddit/
$ docker-compose -f docker-compose.yml -p bot up
```