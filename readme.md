https://docs.djangoproject.com/en/5.0/topics/i18n/
https://docs.djangoproject.com/en/5.0/topics/http/decorators/
https://github.com/django-crispy-forms/crispy-tailwind
https://ccbv.co.uk/
https://www.tailwindcss.com/
https://www.hyperui.dev/components/application-ui/headers

git clone https:github.com/luis-code-666/coffee_shop.git
python -m venv venv
python3 -m venv venv
source venv/bin/activate

pip install django
cd coffee_shop/

pip install -r requirements.txt 
pip install -r requirements-dev.txt 
python manage.py makemigrations
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py runserver

