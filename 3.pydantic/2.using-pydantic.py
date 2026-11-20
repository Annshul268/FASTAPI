from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):  # this class should import BaseModel tbhi ye pydantic model bnegi
    name:str
    age:int
    email:EmailStr
    weight:float
    married: bool = False # its default value is false now 
    allergies: List[str] # why not use list bcoz we need to validate element inside list to be string
    contact_details: Optional[(Dict[str,str])] = None # Using optional now this field is optional will retuen None if nthng written



def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    print('insereted')


def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

# raw dictionary
patient_info = {'name':'nitish', 'age':30, 'email':'abc@gmail.com', 'weight':75.2, 'married':True, 'allergies' :['pollen','dust']}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)