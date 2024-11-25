import sqlite3


database = 'buienradar.db'

startup_statements = [

    """CREATE TABLE IF NOT EXISTS wheather_stations (
            stationid INT       PRIMARY KEY
            , stationname STRING NOT NULL 
            , lat DATETIME 
            , lon FLOAT 
            , regio VARCHAR(255)
    
        );""",
    """CREATE TABLE IF NOT EXISTS measurements (
            id BINARY(16) PRIMARY KEY 
            , measurementid INT NOT NULL
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



    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        sqlite3.rollback()