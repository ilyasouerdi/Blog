from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates") 

posts = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "Getting Started with FastAPI",
        "content": "FastAPI is a modern Python web framework designed for building high-performance APIs with minimal code.",
        "date_posted": "2026-07-12"
    },
    {
        "id": 2,
        "author": "Emily Johnson",
        "title": "Understanding Python Type Hints",
        "content": "Type hints improve code readability, editor support, and help catch potential bugs before runtime.",
        "date_posted": "2026-07-10"
    },
    {
        "id": 3,
        "author": "Michael Brown",
        "title": "Why Learn SQL?",
        "content": "SQL remains one of the most valuable skills for backend developers because nearly every application stores data in a database.",
        "date_posted": "2026-07-08"
    },
    {
        "id": 4,
        "author": "Sarah Wilson",
        "title": "Introduction to REST APIs",
        "content": "REST APIs allow applications to communicate over HTTP using standard methods such as GET, POST, PUT, and DELETE.",
        "date_posted": "2026-07-05"
    },
    {
        "id": 5,
        "author": "David Lee",
        "title": "The Importance of Virtual Environments",
        "content": "Using virtual environments keeps project dependencies isolated and prevents version conflicts between different projects.",
        "date_posted": "2026-07-01"
    }
]

@app.get("/")
def Home(request: Request):
    return templates.TemplateResponse(request , "Home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts