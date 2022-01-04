from flask import Flask,request, render_template
import pickle
from threading import Timer
import webbrowser
from sklearn import preprocessing
import pandas as pd

app= Flask(__name__)

app_port = 5551

@app.route('/', methods=['POST', "GET"])
def box():
    if (request.method=="GET"):
        return render_template('data_forms_page.html')
    return predict()

def open_browser():
      webbrowser.open_new(f'http://127.0.0.1:{app_port}/')


def predict():
    #Get the data
    final_features = [[float(x) for x in request.form.values()]]
    
    #We need to normalize the data now
    try:
        scaler = pickle.load(open('scaler.pkl', 'rb'))
        data_norm = scaler.transform(final_features)
    except:
        df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00272/SkillCraft1_Dataset.csv")

        df.Age = df.Age.replace("?", df[df.Age != '?'].Age.median())

        df.HoursPerWeek = df.HoursPerWeek.replace("?", df[df.HoursPerWeek != '?'][df.LeagueIndex == 7].HoursPerWeek.median())

        df.TotalHours = df.TotalHours.replace("?", df[df.TotalHours != '?'][df.LeagueIndex == 7].TotalHours.median())

        df[['Age', 'HoursPerWeek', 'TotalHours']] = df[['Age', 'HoursPerWeek', 'TotalHours']].astype(int)

        scaler = preprocessing.MinMaxScaler()
        scaler.fit_transform(df)
        data_norm = scaler.transform(final_features)
    
    
    #Load the model and predict
    pred_model = pickle.load(open('final_model.pickle', 'rb'))
    predictions = pred_model.predict(data_norm)
    
    
    
    return render_template('data_forms_page.html', prediction_text='Votre rang devrait etre : {}'.
                           format(["Bronze", "Silver", "Gold", "Platinium", "Diamond", "Master", "GrandMaster", "Professional"][predictions[0] - 1]))

if __name__=="__main__":
    Timer(1, open_browser())
    app.run(host="127.0.0.1", port=app_port, debug=False)