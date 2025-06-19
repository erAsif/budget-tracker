📘 Personal Budget Tracker – Documentation
👤 Candidate Info

·        Name: Asif Sheikh

·        Email: erasif3210@gmail.com

·        Phone: 9146688664

·        GitHub: https://github.com/asifsheikhdev

·        Submission Date: 19-06-2025

🚀 Project Overview

This is a Personal Budget Tracker web application that allows users to:

·        Track income and expenses

·        Set a monthly budget and compare actual expenses

·        Visualize data using D3.js

·        Manage transactions by categories

·        Authenticate securely with JWT (Django Rest Framework)

🧑‍💻 Tech Stack
Backend:

·        Python 3.11

·        Django 4.x

·        Django REST Framework

·        djangorestframework-simplejwt (for authentication)

·        SQLite/PostgreSQL

Frontend:

·        Angular 16 (or React if preferred)

·        D3.js for charts

·        Bootstrap/Tailwind for styling

·        Axios/HttpClient for API integration

🔐 Test Credentials

·        Username: testuser

·        Password: testpassword123

🌐 Hosted Links

Component

	

Link




🔗 API (DRF)

	

http://127.0.0.1:8000/api/
http://localhost:8000/admin/





🧾 Frontend App

	

http://localhost:4200/login




📂 GitHub Repo

	

https://github.com/erAsif/budget_tracker

 

⚠️ Please ensure these links remain active for at least 30 days.

✅ Features
Authentication

·        JWT-based login using DRF SimpleJWT

·        Only authenticated users can access dashboard & transactions

Dashboard (with D3.js)

·        Summary of income, expense, balance

·        D3 Pie/Bar chart visualization

Transaction Management

·        Add/Edit/Delete transactions

·        Category selection: (e.g., Salary, Grocery, Rent, Entertainment)

·        Pagination & Filters (by date, category, amount)

Budget Management

·        Set monthly budget

·        Compare budget vs actual using D3.js

📦 Setup Instructions
🔧 Backend (Django)

bash

CopyEdit

git clone https://github.com/asifsheikhdev/budget-tracker.git
cd backend python -m venv
env source env/bin/activate
# On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
    

 python manage.py runserver

🌐 Frontend (Angular)

bash

CopyEdit

cd frontend npm install ng serve

📊 Libraries Used (Acknowledgements)

·        D3.js

·        Bootstrap

·        TailwindCSS

·        SimpleJWT

·        Angular

·        Django REST Framework

📌 Assumptions

·        Each user has their own transactions and budget

·        No multi-user admin or profile management is implemented

·        User registration is not required (test account is provided)

·        Categories are predefined in backend for simplicity

·        Monthly budget comparison assumes calendar month logic




