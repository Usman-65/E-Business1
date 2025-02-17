from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Datenbank initialisieren
def init_db():
    with sqlite3.connect("brainstorming.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ideas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL
            )
        """)
        conn.commit()

init_db()

@app.route('/brainstorming', methods=['GET', 'POST'])
def brainstorming():
    if request.method == 'POST':
        idea_text = request.form.get('idea')
        if idea_text.strip():
            with sqlite3.connect("brainstorming.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO ideas (text) VALUES (?)", (idea_text,))
                conn.commit()
        return redirect(url_for('brainstorming'))

    # Gespeicherte Ideen abrufen
    with sqlite3.connect("brainstorming.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, text FROM ideas")
        ideas = cursor.fetchall()

    return render_template('brainstorming.html', ideas=ideas)

@app.route('/delete/<int:idea_id>')
def delete_idea(idea_id):
    with sqlite3.connect("brainstorming.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ideas WHERE id = ?", (idea_id,))
        conn.commit()
    return redirect(url_for('brainstorming'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

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

@app.route('/marketing')
def marketing():
     return render_template('marketing.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/entwicklung')
def entwicklung():
    return render_template('entwicklung.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/design')
def design():
    return render_template('design.html')

if __name__ == '__main__':
    app.run(debug=True)