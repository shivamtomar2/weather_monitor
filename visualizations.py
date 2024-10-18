import matplotlib.pyplot as plt
import datetime
import time

# Sample data generation for demonstration purposes
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# Function to plot daily weather summary
def plot_daily_summary(dates, avg_temps, max_temps, min_temps):
    plt.figure(figsize=(10, 6))

    # Plot the average, max, and min temperatures
    plt.plot(dates, avg_temps, label='Avg Temp (°C)', marker='o', color='blue')
    plt.plot(dates, max_temps, label='Max Temp (°C)', marker='o', color='red')
    plt.plot(dates, min_temps, label='Min Temp (°C)', marker='o', color='green')

    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Weather Summary')

    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to plot historical temperature trends
def plot_historical_trends(dates, temperatures, city):
    plt.figure(figsize=(10, 6))

    plt.plot(dates, temperatures, marker='o', linestyle='-', color='purple', label='Temperature (°C)')
    
    plt.title(f'Historical Temperature Trends in {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Function to plot alerts triggered for cities
def plot_alerts(cities, alert_counts):
    plt.figure(figsize=(8, 5))

    plt.bar(cities, alert_counts, color='orange')

    plt.title('Number of Alerts Triggered by City')
    plt.xlabel('City')
    plt.ylabel('Alert Count')

    plt.tight_layout()
    plt.show()

# Main function to simulate weather data and call visualizations
def main():
    # Initialize mock data
    dates = [datetime.date.today() - datetime.timedelta(days=i) for i in range(7)]
    avg_temps = [30, 31, 32, 33, 30, 29, 28]
    max_temps = [35, 36, 37, 38, 36, 35, 33]
    min_temps = [25, 26, 27, 27, 26, 25, 24]

    # Plot the daily weather summary
    plot_daily_summary(dates, avg_temps, max_temps, min_temps)

    # Historical trend for one city
    temperatures = [30 + i for i in range(10)]
    plot_historical_trends(dates, temperatures, 'Delhi')

    # Example alerts for multiple cities
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    alert_counts = [3, 1, 2, 0, 1, 5]
    plot_alerts(cities, alert_counts)

    # You can add a loop to keep fetching data in real-time if required
    # while True:
    #     # Fetch or process real-time data
    #     time.sleep(300)  # Wait for 5 minutes before fetching new data

if __name__ == "__main__":
    main()
