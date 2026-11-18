from pydantic import BaseModel, ConfigDict, Field, EmailStr

class CustomerBase(BaseModel):
    CustomerName : str = Field(min_length=2)
    CustomerEmail : EmailStr
    CustomerAge : int = Field(ge=5, le=65)

class CustomerUpdate(CustomerBase):
    pass

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    CustomerID : int
    model_config = ConfigDict(from_attributes=True)
