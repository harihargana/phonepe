# PhonePe Pulse Project 

Overview:
This project entails the following:
1. Load PhonePe Trnsaction, Insurance and User data from a cloned github data repository into Pandas Dataframes
2. Apply required data cleanup and transformations
3. Store the dataframe contents into CSV files
4. Store the CSV contents in a MySQL DB for performing analytics
5. Develop a Streamlit webapp that displays the insights on the gathered data

Python Notebooks:
1. pp_domin: Contains the the domain classes which could be used to load data from github and store data in MySql DB
2. pp_dbinit: Script to create 'phonepe_pulse' DB and its schema.
3. pp_dao: Code to fetch dashboards and other data insights from the MySQL DB
4. pp_webapp: Streamlit web-app to presents the insight - contains geo map and dashboards

Config Files:
1. pp_template.json: A JSON file capturing template for providing DB connection parameters and other GCP config to access the DB
2. india_states.geojson: Geo-JSON file for Indian states that shall be used by the Choropleth mapping library
3. ppstyle.css: CSS file for styling the web-app
   
CSV Data Files:
1. Data collected from github are stored in CSV files.
2. These files are created by code in pp_domain.ipnyb file. These CSV files are used to populate the tables in the MySQL DB.

Other Utility Python Libraries:
1. dbconnect.py: Code to connec to MySQL DB
2. tools.py: Code to load the DB connection config form a JSON file
