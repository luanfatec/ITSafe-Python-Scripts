from flask import Flask

app = Flask("Page", static_folder="/")

debug = True
app.run(host='0.0.0.0', port=1337, debug=debug)