from flask import Flask,request, render_template
import numpy as np
import pickle

app= Flask(__name__)

@app.route('/')
def box():
    return render_template('dataindividu.html')


@app.route('/predict', methods=['POST'])
def predict():
    final_features = [[np.array([float(x) for x in request.form.values()])]]
    pickled_model = pickle.load(open('finalized_model.pickle', 'rb'))
    predictionsaa = pickled_model.predict(final_features)
    
    return render_template('dataindividu.html', prediction_text='Votre rang devrait etre : {}'.format(predictionsaa[0]))


if __name__=="__main__":
    app.run()