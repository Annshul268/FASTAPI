# for type validation we have to enfore it forcefully through logic which is not efficient if there is lot of function present.

# for data validation, if age is negative we have to impose a condition which is not efficient bcoz we have to write long biolerplate

def insert_patient_data(name:str,age:int):

    if(type(name) == str and type(age) == int):
        if age < 0:
            raise ValueError('Age can not be negative')
        print(name)
        print(age)
        print("Inserted into database")
    else:
        return TypeError("Incorrect types")

insert_patient_data("Anshul","21")

