from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/brainstorming')
def brainstorming():
    return render_template('brainstorming.html')

@app.route('/save-idea', methods=['POST'])
def save_idea():
    # Speichern der Idee aus dem Formular
    idea = request.form.get('idea')
    
    if idea:
        ideas.append(idea)  # Speichern der Idee in der Liste

    # Umleitung zur Brainstorming-Seite
    return redirect(url_for('brainstorming'))

@app.route('/ideas')
def show_ideas():
    # Zeige alle gespeicherten Ideen an
    return render_template('ideas.html', ideas=ideas)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/ueber-uns')
def ueber_uns():
    return render_template('ueber_uns.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Ändere den Port hier, falls 5000 blockiert ist

@app.route('/beratung')
def beratung():
    return render_template('beratung.html')

@app.route('/beratung-kontakt', methods=['POST'])
def beratung_kontakt():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Hier könnten die Daten gespeichert oder per E-Mail versendet werden
    print(f"Neue Beratungsanfrage von {name} ({email}): {message}")

    return redirect(url_for('beratung'))

if __name__ == '__main__':
    app.run(debug=True)