from flask import Flask, redirect, url_for, request, jsonify, session
import requests

app = Flask("DNSecury API Server", static_url_path="")


"""@app.route('/')
def ola_mundo():
    return "Olá teste"

@app.route("/ola/<name>")
def ola_name(name):
    return f"Olá {name}"

@app.route('/blog/<int:postId>')
def posts(postId):
    return f"Esse é o post {postId}."

@app.route('/teste/')
def test():
    return redirect('http://localhost:1337/')

@app.route('/admin/')
def admin():
    return f'Olá admin'

@app.route("/visite/<name>")
def visite(name):
    return f"Olá visitante {name}"

@app.route('/user/<name>')
def users(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('visite', name=name))"""


# Methods GET and POST

"""@app.route("/get/numeros", methods=["GET"])
def test():
    numero = request.args.get("n")
    nome = request.args.get('name')
    return f"O seu numero é {numero} e seu nome é {nome}"""

app.secret_key = "kljdlkajslkdjslkdjdjlksajdklajdlkjlskadjlksjdlksjldkjslkdj"

@app.route("/api/visitas", methods=["GET"])
def test():
    if session.get('visitas'):
        session["visitas"] += 1
    else:
        session["visitas"] = 1

    return jsonify({
        "visitas":session["visitas"]
    })

"""@app.route("/api/visitas", methods=["POST"])
def test():
    senha = request.form["senha"]
    success = False
    if senha == "1234":
        success = True

    return jsonify({
        "success":success
    })"""


debug = True
app.run(host='0.0.0.0', port=1337, debug=debug)