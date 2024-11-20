from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)  

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #comms)

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route('/histogramme/')
def histogramme():
    return render_template('histogramme.html') #comms)

@app.route('/contact/')
def contact():
  <!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page de Contact</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label, textarea, input, button {
            display: block;
            margin-bottom: 10px;
        }
        #result {
            margin-top: 20px;
            border-top: 1px solid #ccc;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <h2>Page de Contact</h2>
    <form id="contactForm">
        <label for="nom">Nom :</label>
        <input type="text" id="nom" name="nom" required>

        <label for="prenom">Prénom :</label>
        <input type="text" id="prenom" name="prenom" required>

        <label for="message">Message :</label>
        <textarea id="message" name="message" required></textarea>

        <button type="button" onclick="afficherMessage()">Envoyer</button>
    </form>

    <div id="result" style="display:none;">
        <h3>Merci pour votre message !</h3>
        <p><strong>Nom :</strong> <span id="resNom"></span></p>
        <p><strong>Prénom :</strong> <span id="resPrenom"></span></p>
        <p><strong>Message :</strong> <span id="resMessage"></span></p>
    </div>

    <script>
        function afficherMessage() {
            // Récupérer les valeurs des champs
            const nom = document.getElementById('nom').value;
            const prenom = document.getElementById('prenom').value;
            const message = document.getElementById('message').value;

            // Vérifier que tous les champs sont remplis
            if (nom && prenom && message) {
                // Afficher les résultats
                document.getElementById('resNom').innerText = nom;
                document.getElementById('resPrenom').innerText = prenom;
                document.getElementById('resMessage').innerText = message;
                document.getElementById('result').style.display = 'block';

                // Réinitialiser le formulaire
                document.getElementById('contactForm').reset();
            } else {
                alert('Veuillez remplir tous les champs.');
            }
        }
    </script>
</body>
</html>

    return render_template('contact.html') #comms)
  
if __name__ == "__main__":
  app.run(debug=True)
