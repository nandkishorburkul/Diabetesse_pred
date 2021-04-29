from flask import Flask,jsonify,request,render_template
import config
import test_model
import details_db
app=Flask(__name__)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        data = request.form 
        response = details_db.register_user(data)

    return jsonify({'msg':response})

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        data = request.form 
        response = details_db.login_user(data)

        return jsonify({'msg':response})
    return jsonify({'msg':'Unsuccessful'})

@app.route('/col_nms_')
def col_nms_():
    response = jsonify({'Name_of_column':test_model.Diabetes().col_names()})

    return response

@app.route('/outcome_pred',methods=['POST','GET'])
def outcome_pred():
    if request.method == 'POST':
        data=request.form
        Pregnancies  = int(data['Pregnancies'])
        Glucose      =int(data['Glucose'])
        BloodPressure=int(data['BloodPressure'])
        SkinThickness=int(data['SkinThickness'])
        Insulin      =int(data['Insulin'])
        BMI          =float(data['BMI'])
        DiabetesPedigreeFunction=float(data['DiabetesPedigreeFunction'])
        Age =int(data['Age'])
        prediction =test_model.Diabetes().outcome_pred(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age)
        details_db.patient_details(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age)

        return "The Result of Diabetes ips {} ".format(prediction)
    return "Fail Outcome_pred"
if __name__=='__main__':
    print('Starting Python Flask Server to Find Diabetes of patient..')
    app.run(host='0.0.0.0',port=config.PORT)