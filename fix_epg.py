#  fix_epg.py  17.02.26
#  basic program to set subtitle for title
#  if title = Movie or empty.
#  Input is local epg.xml
#  The result is fixed_epg.xml
#  which contains all EPG records.
# to do:
# load https://tvpass.org/epg.xml  ok 21.2.2026
# make url from fixed_epg.xml for load to IPTVnator ok 21.2.2026
#################################################################


import xml.etree.ElementTree as ET
import http.server
import socketserver
import threading
import requests

# --- SETTINGS ---
EPG_URL = "https://tvpass.org/epg.xml"
SAVE_PATH = "/mnt/data/FIX-EPG-TITLE/epg.xml"
OUTPUT_FILE = "fixed.xml"
PORT = 8080

def download_epg():
    print(f"Downloading fresh EPG from {EPG_URL}...")
    response = requests.get(EPG_URL, timeout=30)
    with open(SAVE_PATH, 'wb') as f:
        f.write(response.content)
    print("Download complete.")

def process_xml():
    tree = ET.parse(SAVE_PATH)
    root = tree.getroot()
    new_root = ET.Element('tv')

tree = ET.parse('epg.xml')
root = tree.getroot()


for programme in root.findall('programme'):
    # Get the channel attribute from the <programme> tag
    channel_id = programme.get('channel', '')
    title = programme.find('title')
    subtitle = programme.find('sub-title')
    if title is not None and title.text == "Movie" and subtitle is not None:
        title.text = subtitle.text  # Move the movie name to the Title
        print(f"Fixed [{channel_id}]:  {title.text}")
    else:
       print(f"Non Fixed [{channel_id}]:{title.text}")

tree.write('fixed_epg.xml', encoding='utf-8', xml_declaration=True)

# --- SERVER LOGIC ---
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args): return


def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"\nSUCCESS! Server is running.")
            print(f"In IPTVnator, use EPG URL: http://localhost:{PORT}/{OUTPUT_FILE}")
            httpd.serve_forever()
    except Exception as e:
        print(f"Server Error: {e}")


# --- EXECUTION ---
if __name__ == "__main__":
    try:
        download_epg()
        process_xml()

        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()

        input("\nPress ENTER to shut down the server and exit.\n")
    except Exception as e:
        print(f"An error occurred: {e}")