# BAN6420-Final-Project-Flask-Healthcare-Application


## Overview
The Flask Healthcare Application is a survey tool designed to collect data on participants' income and spending patterns for a healthcare product launch. The project involves web development with Flask, data storage with MongoDB, data processing using Python, and visualizations within a Jupyter notebook. The project is intended to gather insights on how participants allocate their income across various expense categories.

### The notebook includes:
- A Flask-based web application for data collection.
- Data processing to export the collected data to CSV from MongoDB.
- Data visualizations to analyze the collected data, including:(Ages with the highest income. Gender distribution across various spending categories.)

## Key Features:
- Flask Web Application: Collects participant data such as age, gender, income, and spending across categories like utilities, entertainment, school fees, shopping, and healthcare.
- MongoDB Integration: Stores the participant data.
- Data Processing: Exports the stored data to a CSV file.
- Data Visualization: Displays visual insights on income and spending using Matplotlib.
- Integrated in Jupyter Notebook: All functionalities are available in one `ipynb` file.
- AWS EC2 Deployment: The Flask web app is deployed and accessible via AWS EC2.



## How to Use
### 1. Setup and Installation
Install Dependencies
All dependencies required for this project are listed in the requirements.txt file. Run the following command to install them:

`pip install -r requirements.txt`

### Key dependencies include:
- Flask: Web application framework for data collection.
- pymongo: For MongoDB integration.
- matplotlib & pandas: For data visualization and manipulation.
- EC2 Deployment: The project is deployed using AWS EC2.

### 2. Running the Project
Step 1: Run the Jupyter Notebook
Open `final_project.ipynb` in Jupyter Notebook.

### The notebook is organized into the following sections:
### Flask Web Application:
- This section starts the Flask server, allowing you to collect data from participants using a simple web form.
- The Flask app runs in a separate thread, so you can still work within the notebook while the app is live.
### Data Processing:
- After collecting data, this section allows you to export the data from MongoDB into a CSV file called `participants_data.csv`.
Data Visualization:
- This section loads the CSV data and generates visualizations such as:
- Highest income by age.
- Gender distribution across spending categories.

### Step 2: Access the Flask Web Application
- Once you run the Flask section of the notebook, the web application will be accessible at:
`http://127.0.0.1:5000`
- Enter the participant’s details (age, gender, total income, and spending) into the form and submit it. The data is automatically stored in MongoDB.

### Step 3: Process the Data
- After collecting enough data, run the Data Processing section of the notebook to export the MongoDB data into a CSV file (`participants_data.csv`).

### Step 4: Visualize the Data
- The Data Visualization section will load the CSV file and create the following plots:
- A bar chart showing the highest income by age.
- Bar charts showing the spending distribution by gender across categories like utilities, entertainment, school fees, shopping, and healthcare.

### Step 5: Deployment on AWS EC2
- You can deploy the Flask app on AWS EC2 for remote accessibility. Ensure that:
- Your EC2 instance is set up with proper security groups to allow HTTP/HTTPS traffic.
- Flask is running on the instance, and MongoDB is accessible to your EC2 environment.
- The Flask app can be accessed via the EC2 public IP.


## File Structure
The project contains the following key files and directories:
- `Healthcare_Data_Analysis_Final_Project.zip`: The compressed file containing all necessary project files, including the Jupyter notebook, CSV, images, and dependencies.
- `final_project.ipynb`: The Jupyter notebook that integrates the Flask app, data processing, and visualizations.
- `participants_data.csv`: The exported CSV file generated after data processing (this file will be created after running the notebook).
- `charts`/ (directory): Contains PNG images of the charts generated from the visualizations. These images are automatically saved when running the Jupyter notebook. They can be used in reports or presentations.
- `Healthcare_Analysis_Presentation.pptx`: The PowerPoint file generated from the data visualizations, containing charts for client presentations.

# Conclusion
This project provides a streamlined solution for collecting, processing, and analyzing participant data. By integrating everything into a single Jupyter notebook, it simplifies the process and makes it easy to run, visualize, and share insights. The Flask application provides a user-friendly interface for data collection, while the notebook handles the data export and visual analysis. The deployment on AWS EC2 ensures that the application is scalable and accessible from anywhere.

## License
This project is open-source and free to use for educational purposes.


## Author
Developed by Calistus Chukwuebuka Ndubuisi.
