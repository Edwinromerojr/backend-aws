echo "BUILD START"
/usr/bin/python3.9 -m ensurepip
/usr/bin/python3.9 -m pip install -r requirements.txt
/usr/bin/python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"