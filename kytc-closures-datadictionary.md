# Project Data Dictionary

## Overview

This file provides a data dictionary for the transportation records dataset. The dataset includes information related to transportation events, routes, and conditions.

## Data Dictionary

1. **District**
   - Data Type: Integer (int64)
   - Description: KYTC divides the state into 12 geographic regions.  Those areas start with District 1 in the far West and end with District 12 in the far East.
   - Examples: 1, 2, 3, etc.

2. **County**
   - Data Type: Object (string)
   - Description: The name of the county where the event occurred.   County names are all proper case.
   - Examples: Fayette, Frankfort, Jefferson, etc.

3. **Route**
   - Data Type: Object (string)
   - Description: The route name associated with the incident.
   - Example: KY-80, US-60, I-69

4. **Road_Name**
   - Data Type: Object (string)
   - Description: The name of the road associated with the transportation records.
   - Example: DONALDSON CREEK RD, BRIDGE ST, I-69, I-69 NC
   - NOTE: In this datasets, you will see values such as I-69 (cardinal direction of travel) and I-69 NC (non-cardinal direction of travel).

5. **Begin_MP**
   - Data Type: Float
   - Description: The milepost where the event or condition begins on the road.  In many cases, you will notice that the begin and ending mile points are equal.  This is because the event was reported at a single mile post and the length of the closure was unknown at the time of the report.

6. **End_MP**
   - Data Type: Float
   - Description: The milepost where the event or condition ends on the road.  In many cases, you will notice that the begin and ending mile points are equal.  This is because the event was reported at a single mile post and the length of the closure was unknown at the time of the report.

7. **Comments**
   - Data Type: Object (string)
   - Description: Additional comments or information related to the transportation event.

8. **Reported_On**
   - Data Type: Datetime
   - Description: The date and time when the transportation event was reported.  All reports are in Eastern Standard Time.

9. **End_Date**
   - Data Type: Datetime
   - Description: The date and time when the transportation event concluded or was resolved.  All reports are in Eastern Standard Time.

10. **latitude**
    - Data Type: Float
    - Description: The latitude coordinate associated with the location of the transportation event.

11. **longitude**
    - Data Type: Float
    - Description: The longitude coordinate associated with the location of the transportation event.

12. **Duration_Default**
    - Data Type: Timedelta
    - Description: The default duration of the transportation event.  This duration value is the default output of Pandas when calculating the difference between two datetimes.

13. **Duration_Hours**
    - Data Type: Float
    - Description: The duration of the transportation event in hours.  This duration is used for reporting.

