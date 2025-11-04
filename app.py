from flask import Flask, render_template, request, redirect, url_for
from client_dao import ClientDAO
from client import Client

app = Flask(__name__)
dao = ClientDAO()

@app.route('/')
def index():
    clients = dao.get_all_clients()
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        nom = request.form['nom']
        age = int(request.form['age'])
        niveau = request.form['niveau']
        client = Client(nom, age, niveau)
        dao.add_client(client)
        return redirect(url_for('index'))
    return render_template('add_client.html')

if __name__ == '__main__':
    app.run(debug=True)
