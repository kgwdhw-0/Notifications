# Notification Service

A Django REST API to create and manage notifications via Email, SMS, and In-App.

---

## Project Structure



Notification\_Service/
│
├── Notifications/               # Django app
│   ├── migrations/
│   ├── templates/
│   │   └── notifications/
│   │       └── in\_app.html     # In-app notifications page
│   ├── utils/
│   │   ├── email\_sender.py
│   │   ├── sms\_sender.py
│   │   └── in\_app\_handler.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── Notification\_Service/       # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md

`

---

## Features

- Create notifications of types: EMAIL, SMS, IN_APP
- List notifications per user
- Render in-app notifications on home page

---

## Installation & Setup

1. Clone the repo:
   bash
   git clone https://github.com/yourusername/Notifications.git
   cd Notifications
`

2. Create and activate virtual environment:

   bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   

3. Install dependencies:

   bash
   pip install -r requirements.txt
   

4. Apply migrations:

   bash
   python manage.py migrate
   

5. Run the server:

   bash
   python manage.py runserver
   

6. Access in-app notifications page:

   
   http://127.0.0.1:8000/
   

---

## API Endpoints

| Method | Endpoint                              | Description                    |
| ------ | ------------------------------------- | ------------------------------ |
| POST   | /api/notifications/                 | Create a new notification      |
| GET    | /api/users/<user_id>/notifications/ | List notifications for a user  |
| GET    | /in-app/<user_id>/                  | View in-app notifications page |

---

## How to Test APIs

You can use curl, Postman, or HTTPie.

### Create Notification (POST)

bash
curl -X POST http://127.0.0.1:8000/api/notifications/ \
-H "Content-Type: application/json" \
-d '{
  "user_id": "bob02",
  "type": "IN_APP",
  "subject": "Welcome",
  "message": "Hello, this is an in-app notification.",
  "phone_number": null
}'


### Get Notifications for a User (GET)

bash
curl http://127.0.0.1:8000/api/users/bob02/notifications/


---

## Notes

* Modify email_sender.py, sms_sender.py for actual Email and SMS sending logic.
* Templates are under Notifications/templates/notifications/in_app.html.
* User ID in URLs is a string identifying the user for notifications.

