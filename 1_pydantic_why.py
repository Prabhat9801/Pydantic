from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
# Annotated is used to add metadata to types
# metadata means additional information about the type
#but if the Field is used to add additional information then why use Annotated? Because in simple words Annotated is used to add metadata to types and Field is used to define the field properties like validation, default values, etc.
# Difference between Field and Annotated:
# Field is used to define the field properties like validation, default values, etc. and Annotated is used to add metadata to types.

class Patient(BaseModel):
    name:str = Annotated[str, Field(max_length=50, title="Patient Name", description="Full name of the patient", example="John Doe")]
    email:EmailStr
    linkdin:AnyUrl
    age:int = Field(gt=0, lt=50)
    weight:float = Annotated[float, Field(gt=0, lt=300, strict=True, description="Weight of the patient in pounds")]
    married:Annotated[bool, Field(default=None, description="Marital status of the patient")]
    allergies:Optional[List[str]] = Field(max_items=5)
    contact_details:Annotated[Dict[str, str], Field(max_items=5, description="Contact details of the patient like phone number, address, etc.")]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkdin)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Patient data inserted successfully.")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkdin)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Patient data updated successfully.")

patient_info = {'name': 'John Doe', 'email':'prabhat@outlook.com', 'linkdin':'https://linkdin.com', 'age': 30, 'weight': 30, 'allergies': ['Peanuts', 'Penicillin'], 'contact_details': {'phone': '123-456-7890'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)
update_patient_data(patient1)