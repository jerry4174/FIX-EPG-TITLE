# EPG Changer

## Purpose
This program repair <title>Movie</title> in the https://tvpass.org/epg.xml

## Project Description
Steps:
- Load https://tvpass.org/epg.xml
- Change <title>Movie</title> with real movie name from <sub_title>Movie Name</sub_title>
- Changed fixed_epg1.xml set to URL: http://localhost:8080/fixed_epg1.xml for load to IPTVnator 
- Program starts with anacron after boot - see in log.txt
- Starting with the script run_epg.sh

## Usage
- If the EPG is out of time (USA - Europe difference) a reload must be done.  
- Kill the  the program:
- ps -ef|grep epg
- sudo kill id of run_epg.sh
- Go to working directory
- Start the shell:./run_epg.sh
- check in log file:  
SUCCESS! Server is running.
In IPTVnator, use EPG URL: http://localhost:8080/fixed_epg1.xml
- IPTVnator Settings: CLEAR EPG DATA, refresh http://localhost:8080/fixed_epg1.xml


## License 
Distributed under the MIT License. See https://en.wikipedia.org/wiki/MIT_License for more information.
