#host -> gcr.io/tap-dating-app/tap-dating-api

docker build -t tap-dating-api -f Dockerfile .

docker tag tap-dating-api gcr.io/tap-dating-app/tap-dating-api

docker push gcr.io/tap-dating-app/tap-dating-api
