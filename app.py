import string, random, sqlite3
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
DB = 'urls.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS urls (short TEXT PRIMARY KEY, full TEXT)')

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        full_url = request.form['url']
        short_id = generate_short_id()
        with sqlite3.connect(DB) as conn:
            conn.execute('INSERT INTO urls (short, full) VALUES (?, ?)', (short_id, full_url))
        return render_template('result.html', short_url=request.host_url + short_id)
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_url(short_id):
    with sqlite3.connect(DB) as conn:
        cursor = conn.execute('SELECT full FROM urls WHERE short = ?', (short_id,))
        result = cursor.fetchone()
        if result:
            return redirect(result[0])
    return 'URL not found!', 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
