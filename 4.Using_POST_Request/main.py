from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
  
app = FastAPI()

# pydantic model use to create new patient
class Patient(BaseModel):

    id : Annotated[str, Field(..., description = 'ID of the patient', examples = ['P001'])]
    name : Annotated[str, Field(..., description = 'Name of the patient')] 
    city : Annotated[str, Field(..., description = 'City where the patient is living')]
    age : Annotated[int, Field(..., gt=0, lt=120, description = 'Age of the patient')]
    gender : Annotated[Literal['male','female','others'], Field(..., description = 'Gender of the patient')]
    height : Annotated[float, Field(..., gt=0, description = 'Height of the patient in mtrs')]
    weight : Annotated[float, Field(..., gt=0, description = 'Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'normal'
        elif self.bmi < 30:
            return 'Overweight'
        else :
            return 'Obese'




# function to load data from json
def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)

    return data

# function to save data in JSON file
def save_data(data):
    with open('patient.json','w') as f:
        json.dump(data,f)


# 1st endpoint 
@app.get("/")
def hello():
    return {'message':'Hello'}

# 2nd endpoint
@app.get("/about")
def about():
    return {'message':'A fully functional api to manage your patient records'}


# 3rd endpoint where u can view your patient
@app.get("/view")
def view():
    data = load_data()

    return data


# Path parameter
# 4. endpoint to find any choice of patient
@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description='ID of the patient in the DB', example = 'P001')):
    # load all the patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail='Patient does not found')


# Query Parameter
# 5. endpoint to get data in sorted order 
@app.get('/sort')
def sort_patients(sort_by : str = Query(..., description = 'Sort on the basis of height, age, bmi'),order : str = Query('asc', description = 'sort in asc or desc order')):

    valid_fields = ['height','age','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = '404', detail = f'Invalid field select from {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code = '404', detail = f'Invalid field select between asc or desc')

    data = load_data()
    # flag for what order type it is so sorting can happen acc. to that
    sort_order = True if order == 'desc' else False
    # Sorting logic
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by,0), reverse = sort_order)

    return sorted_data


# 6. endpoint of type POST
@app.post('/create')
def create_patuent(patient : Patient):

    # load existing data
    data = load_data()

    # check if already exists 
    if patient.id in data:
        raise HTTPException(status_code = 400, detail = 'Patient already exists')
    
    # add new patient to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the JSON file
    save_data(data)

    return JSONResponse(status_code = 200, content = {'message':'patient created successfully'})
