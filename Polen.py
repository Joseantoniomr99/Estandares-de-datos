from flask import Flask, render_template, redirect, request
from flask_pymongo import pymongo

client = pymongo.MongoClient("mongodb+srv://Emanuela:1q2w3e@cluster0.roq9n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mongo_db = client.get_database('AIRE')
mongo_col = pymongo.collection.Collection(mongo_db, 'coleccionPolen')


app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("home.html")
   

@app.route('/samples')
def samples():
    samples = mongo_col.find()
    return render_template("samples.html.j2", users = samples, mostrar_enlace = True)

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template("form.html.j2")
    elif request.method == 'POST':
        date = request.form['date']
        Alnus = request.form['Alnus']
        Betulus = request.form['Betulus']
        Taxus = request.form['Taxus']
        Fraxinus = request.form['Fraxinus']
        Poaceae = request.form['Poaceae']
        Quercus = request.form['Quercus']
        Ulmus = request.form['Ulmus']
        Urtica = request.form['Urtica']
        usuario = {"date" : date, "Alnus": Alnus, "Betulus" : Betulus, "Taxus": Taxus, "Fraxinus": Fraxinus, "Poaceae": Poaceae, "Quercus": Quercus, "Ulmus": Ulmus, "Urtica": Urtica}
        mongo_col.insert_one(usuario)
        return redirect("/samples")

if __name__ == '__main__':
    app.run(debug=True)