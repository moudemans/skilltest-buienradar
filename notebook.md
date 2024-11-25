# Project structure
Below more information on the project structure and functionality found in each scripts
.
 * [docs](./docs)
   * [ERD of relational database (dark)](docs/buienradar_ERD_dark.drawio.png)
   * [ERD of relational database (light)](docs/buienradar_ERD_light.drawio.png)
   * [ERD of relational database XML](docs/ERD.drawio)
   * * [ERD of relational database XML](docs/ERD.drawio)


 * [main.py](./main.py) - start of application, calling all functionalies requested
 * [scraper.py](./scraper.py) - Retrieves json data from provided url and writes it to json format in memory
 * [parser.py](./parser.py) - Retrieves the desired datapoints from the collected json data and provides the option to define default values
 * [database.py](./database.py) - Creates a database if it does not yet exist. Also provides functions to interact with the database
 * [viewer.py](./viewer.py) - Retrieves specific data from database, contains hardcoded queries

# Assignment notes
## Part 1

Todo:
- indexing tables on most used columns dependent on Part 3 -> This is very depending on the types of queries used most. It does not make sense to index continous values.  


## Part 2

Q5 Which weather station recorded the highest temperature? =  Meetstation Arcen \
Q6 What is the average temperature? =  11.288571428571423 \
Q7 What is the station with the biggest difference between feel temperature and the actual temperature? =  'Meetstation Zeeplatform F-3' \
Q8 Which weather station is located in the North Sea? =  'Meetstation Zeeplatform F-3'
# Question 3
The script written for part 1 needs to be called every 20 minutes. Whether the data needs to be polled exactly when it is posted, or somewhere in the timeslot is up to the client. The schedule can be created s.t. it runs every 20 minutes or let it run on specific times on a day (which most likely means more configuration work). Depending on the resources available from the client there are a few possibilities:

If there is some cloud platform / serverless service available, one can use said platform to run python scripts automatically. In Azure for example one can create scheduled [tasks](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios?pivots=programming-language-csharp#run-scheduled-tasks), which can call the python script to fetch the data from the api and store the data in the sqllite database. Another way to achieve similar results is to set up a [data factory pipeline](https://learn.microsoft.com/en-us/azure/batch/tutorial-run-python-batch-azure-data-factory)  

If the client has an in-house server, the script can be run from there. For example, if they run a linux server the script can be schedules as described [here](https://www.geeksforgeeks.org/scheduling-python-scripts-on-linux/)


Some conciderations depending on the requirements from the client:

**How long will this service run for?** \
An important question is how long the client expects to use this service. Each time the data is updated, the measurements table grows a with ~40 records (120 records a day, 43800 records a year). Even with millions of records, sql should keep working efficiently which means this script can run for more then 50 years.

**Can the posted data change within a time slot** \
The script currently can only retrieve the data once in a time slot. If the script is run again within a time slots, the datapoints are not updated. If the client expects the data to change within a time slot, this could have consequences for how often the script needs to be run as well as the functionality of the script.


**Should there be backups of the data** \
The script now only writes the data to the device it is run on. If back-ups are needed then a proper storage solution should be picked (like azure sql database/azure blob storage).