from pydantic import EmailStr, BaseModel, ConfigDict

class studentbase(BaseModel):
    studentname : str
    studentemail : EmailStr
    studentage : int
class studentcreate(studentbase):
    pass

class studentupdate(studentbase):
    studentname : str
    studentemail : EmailStr
    studentage : int

class studentresponse(studentbase):
    studentid : int
    model_config = ConfigDict(from_attributes=True)