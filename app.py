from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask App
app = Flask(__name__)
app.secret_key = os.urandom(24)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")

# Initialize MongoDB Client
client = MongoClient(MONGO_URI)
db = client[MONGO_DBNAME]
participants_collection = db.participants  # ✅ Correct usage

# Home Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        total_income = request.form.get('total_income')

        # Expenses
        utilities = float(request.form.get('utilities') or 0)
        entertainment = float(request.form.get('entertainment') or 0)
        school_fees = float(request.form.get('school_fees') or 0)
        shopping = float(request.form.get('shopping') or 0)
        healthcare = float(request.form.get('healthcare') or 0)

        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "total_income": total_income,
            "utilities": utilities,
            "entertainment": entertainment,
            "school_fees": school_fees,
            "shopping": shopping,
            "healthcare": healthcare
        }

        try:
            participants_collection.insert_one(data)
            flash('Data submitted successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
