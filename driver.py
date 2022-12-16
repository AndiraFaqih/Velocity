import numpy as np
import pickle
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    loaded_model = pickle.load(open("./model/model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        speaking_score = request.form['Speaking']
        writing_score = request.form['Writing']
        listening_score = request.form['Listening']
        reading_score = request.form['Reading']

        to_predict_list = list(map(float, [speaking_score, writing_score, listening_score, reading_score]))
        result = ValuePredictor(to_predict_list)

        if float(result) == 0:
            if float (speaking_score) < 0.31 and float (writing_score) < 0.39 and float (listening_score) < 0.39 and float (reading_score) < 0.39:
                prediction = 'BASIC'         
                suggestion = 'You English skills are deficient. You can start by talking to yourself in the mirror or by talking to a friend in English. You can also start by writing a diary in English or by writing a story in English. You can also start by listening to music in English or by listening to a podcast in English. You can also start by reading a book in English or by reading a news article in English.'

            elif float (writing_score) < 0.45 and float (reading_score) < 0.45:
                prediction = 'BASIC'
                suggestion = 'You need to improve your writing and reading skill. You can start by writing a diary in English or by writing a story in English. You can also start by reading a book in English or by reading a news article in English.'

            elif float (speaking_score) < 0.31:
                prediction = 'BASIC'
                suggestion = 'You need to improve your speaking skill. You can start by talking to yourself in the mirror or by talking to a friend in English.'

            elif float (writing_score) < 0.39:
                prediction = 'BASIC'
                suggestion = 'You need to improve your writing skill. You can start by writing a diary in English or by writing a story in English.'

            elif float (listening_score) < 0.39:
                prediction = 'BASIC'
                suggestion = 'You need to improve your listening skill. You can start by listening to music in English or by listening to a podcast in English.'

            elif float (reading_score) < 0.39:
                prediction = 'BASIC'
                suggestion = 'You need to improve your reading skill. You can start by reading a book in English or by reading a news article in English.'

        elif float(result) == 1:
            if ((float (speaking_score) > 0.45 and float (speaking_score) < 0.65) and (float (writing_score) > 0.45 and float (writing_score) < 0.65) and (float (listening_score) > 0.45 and float (listening_score) < 0.65) and (float (reading_score) > 0.45 and float (reading_score) < 0.65)):
                prediction = 'INTERMEDIATE'         
                suggestion = 'Your English skills are good enough. You can still improve it by practicing more until you reach the advanced level.'

            elif (float (speaking_score) < 0.45 and float (writing_score) < 0.45):
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your speaking and writing skill. You can start by talking to yourself in the mirror or by talking to a friend in English. You can also start by writing a diary in English or by writing a story in English.'
            
            elif float (speaking_score) < 0.45 and float (listening_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your speaking and listening skill. You can start by talking to yourself in the mirror or by talking to a friend in English. You can also start by listening to music in English or by listening to a podcast in English.'

            elif float (speaking_score) < 0.45 and float (reading_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your speaking and reading skill. You can start by talking to yourself in the mirror or by talking to a friend in English. You can also start by reading a book in English or by reading a news article in English.'

            elif float (writing_score) < 0.45 and float (listening_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your writing and listening skill. You can start by writing a diary in English or by writing a story in English. You can also start by listening to music in English or by listening to a podcast in English.'

            elif float (writing_score) < 0.45 and float (reading_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your writing and reading skill. You can start by writing a diary in English or by writing a story in English. You can also start by reading a book in English or by reading a news article in English.'

            elif float (listening_score) < 0.45 and float (reading_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your listening and reading skill. You can start by listening to music in English or by listening to a podcast in English. You can also start by reading a book in English or by reading a news article in English.'

            elif float (speaking_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your speaking skill. You can start by talking to yourself in the mirror or by talking to a friend in English.'

            elif float (writing_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your writing skill. You can start by writing a diary in English or by writing a story in English.'

            # elif (float (writing_score) > 0.45 and float (writing_score) < 0.65):  
            #     prediction = 'INTERMEDIATE'
            #     suggestion = 'Your writing skill is good enough. You can start by writing a diary in English or by writing a story to improve your English writing skill.'
            
            elif float (listening_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your listening skill. You can start by listening to music in English or by listening to a podcast in English.'

            # elif (float (listening_score) > 0.45 and float (listening_score) < 0.65):
            #     prediction = 'INTERMEDIATE'
            #     suggestion = 'Your listening skill is good enough. You can start by listening to music in English or by listening to a podcast to improve your English listening skill.'
            
            elif float (reading_score) < 0.45:
                prediction = 'INTERMEDIATE'
                suggestion = 'You need to improve your reading skill. You can start by reading a book in English or by reading a news article in English.'

            # elif (float (reading_score) > 0.45 and float (reading_score) < 0.65):
            #     prediction = 'INTERMEDIATE'
            #     suggestion = 'Your reading skill is good enough. You can start by reading a book in English or by reading a news article to improve your English reading skill.'
            # else:
            #     prediction = 'INTERMEDIATE'
            #     suggestion = 'E'
            # suggestion for intermediate

        elif float(result) == 2:
            if float (speaking_score) < 0.45:
                prediction = 'ADVANCED'
                suggestion = 'You need to improve your speaking skill. You can start by talking to yourself in the mirror or by talking to a friend in English.'

            elif (float (speaking_score) > 0.45 and float (speaking_score) < 0.59):
                prediction = 'ADVANCED'
                suggestion = 'Your speaking skill is good enough. You can start by talking to yourself in the mirror or by talking to a friend to improve your English speaking skill.'

            elif float (writing_score) < 0.45:
                prediction = 'ADVANCED'
                suggestion = 'You need to improve your writing skill. You can start by writing a diary in English or by writing a story in English.'
            
            elif (float (writing_score) > 0.45 and float (writing_score) < 0.65):
                prediction = 'ADVANCED'
                suggestion = 'Your writing skill is good enough. You can start by writing a diary in English or by writing a story to improve your English writing skill.'
            
            elif float (listening_score) < 0.45:
                prediction = 'ADVANCED'
                suggestion = 'You need to improve your listening skill. You can start by listening to music in English or by listening to a podcast in English.'
            
            elif (float (listening_score) > 0.45 and float (listening_score) < 0.65):
                prediction = 'ADVANCED'
                suggestion = 'Your listening skill is good enough. You can start by listening to music in English or by listening to a podcast to improve your English listening skill.'

            elif float (reading_score) < 0.45:
                prediction = 'ADVANCED'
                suggestion = 'You need to improve your reading skill. You can start by reading a book in English or by reading a news article in English.'
            
            elif (float (reading_score) > 0.45 and float (reading_score) < 0.65):
                prediction = 'ADVANCED'
                suggestion = 'Your reading skill is good enough. You can start by reading a book in English or by reading a news article to improve your English reading skill.'
            
            elif (float (listening_score) > 0.65 and float (writing_score) > 0.65 and float (speaking_score) > 0.65 and float (reading_score) > 0.65):
                prediction = 'ADVANCED'
                suggestion = 'Your English skill amazing. Keep it up!'

        return render_template("result.html", suggestion=suggestion, prediction=prediction, name=name)
        


if __name__ == '__main__':
    app.run(debug=True)