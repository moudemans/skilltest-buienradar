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