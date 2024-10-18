# Real-Time Data Processing System for Weather Monitoring

## Overview
This project is designed to monitor weather conditions in real time and provide summarized insights using rollups and aggregates.

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment.
4. Install dependencies using `pip install -r requirements.txt`.
5. Obtain your API key from OpenWeatherMap and replace `your_api_key` in the code.
6. Run the application with `python src/main.py`.

## Dependencies
- requests
- matplotlib
- sqlite3

## Design Choices
- Utilized OpenWeatherMap API for real-time data.
- Implemented SQLite for persistent storage.

## Usage Instructions
- The application retrieves weather data every 5 minutes for specified cities.
