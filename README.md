# 🍽️ Little Lemon Restaurant API

This is a Django REST API project for managing a restaurant’s menu and table bookings. It allows users to view and manage menu items, make reservations, and supports token-based authentication. Built using Django REST Framework, MySQL, and Djoser.

## 📚 Table of Contents
- Features
- Tech Stack
- Getting Started
- Environment Variables
- Authentication
- API Endpoints
- Admin Panel
- Screenshots
- Project Status
- License
- Author

## ✨ Features
- ✅ Token-based authentication using Djoser
- ✅ View, create, and delete restaurant menu items
- ✅ Book tables with guest details and time
- ✅ Role-based access for authenticated users
- ✅ RESTful endpoints with JSON responses

## 🛠️ Tech Stack
| Tool       | Description                        |
|------------|------------------------------------|
| Django     | Python web framework               |
| DRF        | Django REST Framework              |
| MySQL      | Relational database                |
| Djoser     | User authentication via tokens     |
| Python     | Core programming language          |
| Postman    | API testing (optional)             |

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/srinivasgithub123/restaurant-api.git
cd restaurant-api
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Configure MySQL Database
Edit settings.py to match your MySQL credentials:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5. Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6. Start the Server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

🔑 Environment Variables
For security, store sensitive values in a .env file:

env
Copy
Edit
SECRET_KEY=your_django_secret_key
DB_NAME=littlelemon
DB_USER=youruser
DB_PASSWORD=yourpassword
🔐 Authentication
Get Token:
http
Copy
Edit
POST /api-token-auth/
Example Payload:
json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Use the token in your request headers:

makefile
Copy
Edit
Authorization: Token your_token_here
📬 API Endpoints
🔓 Public Endpoints
Method	URL	Description
GET	/api/menu/	List all menu items
POST	/api/menu/	Create a menu item
GET	/api/menu/<id>	Get menu item by ID
DELETE	/api/menu/<id>	Delete menu item by ID

🔒 Protected (Token Required)
Method	URL	Description
GET	/restaurant/booking/tables/	List bookings
POST	/restaurant/booking/tables/	Create new booking

👤 User Authentication (via Djoser)
Method	URL	Description
POST	/auth/users/	Register new user
POST	/auth/token/login/	Log in & get auth token
POST	/auth/token/logout/	Log out

🖥️ Admin Panel
Create superuser:

bash
Copy
Edit
python manage.py createsuperuser
Visit the admin panel:

arduino
Copy
Edit
http://127.0.0.1:8000/admin/
Use your superuser credentials to log in and manage Menu and Booking models.

🚧 Project Status
🟢 Completed and functional

Pagination

User role restrictions

Booking confirmation emails

🙋‍♂️ Author
Kankala Srinivas
GitHub: @srinivasgithub123
