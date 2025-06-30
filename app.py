from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient, errors
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))  # Use env secret or generate

# MongoDB config
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = os.getenv("MONGO_DBNAME", "survey_db")

# Initialize MongoDB client with error handling
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client[MONGO_DBNAME]
    participants_collection = db.participants    # Ping DB to confirm connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully.")
except errors.ServerSelectionTimeoutError as err:
    print(f"Failed to connect to MongoDB: {err}")
    participants_collection = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if participants_collection is None:
        flash("Database connection is not available.", "danger")
        return render_template('index.html')

    if request.method == 'POST':
        # Collect form data safely with validation
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        total_income = request.form.get('total_income', '').strip()

        # Convert numeric fields safely, default to 0 if invalid
        def to_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return 0.0

        utilities = to_float(request.form.get('utilities'))
        entertainment = to_float(request.form.get('entertainment'))
        school_fees = to_float(request.form.get('school_fees'))
        shopping = to_float(request.form.get('shopping'))
        healthcare = to_float(request.form.get('healthcare'))

        # Basic validation: name and gender are required
        if not name or not gender:
            flash("Name and Gender are required fields.", "warning")
            return redirect(url_for('index'))

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
            flash(f'Error saving data: {e}', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

# Optional: View all participants (for admin/debug)
@app.route('/participants')
def participants():
    if participants_collection is None:
        return "Database connection is not available.", 500
    all_participants = list(participants_collection.find({}, {"_id": 0}))
    return {"participants": all_participants}

if __name__ == "__main__":
    # Disable debug in production!
    app.run(host="0.0.0.0", port=10000, debug=True
