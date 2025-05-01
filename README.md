# BAN6420-Final-Project-Flask-Healthcare-Application


## Overview
The Flask Healthcare Application is a survey tool designed to collect data on participants' income and spending patterns for a healthcare product launch. The project involves web development with Flask, data storage with Postgres, data processing using Python, and visualizations within a Jupyter notebook. The project is intended to gather insights on how participants allocate their income across various expense categories.


## 🚀 Key Features

- **Flask Web App**: Clean interface to collect participant information.
- **PostgreSQL Integration**: Stores form data securely using Railway-hosted PostgreSQL.
- **Jupyter Notebook**: For exporting and visualizing survey data.
- **Matplotlib + Pandas**: To generate insights like:
  - Age groups with highest income
  - Gender distribution in spending categories
- **Deployment Ready**: on Render.

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

## ⚙️ Technologies Used

- **Python**
- **Flask**
- **PostgreSQL** (Railway + pgAdmin)
- **Pandas**, **Matplotlib**
- **Jupyter Notebook**
- **HTML/CSS**
- **Render** / **AWS EC2** (for deployment)

## 🛠️ How to Use

### 1. 🔧 Setup and Installation

Clone the repo and install dependencies:

pip install -r requirements.txt

## Key dependencies include:
- Flask: Web application framework for data collection.
- Railway + pgAdmin: For postgreSQL integration.
- matplotlib & pandas: For data visualization and manipulation.
- Render Deployment: The project is deployed on render web services.

##  Running the Project
Step 1: Run the Jupyter Notebook
Open `final_project.ipynb` in Jupyter Notebook.

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

- app.py: Main Flask application script used to launch the survey form and handle data submission.

- .env: Stores sensitive environment variables (e.g., PostgreSQL credentials).

- requirements.txt: Lists all the Python dependencies required for the project.

- final_project.ipynb: Jupyter notebook that integrates the Flask app, exports data from PostgreSQL, and generates visualizations.

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

- *.png: Bar charts and other visuals produced by the Jupyter notebook.

## : 🌐 Deployment Notes
- Local Deployment: Ensure PostgreSQL is running and accessible via .env.

- Railway PostgreSQL: Connected via pgAdmin for database management.

- Cloud Hosting:

- On Render or AWS EC2, update your .env file with public DB connection strings.

- Make sure port 5000 is open and Flask runs in production mode (host='0.0.0.0').


## ✅ Conclusion
This project delivers a complete pipeline—from data collection via Flask to data analysis using Jupyter—not only making survey data accessible and analyzable, but also providing a foundation for expanding into predictive analytics or dashboard reporting. The deployment on Render ensures that the application is scalable and accessible from anywhere.



## License
This project is open-source and free to use for educational purposes.

## 👨‍💻 Author
Developed by Calistus Chukwuebuka Ndubuisi
