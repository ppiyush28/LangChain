from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    user:str = 'test'
    age:Optional[int] = None
    email : EmailStr
    cgpa : Optional[float] = Field(gt=1,lt=10, default=5.0, description="CGPA must be between 1 and 10")



#new_user = {"user": "John Doe","age": 30}
new_user = {"user": "John Doe","email":"p@gmail.com"}
user = User(**new_user)

print(user)