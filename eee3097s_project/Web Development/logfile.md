| Date                  | Modification                                                                           |
| :--------------------:| :------------------------------------------------------------------------------------- |
|  17th September 2020  | LOGINSTATUS field of USER table updated to length 10 of char data type                 |
|  18th September 2020  | ALTER TABLE SENSOR                                                                     |
|                       | DROP COLUMN TEMPERATURE;                                                               |
|  18th September 2020  | ALTER TABLE SENSOR                                                                     |
|                       | DROP COLUMN HUMIDITY;                                                                  |
|  18th September 2020  | ALTER TABLE SENSOR                                                                     |
|                       | DROP COLUMN ALERT;                                                                     |
|  18th September 2020  | CREATE TABLE READINGS(                                                                 |
|                       | SENSORID int, TEMPERATURE char(10), HUMIDITY char(10), ALERT char(35), TIME char(16)   |
|                       | );                                                                                     |
|  18th September 2020  | ALTER TABLE READINGS                                                                   |
|                       | ADD PRIMARY KEY(`SENSORID`,`TIME`);                                                                     |
