from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import models

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root(request: Request):
    return RedirectResponse("static/forms/index.html")


@app.get("/create_student")
async def create_table():
    # TODO create form
    html_content = """
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        """
    return HTMLResponse(content=html_content, status_code=200)
