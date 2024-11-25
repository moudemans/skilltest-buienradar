# This is a sample Python script.
import database
import parser
import scraper
import json



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Scrape data
    scraped_data: json = scraper.scrape()
    print(scraped_data)

    # Extract required datasets
    weather_station_measurement, weather_stations = parser.parse_json(scraped_data)
    print(weather_station_measurement)
    print(weather_stations)

    # Create database
    conn = database.start()

    # Insert data in database
    database.add_weather_stations(conn, weather_stations)
    database.add_weather_station_measurements(conn, weather_station_measurement)

    conn.close()

