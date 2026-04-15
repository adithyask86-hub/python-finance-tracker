from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/emi", methods=["POST"])
def calc_emi():
    data = request.json
    P = float(data["principal"])
    r = float(data["rate"]) / 12 / 100
    n = int(data["tenure_months"])
    if r == 0:
        emi = P / n
    else:
        emi = P * r * math.pow(1 + r, n) / (math.pow(1 + r, n) - 1)
    total = emi * n
    interest = total - P
    return jsonify(emi=round(emi, 2), total=round(total, 2), interest=round(interest, 2))

@app.route("/api/sip", methods=["POST"])
def calc_sip():
    data = request.json
    mo = float(data["monthly"])
    r = float(data["rate"]) / 12 / 100
    n = int(data["years"]) * 12
    fv = mo * (math.pow(1 + r, n) - 1) / r * (1 + r)
    invested = mo * n
    returns = fv - invested
    return jsonify(fv=round(fv, 2), invested=round(invested, 2), returns=round(returns, 2))

@app.route("/api/lumpsum", methods=["POST"])
def calc_lumpsum():
    data = request.json
    P = float(data["principal"])
    r = float(data["rate"]) / 100
    t = float(data["years"])
    n = int(data["freq"])
    fv = P * math.pow(1 + r / n, n * t)
    earned = fv - P
    return jsonify(fv=round(fv, 2), principal=P, earned=round(earned, 2))

@app.route("/api/interest", methods=["POST"])
def calc_interest():
    data = request.json
    P = float(data["principal"])
    r = float(data["rate"]) / 100
    t = float(data["years"])
    mode = data["mode"]
    if mode == "SI":
        interest = P * r * t
    else:
        n = int(data.get("freq", 12))
        total = P * math.pow(1 + r / n, n * t)
        interest = total - P
    total = P + interest
    return jsonify(total=round(total, 2), principal=P, interest=round(interest, 2))

if __name__ == "__main__":
    app.run(debug=True, port=5050)
