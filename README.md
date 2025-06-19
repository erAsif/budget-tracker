frontEnd----------
om command prompt(CMD)
git clone https://github.com/erAsif/budget_tracker.git

cd budget_tracker

npm install

ng serve

http://localhost:4200/login

Backend-----------

git clone https://github.com/erAsif/budget-tracker.git

cd budget-tracker\Backend\budjet_tracker

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
					Username: Asif
					Email address: asif@test.com
					Password: Asif
					Password (again): Asif
					The password is too similar to the username.
					This password is too short. It must contain at least 8 characters.
					Bypass password validation and create user anyway? [y/N]: y
					Superuser created successfully.
userName admin
password  Admin

python manage.py  runserver

http://127.0.0.1:8000/admin/  for admin login
http://localhost:8000/admin/personal_tracker/category/add/   here you can create category   
											Category Name	Type
											Salary		income
											Grocery		expense
											Rent		expense
											Freelance	income
											Entertainment	expense


http://127.0.0.1:8000/api/    for api page

