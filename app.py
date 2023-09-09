from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/sendd', methods=['GET', 'POST'])
def predict():

    a = request.form.get('age')
    b = request.form.get('salary')
    c = request.form.get('out_type')

    return "<h1>Hey {} good monig you are now in class {} and this is his slid {}</h1>".format(a, b, c)

if __name__ =='__main__':
    app.run(debug=True)

 