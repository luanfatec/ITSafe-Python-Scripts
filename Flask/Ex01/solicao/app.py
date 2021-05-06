from flask import Flask, render_template, request, jsonify, session
import random



app = Flask("Adivinhe um numero", static_url_path="", template_folder='web/', static_folder="web/assets/")
app.secret_key = "kljhsflkjopijktgflkrmlkjv9re0tu5jlkhrjgiorhjtgnmfgdgnfjkdhgdnt54g3434r324"

@app.route("/api/comecar_jogo")
def comecar_jogo():
    session["numero"] = random.randint(1, 100)
    session["tentativas"] = 0
    return jsonify({
        "success": True
    })

@app.route("/api/adivinhe_o_numero", methods=["POST"])
def adivinhe_o_numero():
    palpite = int(request.json["palpite"])
    session["tentativas"] += 1
    if palpite > session["numero"]:
        status = "maior"

    elif palpite < session["numero"]:
        status = "menor"

    else:
        status = "Acertou"

    return jsonify({
        "status": status,
        "tentativas": session["tentativas"]
    })



app.run(host="0.0.0.0", port="8081", debug=True)