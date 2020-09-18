## Database Configuration and Development

### Configuration
I have configured apache web server 2.4.41, mysql 8.0.11, php7 to run the following MariaDB (fork of mySQL) database using phpMyAdmin visualization tool.

### Development
1.  I have named my database **FIRE_DETECTION**. The following SQL command carries out the action:

<!-- blank line -->
----
<!-- blank line -->
CREATE DATABASE FIRE_DETECTION;
<!-- blank line -->
----
<!-- blank line -->

2.  Table **USER** has been created in the database. It logs in registered system users, keeps track of their records and manages their session. The following SQL command carries out the action:

<!-- blank line -->
----
<!-- blank line -->
	CREATE TABLE USER(
  
    	USERID int,
  
		NAME varchar(20),
  
		PHONE_NUMBER char(10),
  
		PASSWORD varchar(10),
  
		LOGINSTATUS char(10),
  
		ADMINISTRATION varchar(20)
  
	);
<!-- blank line -->
----
<!-- blank line -->
The following alterations were made to the structure of the table:
- _USERID_ was set to be the primary key.
- _PHONE_NUMBER_ was set to be an unique field.

3.  Table **SENSOR** has been created in the database. It keeps track of registered sensors. The following SQL command carries out the action:

<!-- blank line -->
----
<!-- blank line -->
	CREATE TABLE SENSOR(

    	SENSORID int,
  
		LOCATION char(25),
  
		TEMPERATURE char(10),
  
		HUMIDITY char(10),
  
		ALERT char(35),
  
		SENSOR_TYPE varchar(10)
  
	);
<!-- blank line -->
----
<!-- blank line -->
The following alterations were made to the structure of the table:
- _SENSORID_ was set to be the primary key.
- _LOCATION_ was set to be an unique field.

4.  Table **READINGS** has been created in the database. It keeps track of registered sensors and their readings (ideal for many sensors). The following SQL command carries out the action:

<!-- blank line -->
----
<!-- blank line -->
	CREATE TABLE READINGS(
    		
		SENSORID int,
    		
		TEMPERATURE char(10),
    		
		HUMIDITY char(10),
    		
		ALERT char(35),
    		
		TIME char(16)
	
	);
<!-- blank line -->
----
<!-- blank line -->
The following alterations were made to the structure of the table:
- _SENSORID_ was set to be a primary key.
- _TIME_ was set to be a primary key.

## Sample Output

### User Table
| USERID          | NAME                   | PHONE_NUMBER           | PASSWORD               | LOGINSTATUS            | ADMINISTRATION         |
| :--------------:| :---------------------:| :---------------------:| :---------------------:| :---------------------:| :---------------------:|
|  1              | Steven Thomi           |0701071594              |1234                    |Logged In               |Forest.CONGO            |
|  2              | Steve Thomi            |0715789786              |5678                    |Logged Out              |FireStation.EAST        |

### Sensor Table
| SENSORID        | LOCATION                      |SENSOR_TYPE	|
| :--------------:| :----------------------------:| :----------:|
|  1              | 33 48' 58" S 18 28' 22.0" E   |dh22		|
|  2              | 33 48' 58" S 18 28' 22.5" E   |dh22		|

### Readings Table
| SENSORID        | TEMPERATURE      | HUMIDITY         | ALERT                  |TIME		   |
| :--------------:| :---------------:| :---------------:| :---------------------:| :--------------:|
|  1              |50°C              |85%               |Alert.HIGH_TEMPARATURE  |18-09-2020 13:30 |
|  2              |25°C              |70%               |Alert.NO_ALERT          |18-09-2020 13:35 |

**N.B. This document is modified alongside the logfile to maintain a common vision throughout the repository.**
