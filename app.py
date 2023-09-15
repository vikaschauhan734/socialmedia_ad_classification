from flask import Flask, render_template, request, redirect, url_for
import requests
import numpy as np
import pickle
app= Flask(__name__)
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/true')
def true():
    return render_template('true.html')

@app.route('/false')
def false():
    return render_template('false.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        age=int(request.form['age'])
        estimated_salary=float(request.form['estimatedsalary'])
        scaled = scaler.transform(np.array([age,estimated_salary]).reshape(1,2))
        prediction = model.predict(scaled)[0]
        if prediction == 0:
            output = "false"
        else:
            output = "true"
    return redirect(url_for(output))


if __name__=='__main__':
    app.run(debug=True)