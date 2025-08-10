# BAN6420-Final-Project-Flask-Healthcare-Application

## Live App
👉 Run the Web App : https://calistusndubuisiban6420surveyapp.onrender.com/


## Overview
## Overview
This is a Flask web application for collecting and analyzing survey data on income and spending.  
The goal is to support decisions for a healthcare product launch by showing how people allocate their income.


## 🚀 Key Features

- Web form to collect participant details.
- SQLite database for secure storage.
- CSV export for use in Jupyter notebooks.
- Pandas + Matplotlib analysis for:
  - Highest income by age group.
  - Spending breakdown by gender.
- Deployed on Render for public access.


## 📊 Dataset Fields

- Name  
- Age  
- Gender  
- Total Income  
- Utilities Expense  
- Entertainment Expense  
- School Fees  
- Shopping  
- Healthcare  

## ⚙️ Tech Stack

- Python  
- Flask  
- SQLite (local) / PostgreSQL (cloud)  
- Pandas  
- Matplotlib  
- HTML/CSS  
- Render (deployment)
  
## 🛠️ How to Use

git clone <repo-url>
cd BAN6420FinalProjectFlaskHealthcareApplication
pip install -r requirements.txt

## Key dependencies include:
- Flask: Web application framework for data collection.
- matplotlib & pandas: For data visualization and manipulation.
- Render Deployment: The project is deployed on render web services.

##   Run Locally
`python app.py`
App runs at http://127.0.0.1:5000

Run Analysis
Open final_project.ipynb in Jupyter Notebook.
Load the exported CSV and run the analysis cells.

## Access the Flask Web Application
- Once you run app.py file the web application will be accessible at:
`http://127.0.0.1:5000`
- Enter the participant’s details (age, gender, total income, and spending) into the form and submit it. The data is automatically stored in MongoDB.


## Visualize the Data
- The Data Visualization section will load the CSV file and create the following plots:
- A bar chart showing the highest income by age.
- Bar charts showing the spending distribution by gender across categories like utilities, entertainment, school fees, shopping, and healthcare.


## 📁 File Structure
- The project contains the following key files and directories:

- File Structure
- app.py – Flask app and routes

- requirements.txt – Python dependencies

- final_project.ipynb: Jupyter notebook that integrates the Flask app, exports data from SQLlite, and generates visualizations.

- participants_data.csv: The CSV file generated after exporting collected data from the PostgreSQL database.

- Healthcare_Analysis_Presentation.pptx: PowerPoint file summarizing key visual insights for stakeholder presentations.

- Healthcare_Data_Analysis_Final_Project.zip: A compressed file that contains all the necessary project files including notebook, images, CSV, and dependencies.

## 📂 Directories:
- templates/: Contains HTML templates for the Flask web app.

- index.html: Survey form used to collect user input.

- success.html: Optional thank-you page displayed after submission.

- static/: Holds static files such as styles and icons.

- css/style.css: Stylesheet for the HTML survey form.

- favicon.ico: (Optional) Browser tab icon.

- charts/: Directory containing generated visualizations.

- data/ – SQLite database (local)

- *.png: Bar charts and other visuals produced by the Jupyter notebook.

## : 🌐 Deployment Notes
- Local Deployment: Update .env with DB connection string for production.

- Railway PostgreSQL: Connected via pgAdmin for database management.

- Cloud Hosting:

- Update .env with DB connection string for production.

- For Render:
     - Add requirements.txt and optional runtime.txt (Python version).
    - Set start command to gunicorn app:app

## ✅ Conclusion
This project delivers a complete pipeline—from data collection via Flask to data analysis using Jupyter—not only making survey data accessible and analyzable, but also providing a foundation for expanding into predictive analytics or dashboard reporting. The deployment on Render ensures that the application is scalable and accessible from anywhere.



## License
This project is open-source and free to use for educational purposes.

## 👨‍💻 Author
Developed by Calistus Chukwuebuka Ndubuisi
