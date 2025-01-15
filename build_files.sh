
echo " BUILD START"
python3.12 -m pip install setuptools

python3.12 -m pip install -r requirements.txt
python3.12 -m python manage.py makemigrations
python3.12 -m python manage.py migrate

python3.12 -m python manage.py collectstatic --noinput --clear

echo " BUILD END"