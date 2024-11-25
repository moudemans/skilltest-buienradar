# This is a sample Python script.
import database
import parser
import scraper
import json

import viewer

# Press the green button in the gutter to run the script.
def answer_questions(conn):
    ## PART 2
    highest_temp_station = viewer.get_highest_temperature_station(conn)
    print("Q5 Which weather station recorded the highest temperature? = ", highest_temp_station)
    avg_temp = viewer.get_average_temp(conn)
    print("Q6 What is the average temperature? = ", avg_temp)

    highest_temp_diff_station = viewer.get_max_temp_deviation(conn)
    print("Q7 What is the station with the biggest difference between feel temperature and the actual temperature? = ", highest_temp_diff_station)

    station_in_north_sea = viewer.get_station_in_region(conn, "Noordzee")
    print("Q8 Which weather station is located in the North Sea? = ", station_in_north_sea)


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

    answer_questions(conn)




    conn.close()

