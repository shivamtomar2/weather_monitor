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


<img width="653" alt="Screenshot 2024-10-18 at 3 47 45 PM" src="https://github.com/user-attachments/assets/ecb21e5a-e380-42f6-b1f6-9d4a0bf8f085">
<img width="1186" alt="Screenshot 2024-10-18 at 3 52 41 PM" src="https://github.com/user-attachments/assets/663239e4-65ba-42fd-af68-cba1370c4a54">
