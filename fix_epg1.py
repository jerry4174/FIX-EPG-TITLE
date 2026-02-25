#  fix_epg1.py  17.02.26
#  basic program to set subtitle for title
#  if title = Movie or empty.
#  Repair only for HBO channels.
#  Input is local epg.xml
#  The result is fixed_epg1.xml
#  which contains all EPG records.
#  25.02.2026 Last version
#####################
import xml.etree.ElementTree as ET
import http.server
import socketserver
import threading
import requests

# --- SETTINGS ---
EPG_URL = "https://tvpass.org/epg.xml"
SAVE_PATH = "/mnt/data/FIX-EPG-TITLE/epg.xml"
OUTPUT_FILE = "fixed_epg1.xml"
OUTPUT_FILE_PATH = "/mnt/data/FIX-EPG-TITLE/fixed_epg1.xml"
PORT = 8080

#   download_epg():
print(f"Downloading fresh EPG from {EPG_URL}...")
response = requests.get(EPG_URL, timeout=30)
with open(SAVE_PATH, 'wb') as f:
    f.write(response.content)
    print("Download complete.")


tree = ET.parse('epg.xml')
root = tree.getroot()

for programme in root.findall('programme'):
    # Get the channel attribute from the <programme> tag
    channel_id = programme.get('channel', '')

    # Check if 'HBO' is in the channel ID (case-insensitive check)
 #   if "HBO" in channel_id.upper():
    title = programme.find('title')
    subtitle = programme.find('sub-title')

    if title is not None and title.text == "Movie" and subtitle is not None:
            title.text = subtitle.text  # Move the movie name to the Title
            print(f"Fixed [{channel_id}]: {title.text}")

tree.write(OUTPUT_FILE_PATH, encoding='utf-8', xml_declaration=True)

# --- SERVER LOGIC ---
class Handler(http.server.SimpleHTTPRequestHandler):
      def log_message(self, format, *args): return


# def start_server():
socketserver.TCPServer.allow_reuse_address = True
try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"\nSUCCESS! Server is running.")
            print(f"In IPTVnator, use EPG URL: http://localhost:{PORT}/{OUTPUT_FILE}")
            httpd.serve_forever()
except Exception as e:
        print(f"Server Error: {e}")