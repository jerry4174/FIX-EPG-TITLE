# EPG Changer

## Purpose
This program repair <title>Movie</title> in the https://tvpass.org/epg.xml

## Project Description
Steps:
- Load https://tvpass.org/epg.xml
- Change <title>Movie</title> with real movie name from <sub_title>Movie Name</sub_title>
- Changed fixed_epg1.xml set to URL: http://localhost:8080/fixed_epg1.xml for load to IPTVnator 

## Configuration
In: /etc/systemd/system/epg-fix.service
- alias epg-start='sudo systemctl start epg-fix.service && echo "EPG Server Started."'
- alias epg-stop='sudo systemctl stop epg-fix.service && echo "EPG Server Stopped."'
- alias epg-check='systemctl status epg-fix.service'



## Usage
- Start program with epg-start
- Stop program with epg-stop
- Check program running with epg-check
- Show log with journalctl -u epg-fix.service --no-pager

## License 
Distributed under the MIT License. See https://en.wikipedia.org/wiki/MIT_License for more information.
