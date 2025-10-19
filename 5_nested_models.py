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

print(patient1)
print(patient1.address.city)  # Accessing nested model field
print(patient1.address.zip_code)  # Accessing nested model field

# Benefits of Nested Models:
# 1. Modularity: Nested models allow you to break down complex data structures into smaller
#    and more manageable components. Each nested model can represent a specific aspect of the data.
# 2. Reusability: Nested models can be reused across different parent models, promoting
#    code reuse and reducing redundancy.
# 3. Clarity: By using nested models, you can provide a clear and organized
#    representation of the data structure, making it easier to understand and maintain.
# 4. Validation: Each nested model can have its own validation rules,
#    ensuring that the data adheres to specific constraints at different levels of the hierarchy.
# 5. Encapsulation: Nested models encapsulate related data and behavior,
#    allowing you to define methods and properties specific to each nested model.
# 6. Improved Readability: Nested models enhance the readability of the code by
#    providing a hierarchical structure that reflects the relationships between different data components.
# Overall, nested models in Pydantic help in creating well-structured,
# maintainable, and validated data representations, making it easier to work with complex data structures.

