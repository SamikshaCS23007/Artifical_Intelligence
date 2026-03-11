from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    fever = request.form['fever']
    cough = request.form['cough']
    fatigue = request.form['fatigue']

    if fever == "1" and cough == "1":
        result = "High chance of Flu"
    elif cough == "1":
        result = "Possible Cold"
    else:
        result = "Possible Allergy"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
    