from pydanntic import EmailStr, ConfigDict, BaseModel, Field

class CustomerBase(BaseModel):
    CustomerName:str = Field(min_length = 20)
    CustomerEmail: EmailStr
    CustomerAge:int = Field(ge=5)

class CustomerCreate(CustomerBase):
    pass
class CustomerUpdate(CustomerBase):
    CustomerName : str | None = Field(default=None, min_length=2)
    CustomerEmail : EmailStr | None = None
    CustomerAge : int | None  = Field(default=None, ge=18, le=70)
    CustomerGender : str | None  = Field(default=None, min_length=2)
class CustomerDelete(CustomerBase):
    pass
class CustomerResponse(CustomerBase):
    CustomerId:int
    model_config = ConfigDict(from_attributes=True)