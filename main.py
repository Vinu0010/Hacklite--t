from flask import Flask,render_template,request, redirect, url_for, flash
from database import init_db, get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.commit()
        conn.close()
        return "User registered!"
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and user['password'] == password:
            return "Login successful!"
        else:
            flash('Invalid username or password')
    return render_template('login.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

