This program repair <title>Movie</title> in the https://tvpass.org/epg.xml

Steps:
- Load https://tvpass.org/epg.xml
- Change <title>Movie</title> with real movie name from <sub_title>Movie Name</sub_title>
- Changed fixed.xml set to URL: http://localhost:8080/fixed.xml for load to IPTVnator 
- Program starts with anacron after boot - see in log.txt
- Starting with script run_epg.sh
