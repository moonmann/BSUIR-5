from typing import List

from fastapi import FastAPI, Request, Form, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy import func, text

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
    return FileResponse("templates/index_test.html")


# region Courses CRUD
@app.get("/courses")
async def courses(request: Request):
    return FileResponse("templates/courses/courses.html")


@app.get("/get_courses")
async def get_courses(request: Request):
    with session(autoflush=False, bind=engine) as db:
        courses = db.query(Course).all()
    return courses


@app.get("/courses/create")
async def get_courses_create(request: Request):
    return FileResponse("templates/courses/create.html")


@app.post("/courses/create")
def post_courses_create(data=Body()):
    if 4 < int(data["year"]) < 1:
        return
    with session(autoflush=False, bind=engine) as db:
        course = Course(title=data["name"], stage=data["year"])
        db.add(course)
        db.commit()
        db.refresh(course)
    return {"message": "Курс успешно добавлен"}


@app.get("/courses/delete")
async def get_courses_create(request: Request):
    return FileResponse("templates/courses/delete.html")


@app.delete("/courses/delete")
def post_courses_create(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        found_course = db.query(Course).filter(Course.id == data["id"]).all()
        if not found_course:
            return JSONResponse(status_code=404, content={"message": "Курс не найден"})
        for i in found_course:
            db.delete(i)
        db.commit()
    return {"message": "Курс успешно удален"}


@app.get("/courses/update")
async def get_courses_update(request: Request):
    return FileResponse("templates/courses/update.html")


@app.post("/courses/update")
def post_courses_update(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == data["id"]).first()
        if not course:
            return JSONResponse(status_code=404, content={"message": "Курс не найден"})
        course.title = data["name"]
        course.stage = data["year"]
        db.commit()
    return {"message": "Курс успешно обновлен"}


# endregion

# region Specialities CRUD
@app.get("/specialities")
async def specialities(request: Request):
    return FileResponse("templates/specialities/specialities.html")


@app.get("/get_specialities")
async def get_specialities(request: Request):
    with session(autoflush=False, bind=engine) as db:
        specialities = db.query(Speciality).all()
    return specialities


@app.get("/specialities/create")
async def get_specialities_create(request: Request):
    return FileResponse("templates/specialities/create.html")


@app.post("/specialities/create")
def post_specialities_create(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == data["course_id"]).first()
        if course is None:
            return JSONResponse(status_code=404, content={"message": "Курс не найден"})
        speciality = Speciality(name=data["name"],
                                specialityNumber=data["specialityNumber"],
                                course_id=data["course_id"])
        db.add(speciality)
        db.commit()
    return {"Специальность добавлена."}


@app.get("/specialities/delete")
async def get_specialities_create(request: Request):
    return FileResponse("templates/specialities/delete.html")


@app.delete("/specialities/delete")
def post_specialities_create(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        found_speciality = db.query(Speciality).filter(Speciality.id == data["id"]).all()
        if not found_speciality:
            return JSONResponse(status_code=404, content={"message": "Специальность не найдена"})
        for i in found_speciality:
            db.delete(i)
        db.commit()
    return {"message": "Специальность успешно удалена"}


@app.get("/specialities/update")
async def get_specialities_update(request: Request):
    return FileResponse("templates/specialities/update.html")


@app.post("/specialities/update")
def post_specialities_update(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        course = db.query(Course).filter(Course.id == data["course_id"]).first()
        if course is None:
            return JSONResponse(status_code=404, content={"message": "Курс не найден"})
        speciality = db.query(Speciality).filter(Speciality.id == data["speciality_id"]).first()
        if not speciality:
            return JSONResponse(status_code=404, content={"message": "Специальность не найдена"})
        speciality.name = data["new_name"]
        speciality.specialityNumber = data["speciality_number"]
        speciality.course_id = data["course_id"]
        db.commit()
        return {"message": "Специальность обновлена."}


# endregion


@app.get("/groups")
async def groups(request: Request):
    return FileResponse("templates/groups/groups.html")


@app.get("/get_groups")
async def get_groups(request: Request):
    with session(autoflush=False, bind=engine) as db:
        groups = db.query(Group).all()
    return groups


@app.get("/groups/create")
async def get_groups_create(request: Request):
    return FileResponse("templates/groups/create.html")


@app.post("/groups/create")
def post_groups_create(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        speciality = db.query(Speciality).filter(Speciality.id == data["speciality_id"]).first()
        if speciality is None:
            return JSONResponse(status_code=404, content={"message": "Специальность не найдена"})
        group = Group(groupNumber=data["group_number"], speciality_id=data["speciality_id"])
        db.add(group)
        db.commit()
    return {"message": "Группа добавленна."}


@app.get("/groups/delete")
async def get_groups_create(request: Request):
    return FileResponse("templates/groups/delete.html")


@app.delete("/groups/delete")
def post_groups_create(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        found_group = db.query(Group).filter(Group.id == data["id"]).all()
        if not found_group:
            return JSONResponse(status_code=404, content={"message": "Группа не найдена"})
        for i in found_group:
            db.delete(i)
        db.commit()
    return {"message": "Группа успешно удалена"}


@app.get("/groups/update")
async def get_groups_update(request: Request):
    return FileResponse("templates/groups/update.html")


@app.post("/groups/update")
def post_groups_update(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        speciality = db.query(Speciality).filter(Speciality.id == data["speciality_id"]).first()
        if speciality is None:
            return JSONResponse(status_code=404, content={"message": "Специальность не найдена"})
        group = db.query(Group).filter(Group.id == data["group_id"]).first()
        if not group:
            return JSONResponse(status_code=404, content={"message": "Группа не найдена"})
        group.groupNumber = data["new_number"]
        group.speciality_id = data["speciality_id"]
        db.commit()
        return {"message": "Группа обновлена."}


@app.get("/students")
async def students(request: Request):
    return FileResponse("templates/students/students.html")


@app.get("/get_students")
async def get_students(request: Request):
    with session(autoflush=False, bind=engine) as db:
        students = db.query(Student).all()
    return students


@app.get("/students/create")
async def get_students_create(request: Request):
    return FileResponse("templates/students/create.html")


@app.post("/students/create")
def post_students_create(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        student = db.query(Student).filter(Student.studentNumber == data["studentNumber"]).first()
        if student is not None:
            return JSONResponse(status_code=404, content={"message": "Такой студент уже имеется"})
        group = db.query(Group).filter(Group.groupNumber == data["group_number"]).first()
        if group is None:
            return JSONResponse(status_code=404, content={"message": "Такой группы не существует"})
        student = Student(firstName=data["firstName"],
                          lastName=data["lastName"],
                          studentNumber=data["studentNumber"],
                          gpa=data["gpa"],
                          group_id=group.id)
        db.add(student)
        db.commit()
    return {"message": "Cтудент добавлен."}


@app.get("/students/delete")
async def get_students_delete(request: Request):
    return FileResponse("templates/students/delete.html")


@app.delete("/students/delete")
def post_students_delete(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        student = db.query(Student).filter(Student.studentNumber == data["number"]).first()
        if student is None:
            return JSONResponse(status_code=404, content={"message": "Такой студент не существует"})
        db.delete(student)
        db.commit()
    return {"Студент удалена."}


@app.get("/students/update")
async def get_students_update(request: Request):
    return FileResponse("templates/students/update.html")


@app.post("/students/update")
def post_students_update(data=Body()):
    with session(autoflush=False, bind=engine) as db:
        group = db.query(Group).filter(Group.groupNumber == data["group_number"]).first()
        if group is None:
            return JSONResponse(status_code=404, content={"message": "Такой группы не существует"})
        student = db.query(Student).filter(Student.studentNumber == data["studentNumber"]).first()
        if not student:
            return JSONResponse(status_code=404, content={"message": "Студент не найдена"})
        student.firstName = data["firstName"]
        student.lastName = data["lastName"]
        student.gpa = data["gpa"]
        student.group_id = group.id
        db.commit()
        return {"message": "Такого студента нет."}
