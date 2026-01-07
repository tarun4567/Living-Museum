# 🦁 Living Museum – Extinct & Distinct Animals

The **Living Museum** is a Django-based web application that provides detailed information about **extinct** and **distinct (rare)** animals.  
The project acts as a digital museum where users can explore animal species, their characteristics, habitats, and conservation status.

This project is developed as an academic mini/major project using the **Django framework**.

---

## 🚀 Features

- 📚 Information about extinct animals
- 🐾 Information about distinct / rare animals
- 🧑‍💼 Django admin panel for managing animal data
- 🎨 Template-based user interface
- 📂 Static files support (CSS, images)
- 🗄️ SQLite database integration

---

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML**
- **CSS**
- **SQLite**
- **Bootstrap** (optional, if used)

---

## 📁 Project Structure

```text
Living-Museum/
│
├── Museum/                 # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── LMuseum/                # Django application
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── manage.py
├── README.md
└── .gitignore

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tarun4567/Living-Museum.git
cd Living-Museum

---

2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate     # For Windows

---

3️⃣ Install Dependencies
pip install django

---

3️⃣ Install Dependencies
pip install django

---

4️⃣ Run Migrations
python manage.py migrate

---

5️⃣ Start the Server
python manage.py runserver





