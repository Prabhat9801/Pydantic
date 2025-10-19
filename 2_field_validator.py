from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name:str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, v):
        valid_domins = ['hdfc.com', 'icici.com']
        domain = v.split('@')[-1]
        if domain not in valid_domins:
            raise ValueError('Email domain not supported')
        return v
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, v):
        return v.upper()


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@hdfc.com', 'age': '30', 'weight': 75.2, 'married':True, 'allergies':['Peanuts', 'Penicillin'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)