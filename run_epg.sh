#!/bin/bash
# Wait 30 seconds for the WiFi/Ethernet to connect
sleep 30

# Go to the project directory
cd /mnt/data/FIX-EPG-TITLE/


# 1. Print a timestamp header into the log
echo "------------------------------------------" >> log.txt
echo "EPG UPDATE STARTED AT: $(date)" >> log.txt

# 2. Start program in the project directory
python3 -u /mnt/data/FIX-EPG-TITLE/fix_epg1.py >> log.txt 2>&1

# 3. Print a closing timestamp
echo "EPG UPDATE FINISHED AT: $(date)" >> log.txt

