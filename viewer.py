import database


def get_highest_temperature_station(conn) -> str:
    query =     """
    SELECT stationname    
    from measurements
    LEFT JOIN main.wheather_stations ws on ws.stationid = measurements.stationid
    ORDER BY
    temperature DESC
    LIMIT 1
        """


    return database.execute_read_query(conn, query)[0][0]

def get_average_temp(conn) -> str:
    query =     """
    SELECT AVG(temperature)    
    from measurements
        """


    return database.execute_read_query(conn, query)[0][0]

def get_max_temp_deviation(conn) -> str:
    query =     """
    SELECT stationname
    , ABS(feeltemperature - temperature) as temperature_diff
        
    from measurements
    LEFT JOIN main.wheather_stations ws on ws.stationid = measurements.stationid
    ORDER BY
    temperature_diff DESC
    LIMIT 1
        """
    return database.execute_read_query(conn, query)[0]

