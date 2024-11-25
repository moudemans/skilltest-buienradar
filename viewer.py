import database

# Selects station from stations table where the [temperature] in the measurements table is highest
def get_highest_temperature_station(conn) -> str:
    query =     """
    SELECT stationname    
    from measurements
    LEFT JOIN main.weather_stations ws on ws.stationid = measurements.stationid
    ORDER BY
    temperature DESC
    LIMIT 1
        """


    return database.execute_read_query(conn, query)[0][0]

# Calculates the average temperature in the measurements table
def get_average_temp(conn) -> str:
    query =     """
    SELECT AVG(temperature)    
    from measurements
        """


    return database.execute_read_query(conn, query)[0][0]

# Calculates the maximum temperature difference between the columns [feeltemperature] and [temperature]
def get_max_temp_deviation(conn) -> str:
    query =     """
    SELECT stationname
    , ABS(feeltemperature - temperature) as temperature_diff
        
    from measurements
    LEFT JOIN main.weather_stations ws on ws.stationid = measurements.stationid
    ORDER BY
    temperature_diff DESC
    LIMIT 1
        """
    return database.execute_read_query(conn, query)[0]


#  Returns all stations in the region provided in function parameters
def get_station_in_region(conn, region) -> str:
    query = """
    SELECT stationname
    
    from weather_stations
    WHERE regio=?
    
        """.format(region)
    return database.execute_read_query_with_param(conn, query, (region,))[:][0]