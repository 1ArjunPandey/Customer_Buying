from flask import Flask, render_template, request, jsonify
import sklearn
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

knn = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/sendd', methods=['GET', 'POST'])
def predict():

    a = (request.form.get('age'))
    b = (request.form.get('salary'))
    c = (request.form.get('out_type'))

    if(a == "" or b == ""):
        return "Tameej se"
    if(c == None):
        return "tameej se"

    a = int(request.form.get('age'))
    b = int(request.form.get('salary'))


    # print(type(a))

    result = knn.predict([[a, b]])[0]


    if(c == "Json_format"):
        bb = "Not Buy"
        if(result == 1):
            bb = "He Will Buy"
        
        ann = {"Age" : a, "Salary": b, "Ans_format" : c, "Result" : bb}
        return jsonify(ann)

    else:

        if(result == 1):
            return render_template('index.html', label = 1)
        else:
            return render_template('index.html', label = -1)
    
    
    # return "<h1>Hey {} good monig you are now in class {} and this is his slid {}</h1>".format(a, b, c)

if __name__ =='__main__':
    app.run(debug=True)

 