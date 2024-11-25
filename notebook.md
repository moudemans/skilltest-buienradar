# Notes during assignment
https://jsonformatter.org/json-viewer


Todo:
- check SQL queries, improve on the format / how it is stored
- Check typing and relationships of sql tables
- indexing tables on most used columns
- new values for stations

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