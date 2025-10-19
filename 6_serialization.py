# nested models : it defined as the model within another model as a field.
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: 'Address'  # Nested model

address_dict = {
    'street': '123 Main St',
    'city': 'Springfield',
    'state': 'IL',
    'zip_code': '62701'
}

address1 = Address(**address_dict)
patient_dict = {
    'name': 'John Doe',
    'gender': 'Male',
    'age': 30,      
    'address': address1
}

patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump()
temp2 = patient1.model_dump(include=['name', 'address'])
temp3 = patient1.model_dump(exclude=['name', 'address'])
temp4 = patient1.model_dump(include={'address': {'city', 'state'}})
temp5 = patient1.model_dump(exclude={'address': {'street', 'zip_code'}})
print(temp1)
print(temp2)
print(temp3)
print(temp4)
print(temp5)
print(type(temp1))

json1 = patient1.model_dump_json()
json2 = patient1.model_dump_json(include={'name', 'address'})
json3 = patient1.model_dump_json(exclude={'name', 'address'})
json4 = patient1.model_dump_json(include={'address': {'city', 'state'}})
json5 = patient1.model_dump_json(exclude={'address': {'street', 'zip_code'}})
print(json1)
print(json2)
print(json3)
print(json4)
print(json5)
print(type(json1))


# serialization: Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted and then reconstructed later. In Pydantic, serialization is achieved using the model_dump and model_dump_json methods.

# use of exclude_unset: By default, Pydantic includes all fields in the serialized output, even if they were not explicitly set (i.e., they have default values). However, you can use the exclude_unset parameter to exclude fields that were not explicitly set when creating the model instance.
# example of exclude_unset in comment line new code:
# from pydantic import BaseModel, Field
# from typing import Optional
# class Patient(BaseModel):
#     name: str
#     age: Optional[int] = Field(default=None)
# patient1 = Patient(name='John Doe')
# temp = patient1.model_dump(exclude_unset=True)
# print(temp)  # Output: {'name': 'John Doe'}
# In this example, the age field is not included in the serialized output because it was not explicitly set when creating the patient1 instance.



# use of by_alias: Pydantic allows you to define aliases for model fields using the alias parameter in the Field function. When serializing the model, you can use the by_alias parameter to control whether to use the field names or their aliases in the output.
# example of by_alias in comment line new code:
# from pydantic import BaseModel, Field
# class Patient(BaseModel):
#     name: str = Field(alias='full_name')
# patient1 = Patient(full_name='John Doe')
# temp = patient1.model_dump(by_alias=True)
# print(temp)  # Output: {'full_name': 'John Doe'}
# In this example, the name field is serialized using its alias full_name when by_alias=True is specified.


# use of exclude_defaults: The exclude_defaults parameter allows you to exclude fields that have their default values from the serialized output.
# example of exclude_defaults in comment line new code:
# from pydantic import BaseModel, Field
# class Patient(BaseModel):
#     name: str
#     age: int = Field(default=30)
# patient1 = Patient(name='John Doe', age=30)
# temp = patient1.model_dump(exclude_defaults=True)
# print(temp)  # Output: {'name': 'John Doe'}
# In this example, the age field is not included in the serialized output because it has its
# default value of 30.