import json
import sqlite3

database = 'buienradar.db'

startup_statements = [

    """CREATE TABLE IF NOT EXISTS wheather_stations (
            stationid INT       PRIMARY KEY
            , stationname STRING NOT NULL 
            , lat FLOAT 
            , lon FLOAT 
            , regio VARCHAR(255)
    
        );""",
    """CREATE TABLE IF NOT EXISTS measurements (
            measurementid integer primary key AUTOINCREMENT
            , timestamp DATETIME  NOT NULL
            , temperature FLOAT 
            , groundtemperature FLOAT
            , feeltemperature  FLOAT        
            , windgusts  FLOAT
            , windspeedBft    INT
            , humidity      INT 
            , precipitation    INT
            , sunpower     INT
            , stationid      INTEGER NOT NULL
            , FOREIGN KEY (stationid) REFERENCES wheather_stations(stationid) ON DELETE CASCADE ON UPDATE CASCADE
        );"""

]


def start():
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()

            # execute statements
            for statement in startup_statements:
                cursor.execute(statement)
                conn.commit()

            return conn



    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        sqlite3.rollback()


def add_weather_station(conn, station):
    sql = '''INSERT OR IGNORE  INTO wheather_stations(stationid, stationname, lat, lon, regio)
                 VALUES(?,?,?,?,?) '''

    # create a cursor
    cur = conn.cursor()

    # execute the INSERT statement
    values = [station["stationid"], station["stationname"], station["lat"], station["lon"], station["regio"]]
    cur.execute(sql, values)

    # commit the changes
    conn.commit()


def add_weather_stations(conn, weather_stations: json):
    for key_id in weather_stations.keys():
        station = weather_stations[key_id]
        add_weather_station(conn, station)


def add_weather_station_measurement(conn, measurement):
    sql = '''INSERT  OR IGNORE  INTO measurements(  timestamp, temperature, groundtemperature, feeltemperature, windgusts, windspeedBft, humidity, precipitation, sunpower, stationid) 
                 VALUES(?,?,?,?,?,?,?,?,?,?) '''

    # create a cursor
    cur = conn.cursor()

    # execute the INSERT statement
    values = [
        measurement["timestamp"],
        measurement["temperature"],
        measurement["groundtemperature"],
        measurement["feeltemperature"],
        measurement["windgusts"],
        measurement["windspeedBft"],
        measurement["humidity"],
        measurement["precipitation"],
        measurement["sunpower"],
        measurement["stationid"]
    ]
    cur.execute(sql, values)

    # commit the changes
    conn.commit()


def add_weather_station_measurements(conn, weather_station_measurements):
    for measurement in weather_station_measurements:
        add_weather_station_measurement(conn, measurement)
