from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask App
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database Configuration
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT")
DB_NAME = os.getenv("PG_DATABASE")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Home Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        total_income = request.form.get('total_income')

        # Expenses
        utilities = request.form.get('utilities') or 0
        entertainment = request.form.get('entertainment') or 0
        school_fees = request.form.get('school_fees') or 0
        shopping = request.form.get('shopping') or 0
        healthcare = request.form.get('healthcare') or 0

        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute('''
                INSERT INTO users (name, age, gender, total_income, utilities, entertainment, school_fees, shopping, healthcare)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (name, age, gender, total_income, utilities, entertainment, school_fees, shopping, healthcare))

            conn.commit()
            cur.close()
            conn.close()

            flash('Data submitted successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
