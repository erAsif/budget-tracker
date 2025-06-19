🚀 Project Setup Instructions
🔹 Frontend (Angular)
1. Clone the Frontend Repository
bash
Copy
Edit
git clone https://github.com/erAsif/budget_tracker.git
cd budget_tracker
2. Install Dependencies
bash
Copy
Edit
npm install
3. Start the Angular Development Server
bash
Copy
Edit
ng serve
4. Open in Browser
bash
Copy
Edit
http://localhost:4200/login
🔹 Backend (Django)
1. Clone the Backend Repository
bash
Copy
Edit
git clone https://github.com/erAsif/budget-tracker.git
cd budget-tracker/Backend/budjet_tracker
2. Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv env
env\Scripts\activate  # On Windows
source env/bin/activate  # On macOS/Linux
3. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Make and Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
Provide the following values when prompted:

vbnet
Copy
Edit
Username: Asif
Email: asif@test.com
Password: Asif
Confirm Password: Asif
(Choose 'y' to bypass password validation)
Or use the default admin login:

pgsql
Copy
Edit
Username: admin
Password: Admin
6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
7. Access the Admin and API Pages
Django Admin: http://127.0.0.1:8000/admin/

Django REST API: http://127.0.0.1:8000/api/

📂 Add Categories via Admin Panel
Go to:
http://localhost:8000/admin/personal_tracker/category/add/

Example Categories:

Category Name	Type
Salary	income
Grocery	expense
Rent	expense
Freelance	income
Entertainment	expense

📌 Features
Login & Register

Transaction Management

Budget vs Expense Visualization

Add Income/Expense Categories

Admin Panel for management

REST API for integration

📞 Contact
Developer: Asif
GitHub: github.com/erAsif

