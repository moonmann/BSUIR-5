from typing import List

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import func

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
    return templates.TemplateResponse('index.html', {"request": request, })


# region Courses CRUD
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


# endregion

# region Specialities CRUD
@app.get("/specialities")
async def courses(request: Request):
    return templates.TemplateResponse("specialities/specialities.html", {"request": request})


@app.get("/get_specialities")
async def get_specialities(request: Request):
    table_data = "<table><tr><th>Id</th><th>Имя специальности</th><th>Номер специальности</th><th>Курс</th></tr>"

    with session(autoflush=False, bind=engine) as db:
        specialities = db.query(Speciality).all()
        courses: List[Course] = db.query(Course).all()
        course_name = ""
        for s in specialities:
            for c in courses:
                if c.id == s.course_id:
                    course_name = c.title
            table_data += (f"<tr>"
                           f"<td>{s.id}</td>"
                           f"<td>{s.name}</td>"
                           f"<td>{s.specialityNumber}</td>"
                           f"<td>{course_name}</td>"
                           f"</tr>")
        table_data += "</table>"
    return HTMLResponse(content=table_data, status_code=200)


@app.get("/specialities/create")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("specialities/create.html", {"request": request})


@app.post("/specialities/create")
def post_courses_create(name=Form(), specialityNumber=Form(), course_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            return {"Такого курса не существует"}
        speciality = Speciality(name=name, specialityNumber=specialityNumber, course_id=course_id)
        db.add(speciality)
        db.commit()
    return {"Специальность добавлена."}


@app.get("/specialities/delete")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("specialities/delete.html", {"request": request})


@app.post("/specialities/delete")
def post_courses_create(speciality_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        specialities = db.query(Speciality).filter(Speciality.id == speciality_id).first()
        if specialities is None:
            return {"Такой специальности нет."}
        db.delete(specialities)
        db.commit()
    return {"Курс удален."}


@app.get("/specialities/update")
async def get_courses_update(request: Request):
    return templates.TemplateResponse("specialities/update.html", {"request": request})


@app.post("/specialities/update")
def post_courses_update(speciality_id=Form(), name=Form(), speciality_number=Form(), course_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            return {"Такого курса нет."}
        speciality = db.query(Speciality).filter(Speciality.id == speciality_id).first()
        if speciality is not None:
            speciality.name = name
            speciality.specialityNumber = speciality_number
            speciality.course_id = course_id
            db.commit()
            return {"Специальность обновлена."}
        else:
            return {"Такой специальности нет."}
# endregion


@app.get("/groups")
async def courses(request: Request):
    return templates.TemplateResponse("groups/groups.html", {"request": request})


@app.get("/get_groups")
async def get_groups(request: Request):
    table_data = ("<table><tr><th>Id</th><th>Номер группы</th><th>Специальность</th></tr>")

    with session(autoflush=False, bind=engine) as db:
        groups = db.query(Group).all()
        specialities: List[Speciality] = db.query(Speciality).all()
        speciality_name = ""
        for s in specialities:
            for g in groups:
                if g.speciality_id == s.id:
                    speciality_name = s.name
                    table_data += (f"<tr>"
                           f"<td>{g.id}</td>"
                           f"<td>{g.groupNumber}</td>"
                           f"<td>{speciality_name}</td>"
                           f"</tr>")
        table_data += "</table>"
    return HTMLResponse(content=table_data, status_code=200)


@app.get("/groups/create")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("groups/create.html", {"request": request})


@app.post("/groups/create")
def post_courses_create(number=Form(), speciality_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        speciality = db.query(Speciality).filter(Speciality.id == speciality_id).first()
        if speciality is None:
            return {"Такой группы не существует"}
        speciality_id = Group(groupNumber=number, speciality_id = speciality_id)
        db.add(speciality_id)
        db.commit()
    return {"Группа добавлена."}


@app.get("/groups/delete")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("groups/delete.html", {"request": request})


@app.post("/groups/delete")
def post_courses_create(groups_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        group = db.query(Group).filter(Group.id == groups_id).first()
        if group is None:
            return {"Такой группы нет."}
        db.delete(group)
        db.commit()
    return {"Группа удалена."}


@app.get("/groups/update")
async def get_courses_update(request: Request):
    return templates.TemplateResponse("groups/update.html", {"request": request})


@app.post("/groups/update")
def post_courses_update(groups_id=Form(), name=Form(), speciality_number=Form()):
    with session(autoflush=False, bind=engine) as db:
        speciality = db.query(Speciality).filter(Speciality.id == speciality_number).first()
        if speciality is None:
            return {"Такой специальности нет."}
        group = db.query(Group).filter(Group.id == groups_id).first()
        if group is not None:
            group.groupNumber = name
            group.speciality_id = speciality_number
            db.commit()
            return {"группа обновлена."}
        else:
            return {"Такой группы нет."}


@app.get("/students")
async def courses(request: Request):
    return templates.TemplateResponse("students/students.html", {"request": request})


@app.get("/get_students")
async def get_groups(request: Request):
    table_data = ("<table><tr><th>Id</th><th>Имя</th><th>Фамилия</th><th>Номер студента</th><th>Средний балл</th><th>Номер группы</th></tr>")

    with session(autoflush=False, bind=engine) as db:
        students = db.query(Student).all()
        groups: List[Group] = db.query(Group).all()
        speciality_name = ""
        for s in students:
            for g in groups:
                if g.id == s.group_id:
                    table_data += (f"<tr>"
                           f"<td>{s.id}</td>"
                           f"<td>{s.firstName}</td>"
                           f"<td>{s.lastName}</td>"
                           f"<td>{s.studentNumber}</td>"
                           f"<td>{s.gpa}</td>"
                           f"<td>{g.groupNumber}</td>"
                           f"</tr>")
        table_data += "</table>"
    return HTMLResponse(content=table_data, status_code=200)


@app.get("/students/create")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("students/create.html", {"request": request})


@app.post("/students/create")
def post_courses_create(f_name=Form(), l_name=Form(), number=Form(), gpa=Form(), group_number=Form()):
    with session(autoflush=False, bind=engine) as db:
        student = db.query(Student).filter(Student.studentNumber == number).first()
        if student is not None:
            return {"Студент с таким номером уже имееться."}
        group = db.query(Group).filter(Group.groupNumber == group_number).first()
        if group is None:
            return {"Такой группы не существует"}
        student = Student(firstName=f_name, lastName=l_name, studentNumber=number, gpa=gpa, group_id=group.id)
        db.add(student)
        db.commit()
    return {"Cтудент добавлен."}


@app.get("/students/delete")
async def get_courses_create(request: Request):
    return templates.TemplateResponse("students/delete.html", {"request": request})


@app.post("/students/delete")
def post_courses_create(number=Form()):
    with session(autoflush=False, bind=engine) as db:
        student = db.query(Student).filter(Student.studentNumber == number).first()
        if student is None:
            return {"Такого студента нет."}
        db.delete(student)
        db.commit()
    return {"Студент удалена."}


@app.get("/students/update")
async def get_courses_update(request: Request):
    return templates.TemplateResponse("students/update.html", {"request": request})


@app.post("/students/update")
def post_courses_update(number=Form(), f_name=Form(), l_name=Form(), gpa=Form(), group_id=Form()):
    with session(autoflush=False, bind=engine) as db:
        group = db.query(Group).filter(Group.id == group_id).first()
        if group is None:
            return {"Такой группы нет."}
        student = db.query(Student).filter(Student.studentNumber == number).first()
        if student is not None:
            student.firstName = f_name
            student.lastName = l_name
            student.gpa = gpa
            student.group_id = group_id
            db.commit()
            return {"Студент обновлен."}
        else:
            return {"Такого студента нет."}
