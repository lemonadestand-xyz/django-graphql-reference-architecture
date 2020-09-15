gcloud run deploy tap-dating-api \
--image gcr.io/tap-dating-app/tap-dating-api \
--platform managed \
--region us-central1 \
--allow-unauthenticated \
--project tap-dating-app \
--service-account tap-dating-backend@tap-dating-app.iam.gserviceaccount.com
