cd /usr/local/edx/files/NOTV2016/NOTV2016/notv2016
daemon -f  /usr/local/edx/files/NOTV2016/env/bin/gunicorn --error-logfile notv.log  --workers=3 -b 0.0.0.0:33003 notv2016.wsgi:application
