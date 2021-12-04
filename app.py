from flask import Flask, render_template, request
import predict

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sub", methods = ['POST'])
def sub():
    if request.method == 'POST':
        n = request.form['age']
        m = request.form['gender']
        
    return render_template("index.html", genre = predict.genre_predictor(n,m), accuracy = predict.accuracy_score())
    



if __name__ == '__main__':
    app.run(debug=True)