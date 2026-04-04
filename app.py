from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/predict', methods=['POST'])
def predict():

    fever = int(request.form.get('fever', 0))
    cough = int(request.form.get('cough', 0))
    fatigue = int(request.form.get('fatigue', 0))
    headache = int(request.form.get('headache', 0))
    throat = int(request.form.get('throat', 0))

    # 👉 NEW CONDITION (IMPORTANT 🔥)
    if fever == 0 and cough == 0 and fatigue == 0 and headache == 0 and throat == 0:
        return render_template("result.html",
                               flu=0,
                               cold=0,
                               allergy=0,
                               final="✅ You are Fit and Fine! No disease detected.")

    # Probability logic
    flu = fever*0.4 + cough*0.3 + fatigue*0.2 + headache*0.2
    cold = cough*0.5 + throat*0.3 + headache*0.2
    allergy = throat*0.4 + fatigue*0.2

    flu_p = int(flu * 100)
    cold_p = int(cold * 100)
    allergy_p = int(allergy * 100)

    # Final result
    if flu_p >= cold_p and flu_p >= allergy_p:
        final = "⚠️ High chance of Flu. Take rest & consult doctor."
    elif cold_p >= allergy_p:
        final = "🤧 You may have a Cold. Stay hydrated."
    else:
        final = "🌿 Possible Allergy. Avoid dust & triggers."

    return render_template("result.html",
                           flu=flu_p,
                           cold=cold_p,
                           allergy=allergy_p,
                           final=final)

if __name__ == "__main__":
    app.run(debug=True)