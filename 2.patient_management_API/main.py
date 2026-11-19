from fastapi import FastAPI, Path, HTTPException, Query
import json


app = FastAPI()

# function to load data from json
def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)

    return data

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


