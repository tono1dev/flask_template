# 起動
docker-compose up

# 削除
docker rm --force 

docker-compose build --no-cache
docker exec -it flask_app /bin/sh
docker exec -it mysql bash

docker cp ./app flask_app:/app

# ネットワークを作成しないと通信できないらしい
sudo docker network create webapp-network