from pydantic import BaseModel

class Patient(BaseModel):  # this class should import BaseModel tbhi ye pydantic model bnegi
    name:str
    age:int


def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('insereted')

# raw dictionary
patient_info = {'name':'nitish', 'age':30}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)