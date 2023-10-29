from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

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
async def courses(request: Request):
    return templates.TemplateResponse("courses/courses.html", {"request": request})


@app.get("/get_courses")
async def get_courses(request: Request):
    table_data = "<table><tr><th>Id</th><th>Title</th><th>Stage</th></tr>"

    with session(autoflush=False, bind=engine) as db:
        courses = db.query(Course).all()
        for c in courses:
            table_data += (f"<tr>"
                           f"<td>{c.id}</td>"
                           f"<td>{c.title}</td>"
                           f"<td>{c.stage}</td>"
                           f"</tr>")
        table_data += "</table>"
    return HTMLResponse(content=table_data, status_code=200)


@app.get("/courses/create")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("courses/create.html", {"request": request})


@app.post("/courses/create")
def post_courses_create(name=Form(), year=Form()):
    if 4 < int(year) < 1:
        return
    with session(autoflush=False, bind=engine) as db:
        db.add(Course(title=name, stage=year))
        db.commit()
    return {"Курс добавлен."}


@app.get("/courses/delete")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("courses/delete.html", {"request": request})


@app.post("/courses/delete")
def post_courses_create(course_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == course_id).first()
        db.delete(course)
        db.commit()
    return {"Курс удален."}


@app.get("/courses/update")
async def get_courses_update(request: Request):
    return templates.TemplateResponse("courses/update.html", {"request": request})


@app.post("/courses/update")
def post_courses_update(course_id=Form(), name=Form(), year=Form()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is not None:
            course.title = name
            course.stage = year
            db.commit()
    return {"Курс обновлен."}
