#/bin/bash!

export DEBUG=True
export SECRET_KEY='django-insecure-@grn@^$0s()xoz+tc@fbnk$hz-s6*tflz@@cmm2(5@+yw2m16&'
export ALLOWED_HOSTS=*
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/postgres

# django superuser
export DJANGO_SUPERUSER_PASSWORD=admin123
export DJANGO_SUPERUSER_EMAIL=ricardoccpp@gmail.com
export DJANGO_SUPERUSER_USERNAME=admin

# postgres
export POSTGRES_USER=root
export POSTGRES_PASSWORD=root123
export POSTGRES_DB=public
export POSTGRES_HOST=localhost