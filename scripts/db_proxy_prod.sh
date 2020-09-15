
cloud_sql_proxy -instances=tap-dating-app:us-central1:tap-dating-production=tcp:6434 -credential_file=$PWD/db/creds.json