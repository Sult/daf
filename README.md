# daf
Full api access corporation site that later will be blown up to support multiple corporations


For this project to work a couple steps have to be taken.
First of all change the secret key in config/settings.py

Setting up databases:
Download static dumps from (use latest postgres.dmp.bz2)
staticdump:https://www.fuzzwork.co.uk/dump/
images: https://developers.eveonline.com/resource/image-export-collection

Static database
sudo - postgres
createdb static
####create user named eve (this is needed for this dump)
createuser -P
psql grant all privileges on database static to eve;
pg_restore -d static /path/to/dump/file
more info: http://www.postgresql.org/docs/9.1/static/app-pgrestore.html

Other databases:
create 2 more databases for bulk and default.
Default is for user and api data.
Bulk is used for histories of public eve data. (I will try to release regular dups of my own database)
Feel free to name them differently, just dont forget to adjust the config/settings.py file accordingly


Migrating databases:

./manage.py migrate

./manage.py migrate --database=bulk

./manage.py migrate --database=static






