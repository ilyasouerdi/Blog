# DevJournal

<p align="center">
  <img src="static/images/logo_blog.png" alt="DevJournal Logo" width="220">
</p>

<p align="center">
A modern blogging platform built with <strong>FastAPI</strong>, <strong>Jinja2</strong>, and <strong>Bootstrap 5</strong>.
</p>

---

## 📖 About the Project

DevJournal is a personal learning project created while studying **FastAPI**.

The objective is not only to learn the FastAPI framework, but also to understand how a real web application is structured from scratch.

The project follows modern backend development practices while keeping the frontend clean and responsive using Bootstrap.

---

## 🚀 Features

* FastAPI web framework
* Jinja2 template rendering
* Bootstrap 5 responsive UI
* Static files (CSS & Images)
* Dynamic blog posts
* Modern landing page
* Reusable layout template
* REST API endpoint
* Clean project architecture

---

## 🛠️ Tech Stack

### Backend

* Python 3.13
* FastAPI
* Uvicorn
* Jinja2

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Development Tools

* uv
* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```text
Blog/
│
├── static/
│   ├── css/
│   │   └── main.css
│   │
│   └── images/
│       └── logo.png
│
├── templates/
│   ├── layout.html
│   └── Home.html
│
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/ilyasouerdi/Blog.git
```

Move into the project

```bash
cd Blog
```

Install the dependencies

```bash
uv sync
```

Run the application

```bash
fastapi dev main.py
```

or

```bash
uv run fastapi dev main.py
```

Open your browser

```
http://127.0.0.1:8000
```

---

## 📚 What I Learned

During the development of this project I learned how to:

* Install packages using **uv**
* Create isolated virtual environments
* Configure FastAPI
* Render HTML using Jinja2
* Build reusable templates
* Create a base layout
* Extend templates with Jinja2 blocks
* Serve static files
* Organize CSS and images
* Use Bootstrap components
* Build responsive layouts
* Create reusable navigation bars
* Build a hero section
* Display dynamic data
* Create API endpoints
* Manage project dependencies
* Initialize a Git repository
* Push projects to GitHub

---

## 🖼️ Current Interface

The application currently contains:

* Responsive navigation bar
* Custom DevJournal logo
* Hero banner
* Dynamic posts
* Sidebar
* Categories section
* Popular posts
* Footer

---

## 📄 API

### Get all posts

```
GET /api/posts
```

Example response

```json
[
  {
    "id":1,
    "author":"John Doe",
    "title":"Getting Started with FastAPI",
    "content":"FastAPI is a modern Python web framework...",
    "date_posted":"2026-07-12"
  }
]
```

---

## 📌 Current Progress

✔ FastAPI project initialized

✔ uv package manager

✔ Git repository

✔ GitHub repository

✔ Bootstrap integrated

✔ Static files configured

✔ Jinja2 templates

✔ Dynamic posts

✔ Responsive navigation

✔ Hero section

✔ Sidebar

✔ API endpoint

---

## 🔮 Future Improvements

* User authentication
* Registration system
* Password hashing
* Database integration
* SQLAlchemy ORM
* Alembic migrations
* Rich text editor
* Comments
* Categories
* Search
* Tags
* User profiles
* Admin dashboard
* Markdown support
* Image uploads
* Like system
* Bookmark posts
* Pagination
* Dark mode
* Email verification
* JWT Authentication
* Docker support
* CI/CD
* Unit testing
* Deployment

---

## 🎯 Project Goal

This project serves as a complete learning journey for mastering FastAPI while following professional development practices.

The long-term objective is to evolve DevJournal from a learning project into a production-ready blogging platform.


---

## 📜 License

This project is developed for educational purposes.
