import json
import uuid


# Function extracts relevant datapoints from provided json argument.
# # - scraped_data
#     - actual
#         - stationmeasurements []
#             {
#               measurementid 
#               timestamp
#               temperature
#               groundtemperature
#               feeltemperature
#               windgusts
#               windspeedBft
#               humidity
#               precipitation
#               sunpower
#               stationid
#               stationname
#               lat
#               lon
#               regio
#             },
#             ...

# TODO: Create data objects from extracted values
def parse_json(scraped_data: json):
    weather_station_measurements = []
    weather_stations = {}

    # weather station measurement:
    # scraped_data -> actual -> stationmeasurements[] = List of dictionaries
    weather_station_measurements_json = scraped_data["actual"]["stationmeasurements"]
    for measurement in weather_station_measurements_json:
        tmp_holder = {}

        # TODO: create measurement id in table? or have a central counter..
        tmp_holder["measurementid"] = uuid.uuid4()

        # TODO: What to do with missing values? , there are None values
        tmp_holder["timestamp"] = measurement.get("timestamp")
        tmp_holder["temperature"] = measurement.get("temperature")
        tmp_holder["groundtemperature"] = measurement.get("groundtemperature")
        tmp_holder["feeltemperature"] = measurement.get("feeltemperature")
        tmp_holder["windgusts"] = measurement.get("windgusts")
        tmp_holder["windspeedBft"] = measurement.get("windspeedBft")
        tmp_holder["humidity"] = measurement.get("humidity")
        tmp_holder["precipitation"] = measurement.get("precipitation")
        tmp_holder["sunpower"] = measurement.get("sunpower")
        tmp_holder["stationid"] = measurement.get("stationid")

        weather_station_measurements.append(tmp_holder)

    # weather station:
    # scraped_data -> actual -> stationmeasurements[] = List of dictionaries
    weather_station_json = scraped_data["actual"]["stationmeasurements"]
    for measurement in weather_station_json:
        tmp_holder = {}

        tmp_holder["stationid"] = measurement.get("stationid")
        tmp_holder["stationname"] = measurement.get("stationname")
        tmp_holder["temperature"] = measurement.get("temperature")
        tmp_holder["lat"] = measurement.get("lat")
        tmp_holder["lon"] = measurement.get("lon")
        tmp_holder["regio"] = measurement.get("regio")

        weather_stations[tmp_holder["stationid"]] = tmp_holder

    return weather_station_measurements, weather_stations
