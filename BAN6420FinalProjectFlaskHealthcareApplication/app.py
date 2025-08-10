from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))  # Use env secret or generate

# Determine DB directory based on environment
if os.environ.get("RENDER"):  # Running on Render
    DB_DIR = "/data"
else:  # Running locally
    DB_DIR = os.path.join(os.path.dirname(__file__), "data")

# Ensure DB directory exists
os.makedirs(DB_DIR, exist_ok=True)

# Full DB path
DB_PATH = os.path.join(DB_DIR, "survey.db")

# SQLite configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(10))
    gender = db.Column(db.String(20), nullable=False)
    total_income = db.Column(db.String(50))
    utilities = db.Column(db.Float, default=0.0)
    entertainment = db.Column(db.Float, default=0.0)
    school_fees = db.Column(db.Float, default=0.0)
    shopping = db.Column(db.Float, default=0.0)
    healthcare = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f"<Participant {self.name}>"

# Create tables if not exist
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        total_income = request.form.get('total_income', '').strip()

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

        if not name or not gender:
            flash("Name and Gender are required fields.", "warning")
            return redirect(url_for('index'))

        new_participant = Participant(
            name=name,
            age=age,
            gender=gender,
            total_income=total_income,
            utilities=utilities,
            entertainment=entertainment,
            school_fees=school_fees,
            shopping=shopping,
            healthcare=healthcare
        )
        try:
            db.session.add(new_participant)
            db.session.commit()
            flash('Data submitted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error saving data: {e}', 'danger')
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/participants')
def participants():
    all_participants = Participant.query.all()
    return {
        "participants": [
            {
                "name": p.name,
                "age": p.age,
                "gender": p.gender,
                "total_income": p.total_income,
                "utilities": p.utilities,
                "entertainment": p.entertainment,
                "school_fees": p.school_fees,
                "shopping": p.shopping,
                "healthcare": p.healthcare
            } for p in all_participants
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
