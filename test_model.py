import pickle
import json
import numpy as np
logistic=pickle.load(open('Logistic_model.pickle','rb'))


class Diabetes():
    def col_names(self):
        with open('Name_of_column.json','r') as f:
            locations_list = json.load(f)['columns_name']
        return locations_list
    
    def outcome_pred(self,Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age):
        # logistic=pickle.load(open('Logistic_model.pickle','rb'))
        with open("Name_of_column.json", "r") as f:
            column_json=json.load(f)['columns_name']
            location_list=column_json
        
        x=np.zeros(len(location_list))
        x[0]=Pregnancies
        x[1]=Glucose
        x[2]=BloodPressure
        x[3]=SkinThickness
        x[4]=Insulin
        x[5]=float(BMI)
        x[6]=float(DiabetesPedigreeFunction)
        x[7]=Age
        return logistic.predict([x])[0]

if __name__ == "__main__":
    d=Diabetes()
    outcome=d.outcome_pred(7,150,78,29,126,35.2,0.692,54)
    print("the outcome is",outcome)
     
