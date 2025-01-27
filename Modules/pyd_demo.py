#PYDANTIC
print("\nPYDANTIC\n")
from pydantic import BaseModel, field_validator
class User(BaseModel):
    name: str
    age: int
    city: str
    email: str

user = User(name="Alice", age="25", city="New York", email="123")
print(user)
print(type(user.age))


#Field Validators and Fields
print("\nFIELD VALIDATORS AND FIELDS\n")
from pydantic import EmailStr, Field
class Person(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, le=100)
    city: str
    email: str = Field(..., pattern=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    pemail: EmailStr
    price: float = Field(ge=0, description="Price of the product")

    @field_validator("email")
    def validate_email(cls, value):
        if "@example.com" not in value:
            raise ValueError("Email must be @example.com domain")
        return value
try:
    person = Person(name="Alice", age=22, city="New York", email="123@example.com",pemail="12345@123.in")
    print(person)  
except ValueError as e:
    print("Validation Error:", e)

#Root Validators
print("\nROOT VALIDATORS\n")
from pydantic import model_validator
class AgeRange(BaseModel):
    min_age: int
    max_age: int

    @model_validator(mode="after")  
    def validate_age_range(cls, values):
        if values.min_age > values.max_age:
            raise ValueError("min_age must be less than or equal to max_age")
        return values

# Valid example
age_range = AgeRange(min_age=18, max_age=30)
print(age_range)

# Invalid example
# try:
#     invalid_age_range = AgeRange(min_age=35, max_age=30)
# except ValueError as e:
#     print("Validation Error:", e)


#Serialization and Parsing
print("\nSERIALIZATION AND PARSING\n")

from pydantic import BaseModel
class User(BaseModel):
    name: str
    age: int
    city: str
    email: str

user = User(name="Alice", age=25, city="New York", email="12.in")
print(user)
print(user.model_dump_json())
print(type(user.model_dump_json()))
print(user.model_dump())
print(type(user.model_dump()))