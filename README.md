This program repair <title>Movie</title> in the https://tvpass.org/epg.xml

Steps:
- Load https://tvpass.org/epg.xml
- Change <title>Movie</title> with real movie name from <sub_title>Movie Name</sub_title>
- Changed fixed_epg1.xml set to URL: http://localhost:8080/fixed_epg1.xml for load to IPTVnator 
- Program starts with anacron after boot - see in log.txt
- Starting with the script run_epg.sh
