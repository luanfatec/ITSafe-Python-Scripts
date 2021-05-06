from flask import Flask, render_template, request, jsonify, session
import random



app = Flask("Adivinhe um numero", static_url_path="", template_folder='web/', static_folder="web/assets/")
app.secret_key = "kljhsflkjopijktgflkrmlkjv9re0tu5jlkhrjgiorhjtgnmfgdgnfjkdhgdnt54g3434r324"

@app.route("/api/comecar_jogo")
def comecar_jogo():
    return render_template("index.html", name_page="Começar jogo")

@app.route("/api/adivinhe_o_numero")
def adivinhe_o_numero():
    return render_template("index.html", name_page="Adivinhe um numero")

@app.route("/api/advinha", methods=["POST"])
def advinha_numero():
    num_sort = random.randint(1, 5)
    num = request.form["number"]
    if (num == str(num_sort)):
        return jsonify(f"Você acertou, o numero sorteador foi {num_sort}", True)
    else:
        return jsonify(f"Você errou, o numero sorteador foi {num_sort}", False)


app.run(host="0.0.0.0", port="8081", debug=True)