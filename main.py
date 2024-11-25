# This is a sample Python script.
import database
import parser
import scraper
import json

import viewer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Scrape data
    scraped_data: json = scraper.scrape()
    print(scraped_data)

    ## PART 1
    # Extract required datasets
    weather_station_measurement, weather_stations = parser.parse_json(scraped_data)
    print(weather_station_measurement)
    print(weather_stations)

    # Create database
    conn = database.start()

    # Insert data in database
    database.add_weather_stations(conn, weather_stations)
    database.add_weather_station_measurements(conn, weather_station_measurement)


    ## PART 2
    highest_temp_station = viewer.get_highest_temperature_station(conn)
    print("Q5 Which weather station recorded the highest temperature? = ", highest_temp_station)


    conn.close()

