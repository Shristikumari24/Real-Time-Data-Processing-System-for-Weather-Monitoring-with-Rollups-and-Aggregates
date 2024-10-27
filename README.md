# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
This project is a real-time weather monitoring system for major Indian metros, providing summarized insights from the OpenWeatherMap API. It retrieves weather data at set intervals, enabling users to track daily temperature trends, monitor extreme conditions, and receive alerts based on configurable thresholds.
<br>
Project Overview
This project is a real-time data processing system designed to monitor weather conditions across major Indian metros, providing summarized insights through rollups and aggregates. Using data from the OpenWeatherMap API, the system retrieves and processes weather data at regular intervals, enabling users to track daily temperature trends, monitor extreme conditions, and receive alerts when specific thresholds are met.

Features
Real-Time Weather Retrieval: Retrieves weather data every 5 minutes (configurable) for major Indian metros: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
Daily Summary Generation:
Calculates average, maximum, and minimum temperatures for each day.
Identifies the dominant weather condition based on frequency.
Configurable Alerting System:
Allows users to set thresholds for temperature and other conditions.
Alerts are triggered if thresholds are exceeded, displayed in the console or optionally through email.
Visualization: Displays daily summaries, historical weather trends, and triggered alerts for user insights.
Data Source
Data is retrieved from the OpenWeatherMap API, focusing on:

main: Main weather condition (e.g., Rain, Snow, Clear)
temp: Current temperature in Celsius
feels_like: Perceived temperature in Celsius
dt: Timestamp of data update
Setup and Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Set Up API Key:

Sign up for a free API key on OpenWeatherMap.
Add your API key to the configuration file.
Run the Application:

bash
Copy code
python app.py
Usage
Weather Monitoring: Retrieves data at intervals and processes it into daily summaries.
Alerts: Configure alert thresholds for temperature or specific weather conditions.
Visualizations: View daily summaries and alerts for trends and historical data.
Testing
Test Cases:
System Setup: Verifies connection to the OpenWeatherMap API with a valid key.
Data Retrieval: Ensures data is correctly retrieved and parsed.
Temperature Conversion: Tests temperature conversion from Kelvin to Celsius.
Daily Summary Calculation: Confirms accuracy of daily rollups and aggregates.
Alerts: Ensures alerts are triggered when thresholds are breached.
