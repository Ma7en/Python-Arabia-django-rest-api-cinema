<h1 align="center" id="title">Dicussion Board - Backend - APi</h1>

<h2 id="description">Description</h2>

<p>
 
</p>

## 🔧 Github Commands :-

`Step 1` : SSH Configuration.

```
ssh-keygen -t ed25519 -C "ex@gmail.com"
```

```
cat ~/.ssh/id_ed25519.pub
```

```
git config --global user.email "ex@gmail.com"
```

```
git config --global user.name "ex"
```

`Step 2` : Starting Git.

```
git init
```

```
git add .
```

```
git commit -m "first commit"
```

```
git branch -M main
```

```
git remote add origin  git@github.com:ma7en/django-full-dicussion-board-3.git
```

```
git push -u origin main
```

`Step 3` : Clone.

```
git clone  git@github.com:ma7en/django-full-dicussion-board-3.git
```

`Step 4` : Pull.

```
git pull -r origin main
```

```
Accept Both Changes
```

```
git rebase --continue
```

```
git config --global pull.rebase true
```

`Step 5` : Tag.

```
git checkout main
```

```
git tag
```

```
git tag -a v1.0 -m "Version 1.0"
```

```
git push origin v1.0
```

---

## 🛠️ Installation Steps :-

<h3 align="center"> Ubuntu </h3>

`Step 1` : Install and activate VirtualEnvironment.

```
pip install virtualenv
```

```
virtualenv venv
```

```
source venv/bin/activate
```

`Step 2` : Install Packages.

```
pip install django
```

```
pip install --upgrade pip
```

```
pip install psycopg2-binary
```

```
pip install pillow
```

```
pip install django-crispy-forms
```

```
pip install crispy-bootstrap5
```

```
pip install djangorestframework
```

```
pip install fontawesomefree
```

```
pip install django-jquery
```

```
pip install django-cleanup
```

```
pip install django-utils-six
```

```
pip install social-auth-app-django
```

```
pip install django-allauth
```

```
pip install python-dotenv
```

```
pip install django-countries
```

`Step 3` : Install requiremental Packages.

```
pip freeze > requirements.txt
```

```
pip install -r requirements.txt
```

`Step 4` : Create Project.

```
django-admin startproject crowdfunding
```

```
cd crowdfunding
```

`Step 5` : Create Apps.

```
python3 manage.py startapp account
```

```
python3 manage.py startapp projects
```

```
python3 manage.py startapp home
```

```
python3 manage.py startapp Feedback
```

`Step 6` : Create Database.

```
su - postgres
```

```
psql
```

```
CREATE USER django WITH PASSWORD 'mazen@@1';
```

```
create database boards_django;
```

```
\c boards_django;
```

```
GRANT ALL PRIVILEGES ON DATABASE boards_django TO django;
```

```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django;
```

```
GRANT ALL PRIVILEGES ON SCHEMA public TO django;
```

```
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django;
```

`Step 7` : Create Migrate.

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

```
python3 manage.py createsuperuser
```

```
django_proj
```

```
django_proj@gmail.com
```

```
django@@1
```

`Step 8` : Run Server.

```
python3 manage.py runserver
```

<h3 align="center"> Windows </h3>

`Step 1` : Install and activate VirtualEnvironment.

```
pip install virtualenv
```

```
virtualenv wvenv
```

```
wvenv\Scripts\activate
```

`Step 2` : Install Packages.

```
pip install django
```

```
pip install --upgrade pip
```

```
pip install psycopg2-binary
```

```
pip install djangorestframework
```

```
------------------------------------------------
```

```
pip install pillow
```

```
pip install django-crispy-forms
```

```
pip install crispy-bootstrap5
```

```
pip install fontawesomefree
```

```
pip install django-jquery
```

```
pip install django-cleanup
```

```
pip install django-utils-six
```

```
pip install social-auth-app-django
```

```
pip install django-allauth
```

```
pip install python-dotenv
```

```
pip install django-countries
```

`Step 3` : Install requiremental Packages.

```
pip freeze > wrequirements.txt

```

```
pip install -r wrequirements.txt
```

`Step 4` : Create Project.

```
django-admin startproject dicussion_board_api
```

```
cd dicussion_board_api
```

`Step 5` : Create Apps.

```
python manage.py startapp boards
```

```
python manage.py startapp projects
```

```
python manage.py startapp home
```

```
python manage.py startapp Feedback
```

`Step 6` : Create Database.

```
su - postgres
```

```
psql
```

```
CREATE USER django WITH PASSWORD 'django@@1';
```

```
create database boards_django_api;
```

```
\c boards_django_api
```

```
GRANT ALL PRIVILEGES ON DATABASE boards_django_api TO django;
```

```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django;
```

```
GRANT ALL PRIVILEGES ON SCHEMA public TO django;
```

```
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django;
```

`Step 7` : Create Migrate.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py createsuperuser
```

```
django
```

```
django@gmail.com
```

```
django@@1
```

`Step 8` : Run Server.

```
python manage.py runserver
```

`Step 9` : Login

```
mazen20
```

```
Mazen@@123
```

---

## 🧐 Features :

---

## 💻 Built with :-

Technologies used in the project:

-   Django Framework
-   Postgres Database
-   HTML
-   CSS
-   JS
-   Bootstrap
-   Fontawesome

---
