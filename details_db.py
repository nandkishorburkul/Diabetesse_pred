from pymongo import MongoClient
import config

db_name = config.HPP_DATABASE
myclient = MongoClient('mongodb://localhost:27017/')
db = myclient[db_name]
collection_user = db['user_details']
collection_prediction = db['prediction_details']

def register_user(user_data):
    user_data_dict = {}
    user_data_dict['name'] = user_data['name']
    user_data_dict['password'] = user_data['password']
    user_data_dict['mailid'] = user_data['mailid']
    user_data_dict['phone'] = user_data['phone']

    collection_user.insert_one(user_data_dict)
    return 'success'


def login_user(login_details):
    user_data_dict = {}
    user_data_dict['mailid'] = login_details['mailid']
    user_data_dict['password'] = login_details['password']
    
    response = collection_user.find_one(user_data_dict)
    if not response:
        return 'Invalid User id or Password'
    return 'Login Successfully'

def patient_details(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age):

    details = {'Pregnancies':Pregnancies, 'Glucose':Glucose, 'BloodPressure':BloodPressure, 'SkinThickness':SkinThickness, 'Insulin':Insulin,'BMI':BMI, 'DiabetesPedigreeFunction':DiabetesPedigreeFunction,'Age':Age}
                
    collection_prediction.insert_one(details)

    return 'saved successfully'