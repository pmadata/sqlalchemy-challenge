#sqlalchemy-challange
## SurfsUp
###Resources
- for this analysis we utilized the database station.csv and measurement.csv
### climate_starter.ipynb
Queries to identify :
- Most recent 12 months precipitation data overview
![image](https://github.com/pmadata/sqlalchemy-challenge/assets/143486132/d7bb266d-387b-43f3-9cb4-3b4d695f107d)
![image](https://github.com/pmadata/sqlalchemy-challenge/assets/143486132/36c7546e-4c93-4551-bf0a-9f01a1bcb5a7)

- Last 12 months temperature observation from station with higherst number of observations
![image](https://github.com/pmadata/sqlalchemy-challenge/assets/143486132/0c7fc4dc-f85a-4fa7-b80e-899273495421)

### app.py
From queries above an API has been developed using Flask to have access to the results for the following:
  f"Available route list:"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs" (tempertures)
        f"/api/v1.0/<start>" (from a starting date, min, max and average temperature)
        f"/api/v1.0/<start>/<end>") (from a starting  and ending date, min, max and average temperature)

