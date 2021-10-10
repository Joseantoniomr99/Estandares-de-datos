from flask import Flask, render_template
from flask_pymongo import pymongo

client = pymongo.MongoClient("mongodb+srv://Emanuela:1q2w3e@cluster0.roq9n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mongo_db = client.get_database('api_example')
mongo_col = pymongo.collection.Collection(mongo_db, 'api_example')


app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("home.html")

@app.route('/usuarios')
def usuarios():
    usuarios = mongo_col.find()
    return render_template("usuarios.html.j2", users = usuarios, motrar_enlace = False)


if __name__ == '__main__':
    app.run(debug=True)