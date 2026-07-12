from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


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

@app.get("/", response_class=HTMLResponse)
def Home():
    return f"<h1>Welcome to the FastAPI Blog!</h1><p>Explore our latest posts at <a href='/api/posts'>/api/posts</a></p>"

@app.get("/api/posts")
def get_posts():
    return posts