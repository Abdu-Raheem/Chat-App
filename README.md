# 💬 Django Real-Time Chat App

A real-time chat application built with **Django**, **Channels**, **Redis**, and **WebSockets**. Users can register, join rooms, and send messages instantly.

---

## 🚀 Features

- 🔁 Real-time messaging using WebSockets
- 🔐 User authentication (login/signup/logout)
- 🗨️ Multiple chat rooms
- 📜 Persistent message history
- ⚡ Asynchronous event handling with Django Channels
- ⚙️ Redis-powered channel layer
- 📱 Responsive frontend (HTML, CSS, JS)

---

## 🛠 Tech Stack

- **Backend**: Django, Django Channels, ASGI
- **Real-Time**: WebSockets, Redis
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite / PostgreSQL
- **Deployment**: ASGI server (Daphne/Uvicorn), Docker (optional)

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.8+
- Redis server installed and running
- Git, pip, and virtualenv

### ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/django-chat-app.git
cd django-chat-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Redis server (in another terminal)
redis-server

# 5. Apply migrations
python manage.py migrate

# 6. Create superuser (optional)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
