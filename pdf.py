from flask import Flask, send_file, render_template
import os

# Créer l'application Flask
app = Flask(__name__)

# Route pour afficher la page HTML avec l'iframe
@app.route('/')
def index():
    return render_template('pdf.html')

# Route pour servir le fichier PDF
@app.route('/pdf/<filename>')
def get_pdf(filename):
    try:
        # Le chemin vers le fichier PDF dans le dossier principal de votre projet
        pdf_path = os.path.join(app.root_path, filename)  # Utiliser le chemin absolu
        print(f"Chemin du fichier PDF : {pdf_path}")  # Debugging pour vérifier le chemin
        return send_file(pdf_path, as_attachment=False)
    except FileNotFoundError:
        return "Le fichier PDF n'existe pas.", 404

# Lancer l'application Flask sur un port spécifique
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Spécifiez le port ici
