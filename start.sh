source env/bin/activate
source .env

rm /etc/nginx/sites-enabled/default
cp -r ./nginx /etc
cp -r ./nginx /usr/local/etc/
nginx -s reload

pip install --no-cache-dir -r requirements.txt
cp -r aldryn_newsblog env/lib/python2.7/site-packages/

cd website
gunicorn mysite.wsgi:application -w 2 -b 0.0.0.0:8081 --reload
cd ..