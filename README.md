# 🥑 MiamPlanner

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-MVP-success?style=for-the-badge)

> **A minimalist meal planner that focuses on what matters.**  
> *No more overcomplicated tools. Just you, your recipes, and your weekly plan.*

---

## 📸 Preview

## 📋 About

**MiamPlanner** was created to solve a simple problem: planning meals without drowning in unnecessary features.

Unlike traditional apps that require complex account creation or endless ingredient databases, MiamPlanner follows a strict **MVP (Minimum Viable Product)** philosophy:

* 🚫 **No user accounts** — direct and instant access.  
* 🚫 **No micro-management** — no ingredient stocks tracked by the gram.  
* ✅ **Modern Interface** — clean thanks to Tailwind CSS.  
* ✅ **Efficient** — fully focused on weekly planning.

## 🛠 Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Django | Robust and secure Python framework. |
| **Frontend** | Tailwind CSS | Utility‑first CSS framework for rapid UI. |
| **Hosting** | PythonAnywhere | PaaS deployment platform. |

## 🚀 Installation & Setup

### Requirements
* Python 3.8+
* Node.js & npm

### 1. Clone the project

```bash
git clone https://github.com/ClementLazzarini/MiamPlanner.git
cd MiamPlanner
```

### 2. Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Tailwind Setup

**With django-tailwind:**

```bash
python manage.py tailwind install
python manage.py tailwind start
```

**With npm:**

```bash
npm install
npm run dev
```

### 5. Migrations & Launch

```bash
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000 🎉

---

## 📦 Deployment (PythonAnywhere)

1. Clone the repo  
2. Set up a Virtualenv  
3. Install dependencies  
4. Ensure compiled CSS is in `static/`  
5. Configure static files  
6. Run `collectstatic`  
7. Reload

---

## 🤝 Contribute

Contributions are welcome — just keep the **KISS** philosophy in mind.

## 📄 License

MIT License.  
Made with ❤️ by **Clément Lazzarini**.
