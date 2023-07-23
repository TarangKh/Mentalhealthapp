import pickle
import numpy as np
from flask import Flask,request, url_for, redirect, render_template

app = Flask(__name__)

model=pickle.load(open('modell.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[int_features]
    print(int_features) 

    print(final)
    prediction=model.predict(final)
    output='{0}'.format(prediction)

    if output<str(1):
        return render_template('index.html',pred='Your Country has good Mental Health.\n DALY is {}'.format(output),bhai=" Itni Khushi")
    else:
        return render_template('index.html',pred='Your Country has not Good mental Health.\n  DALY is {}'.format(output),bhai=" Utha Le Re BABA")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port = 8000)
