from flask import Flask, render_template, request, redirect, jsonify, url_for 
import pickle
import numpy as np
import pandas as pd 

model = pickle.load(open('rfc.pkl', 'rb'))
app = Flask(__name__)
app.config['SECRET_KEY'] = '78fabf5575579bcb76daea4131c8b06f8d41462b08850e3f'

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about/")
def about_page():
    return render_template("about.html")

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = print(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])


@app.route("/result/", methods=['POST', 'GET'])
def potability_calc():
    if request.method == "POST":
        ph = request.form["ph"]
        hard = request.form["hardness"]
        solid = request.form["solids"]
        chamine = request.form["chloramines"]
        sulfate = request.form["sulfate"]
        cond = request.form["conductivity"]
        oc = request.form["oc"]
        thm = request.form["trihalomethanes"]
        turb = request.form["turbidity"]
        
        context = {"ph": ph, "hard": hard, "solid": solid, "chamine": chamine, "sulfate": sulfate, "cond": cond, "oc": oc, "thm": thm, "turb": turb}

        return render_template("results.html", context=context)
    else:
        return redirect("/")
        
    


if  __name__ == "__main__":
    app.run(debug=True)
