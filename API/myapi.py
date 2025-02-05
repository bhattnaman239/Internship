from enum import Enum
from typing import List, Optional

from fastapi import (
    FastAPI,
    Request,
    Query,
    Path,
    Cookie,
    Header,
    Depends,
    File,
    UploadFile,
    status,
    BackgroundTasks,
    HTTPException
)
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()

# ---------------------------
# STUDENT ENDPOINTS
# ---------------------------
students = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
    3: {"name": "Charlie"},
}

@app.get("/")
def test():
    return students

@app.get("/items/{student_id}")
def read_student(s_id: int = Path(..., ge=1)):
    if s_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[s_id]

@app.post("/items/{student_id}")
def create_student(s_id: int, name: str):
    if s_id in students:
        return {"Error": "Student already exists"}
    students[s_id] = {"name": name}
    return students[s_id]

@app.put("/items/{student_id}")
def update_student(s_id: int, name: str):
    if s_id not in students:
        return {"Error": "Student does not exist"}
    students[s_id] = {"name": name}
    return students[s_id]

@app.delete("/items/{student_id}")
def delete_student(s_id: int):
    if s_id not in students:
        return {"Error": "Student does not exist"}
    del students[s_id]
    return {"message": "Student deleted successfully!"}

@app.get("/check/{item_id}")
def read_item_by_id(item_id: str):
    return {"item_id": item_id}


# ---------------------------
# ENUM EXAMPLE FOR MODELS
# ---------------------------
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# ---------------------------
# SIMPLE ITEM MODEL (for JSON body)
# ---------------------------
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.post("/create-item/")
def create_item(item: ItemBase):
    return item


# ---------------------------
# QUERY PARAMETERS WITH VALIDATION
# ---------------------------
@app.get("/items/")
def read_items(q: List[str] = Query(None, min_length=2)):
    return {"q": q}


# ---------------------------
# QUERY PARAMETER MODEL (using Dependency)
# ---------------------------
class UserQuery(BaseModel):
    q: str = Query(..., min_length=3)
    skip: int = Query(0, ge=0)
    limit: int = Query(10, ge=1)

@app.get("/users/model/")
def read_users(query: UserQuery = Depends()):
    return query.dict()


# ---------------------------
# COMBINING PATH, BODY, AND QUERY PARAMETERS
# ---------------------------
@app.post("/update-item/{item_id}")
def update_item_endpoint(item_id: int, item: ItemBase, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result["q"] = q
    return result


# ---------------------------
# NESTED MODELS
# ---------------------------
class Image(BaseModel):
    url: str
    height: int
    width: int

class ItemWithImage(BaseModel):
    name: str
    description: Optional[str] = None
    image: Image

@app.post("/check/")
def create_item_with_image(item: ItemWithImage):
    return item


# ---------------------------
# MODEL WITH EXAMPLE DATA (using Field)
# ---------------------------
class ItemExample(BaseModel):
    name: str = Field(..., example="Example Item")
    price: float = Field(..., example=29.99)

@app.post("/example/")
def create_item_example(item: ItemExample):
    return item


# ---------------------------
# COOKIE PARAMETER EXAMPLE
# ---------------------------
@app.get("/cookie/")
def read_cookie(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


# ---------------------------
# HEADER PARAMETER EXAMPLE
# ---------------------------
@app.get("/headers/")
def read_headers(user_agent: str = Header(...)):
    return {"User-Agent": user_agent}


# ---------------------------
# COOKIE DEPENDENCY EXAMPLE
# ---------------------------
class CookieData(BaseModel):
    session_id: str
    user_id: int

def get_cookies(session_id: str = Cookie(...), user_id: int = Cookie(...)):
    return CookieData(session_id=session_id, user_id=user_id)

@app.get("/read-cookies/")
def read_cookies(cookie_data: CookieData = Depends(get_cookies)):
    return {"session_id": cookie_data.session_id, "user_id": cookie_data.user_id}


# ---------------------------
# RESPONSE STATUS CODE EXAMPLE
# ---------------------------
@app.post("/status/", status_code=status.HTTP_201_CREATED)
def create_item_status(item: ItemExample):
    return item


# ---------------------------
# FILE UPLOAD EXAMPLE
# ---------------------------
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


# ---------------------------
# PATH OPERATION CONFIGURATION (METADATA)
# ---------------------------
@app.get(
    "/extra/{item_id}",
    tags=["items"],
    summary="Get an item by ID",
    description="Retrieve an item by its unique ID."
)
def extra_read_item(item_id: int):
    return {"item_id": item_id}


# ---------------------------
# SECURITY EXAMPLE USING OAUTH2
# ---------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
# NOTE: A /token endpoint is required for the OAuth2PasswordBearer to function fully.

# ---------------------------
# BACKGROUND TASKS EXAMPLE
# ---------------------------
def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")

@app.post("/send-notification/")
def send_notification(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Notification sent!")
    return {"message": "Notification is processing in the background"}
