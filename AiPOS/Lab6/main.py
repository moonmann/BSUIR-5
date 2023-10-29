from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from models import Session, engine
from models.Course import Course
from models.Group import Group
from models.Speciality import Speciality
from models.Student import Student

templates = Jinja2Templates(directory="templates")
app = FastAPI()
session = Session


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('index.html',
{
            "request": request,
    }
)

@app.get("/courses")
async def root(request: Request):
    table_data = ""

    with session(autoflush=False, bind=engine) as db:
        courses = db.query(Course).all()
        for c in courses:
            table_data += f"<tr><td>{c.id}</td><td>{c.title}</td><td>c.stage</td></tr>"

    return templates.TemplateResponse('courses/courses.html',
{
            "request": request,

            "table_data": table_data
    }
)