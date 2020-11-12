import csv
from flask import Flask, render_template, request
import ""

# Si le chemin demandé est /Accueil
app = Flask(__name__)
@app.route('/page accueil minecraft')
@app.route('/')
def Accueil():
    return render_template('page accueil minecraft.html')

# Si le chemin demandé est /sondage
@app.route('/page des sondages', methods=['GET', 'POST'])
def Sondage():
    
    # S'il s'agit d'une requête POST
    if request.method == 'POST':
        valeurpython = request.values["valrequete"]
        
        return render_template('page des sondages.html' )
    # Sinon (s'il s'agit d'une requête GET)
    else:
        return render_template('page des sondages.html')


# Si le chemin demandé est /records
@app.route('/records')
def records():
    return render_template('records.html')


if __name__ == '__main__':
    app.run(debug=True)

